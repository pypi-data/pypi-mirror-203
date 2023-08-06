"""Lightweight ORM to perform simple CRUD operations on FaunaDB collections and provision indexes

   the fauna query object is available also within the class for further customization
"""

from __future__ import annotations

import asyncio

from typing import List, Optional, Any, Callable

from aiofauna import query as q

from aiofauna.errors import AioFaunaException

from aiofauna.json import JSONModel  # pylint: disable=no-name-in-module

from aiofauna.client import AsyncFaunaClient

from pydantic import BaseModel

class Fql(BaseModel):
    field: str
    operator: str
    value: Any

class AsyncFaunaModel(JSONModel):
    """

    A base model class for interacting with FaunaDB using asynchronous operations.


    Attributes:
    -----------

    ref: Optional[int]

        The FaunaDB reference ID of the model instance.

    ts: Optional[int]

        The timestamp of the model instance.


    Methods:
    --------

    client() -> AsyncFaunaClient:

        Returns an instance of AsyncFaunaClient to interact with FaunaDB.

    q() -> Expr:

        Returns an instance of Expr to wrap queries for FaunaDB.

    async provision() -> None:

        Creates the collections, indexes and unique_indexes for the model if they don't exist in FaunaDB.
    
    exists(ref: int) -> bool:

        Checks if a document exists in FaunaDB.

    find_unique(field: str, value: Any) -> Optional[AsyncFaunaModel]:

        Finds a document in FaunaDB by a unique field.

    find_many(field: str, value: Any) -> Optional[List[AsyncFaunaModel]]:

        Finds documents in FaunaDB by a non-unique field.

    find(ref: int) -> Optional[AsyncFaunaModel]:

        Finds a document in FaunaDB by its reference ID.

    find_all() -> Optional[List[AsyncFaunaModel]]:

        Finds all documents of the model in FaunaDB with pagination.

    delete_unique(field: str, value: Any) -> bool:

        Deletes a document in FaunaDB by a unique field.

    create() -> Optional[AsyncFaunaModel]:

        Creates a new document in FaunaDB if it complies with the unique constraints.

    update(ref: int, **kwargs) -> Optional[AsyncFaunaModel]:

        Updates a document in FaunaDB looking up by its reference ID and passing the fields to update.

    upsert() -> Optional[AsyncFaunaModel]:

        Upserts a document in FaunaDB if it complies with the unique constraints.

    query(query: str) -> Optional[List[AsyncFaunaModel]]:

        Runs a query in FaunaDB and returns the results.
    """

    ref: Optional[int] = None

    ts: Optional[int] = None

    def __init__(self, **data: Any) -> None:

        for field in self.__fields__.values():

            try:

                one_of = field.field_info.extra.get("oneOf")

                if isinstance(one_of, list):

                    if data.get(field.name) not in one_of:

                        raise ValueError(f"{field.name} must be one of {one_of}")

            except KeyError:

                continue

        super().__init__(**data)

    @classmethod
    def client(cls) -> AsyncFaunaClient:
        """

        Returns an instance of AsyncFaunaClient to interact with FaunaDB.


        Returns:
        --------

        AsyncFaunaClient:

            An instance of AsyncFaunaClient.
        """

        return AsyncFaunaClient()  # pylint: disable=no-value-for-parameter

    @classmethod
    def q(cls) -> Callable:
        """

        Returns an instance of Expr to build queries for FaunaDB.


        Returns:
        --------

        Expr:

            An instance of Expr.
        """

        return cls.client().query

    @classmethod
    async def provision(cls) -> None:
        """

        Creates a collection and indexes for the model if they don't exist in FaunaDB.


        Returns:
        --------

        None:

            None.
        """

        _q = cls.q()

        try:

            if not await _q(q.exists(q.collection(cls.__name__.lower()))):

                await _q(q.create_collection({"name": cls.__name__.lower()}))

                print(f"Created collection {cls.__name__.lower()}")

                await _q(
                    q.create_index(
                        {
                            "name": cls.__name__.lower(),
                            "source": q.collection(cls.__name__.lower()),
                        }
                    )
                )

                print(f"Created index {cls.__name__.lower()}")

            for field in cls.__fields__.values():

                if field.field_info.extra.get("unique"):

                    await _q(
                        q.create_index(
                            {
                                "name": f"{cls.__name__.lower()}_{field.name}_unique",
                                "source": q.collection(cls.__name__.lower()),
                                "terms": [{"field": ["data", field.name]}],
                                "unique": True,
                            }
                        )
                    )

                    print(
                        f"Created unique index {cls.__name__.lower()}_{field.name}_unique"
                    )
                    continue

                if field.field_info.extra.get("index"):

                    await _q(
                        q.create_index(
                            {
                                "name": f"{cls.__name__.lower()}_{field.name}",
                                "source": q.collection(cls.__name__.lower()),
                                "terms": [{"field": ["data", field.name]}],
                            }
                        )
                    )

                    print(f"Created index {cls.__name__.lower()}_{field.name}")
                    continue

        except AioFaunaException as exc:

            print(exc)

            return None

    @classmethod
    async def exists(cls, ref: int) -> bool:
        """

        Checks if a document exists in FaunaDB.


        Parameters:
        -----------
        ref: int

            The reference ID of the document to check.


        Returns:
        --------

        bool:

            True if the document exists, False otherwise.
        """

        try:

            return await cls.q()(
                q.exists(q.ref(q.collection(cls.__name__.lower()), ref))
            )

        except AioFaunaException as exc:

            print(exc)

            return False

    @classmethod
    async def find_unique(cls, field: str, value: Any) -> Optional[AsyncFaunaModel]:
        """

        Finds a document in FaunaDB by a unique field.


        Parameters:
        -----------
        field: str

            The name of the field to search.

        value: Any

            The value to search for.


        Returns:
        --------

        Optional[AsyncFaunaModel]:

            An instance of the model if found, None otherwise.
        """

        try:

            data = await cls.q()(
                q.get(q.match(q.index(f"{cls.__name__.lower()}_{field}_unique"), value))
            )
            return cls(
                **{
                    **data["data"],
                    "ref": data["ref"]["@ref"]["id"],
                    "ts": data["ts"] / 1000,
                }
            )

        except AioFaunaException as exc:
            print(exc)

            return None

    @classmethod
    async def find_many(cls, field: str, value: Any) -> Optional[List[AsyncFaunaModel]]:
        """

        Finds documents in FaunaDB by a field.


        Parameters:
        -----------
        field: str

            The name of the field to search.

        value: Any

            The value to search for.


        Returns:
        --------

        Optional[List[AsyncFaunaModel]]:

            A list of instances of the model if found, None otherwise.
        """

        try:

            _q = cls.q()

            refs = (
                await _q(
                    q.paginate(
                        q.match(q.index(f"{cls.__name__.lower()}_{field}"), value)
                    )
                )
            )["data"]

            data = await asyncio.gather(
                *[
                    _q(
                        q.get(
                            q.ref(q.collection(cls.__name__.lower()), ref["@ref"]["id"])
                        )
                    )
                    for ref in refs
                ]
            )

            return [
                cls(
                    **{**d["data"], "ref": d["ref"]["@ref"]["id"], "ts": d["ts"] / 1000}
                )
                for d in data
            ]

        except AioFaunaException as exc:

            print(exc)

            return None

    @classmethod
    async def find(cls, ref: int) -> Optional[AsyncFaunaModel]:
        """

        Finds a document in FaunaDB by its ID.


        Parameters:
        -----------
        ref: int

            The reference ID of the document to find.


        Returns:
        --------

        Optional[AsyncFaunaModel]:

            An instance of the model if found, None otherwise.
        """

        try:

            data = await cls.q()(q.get(q.ref(q.collection(cls.__name__.lower()), ref)))
            return cls(
                **{
                    **data["data"],
                    "ref": data["ref"]["@ref"]["id"],
                    "ts": data["ts"] / 1000,
                }
            )

        except AioFaunaException as exc:

            print(exc)

            return None

    @classmethod
    async def find_all(cls) -> Optional[List[AsyncFaunaModel]]:
        """

        Finds all documents of the model in FaunaDB.


        Returns:
        --------

        Optional[List[AsyncFaunaModel]]:

            A list of instances of the model if found, None otherwise.
        """

        try:

            _q = cls.q()

            refs = (await _q(q.paginate(q.match(q.index(cls.__name__.lower())))))[
                "data"
            ]

            data = await asyncio.gather(
                *[
                    _q(
                        q.get(
                            q.ref(q.collection(cls.__name__.lower()), ref["@ref"]["id"])
                        )
                    )
                    for ref in refs
                ]
            )

            return [
                cls(
                    **{**d["data"], "ref": d["ref"]["@ref"]["id"], "ts": d["ts"] / 1000}
                )
                for d in data
            ]

        except AioFaunaException as exc:

            print(exc)

            return None

    @classmethod
    async def delete_unique(cls, field: str, value: Any) -> bool:
        """

        Deletes a document in FaunaDB by a unique field.


        Parameters:
        -----------
        field: str

            The name of the unique field to use in the search.

        value: Any

            The value of the unique field to use in the search.


        Returns:
        --------

        bool:

            True if the document is deleted, False otherwise.
        """

        try:

            _q = cls.q()

            ref = await _q(
                q.get(q.match(q.index(f"{cls.__name__.lower()}_{field}_unique"), value))
            )

            await _q(q.delete(ref))

            return True

        except AioFaunaException as exc:

            print(exc)

            return False

    @classmethod
    async def delete(cls, ref: int) -> bool:

        """Delete a document by id"""

        try:

            await cls.q()(q.delete(q.ref(q.collection(cls.__name__.lower()), ref)))

            return True

        except AioFaunaException as exc:

            print(exc)

            return False

    async def create(self) -> Optional[AsyncFaunaModel]:
        """

        Creates a new document in FaunaDB.


        Parameters:
        -----------

        **kwargs:

            The data to create the new document with.


        Returns:
        --------

        Optional[AsyncFaunaModel]:

            An instance of the model if created successfully, None otherwise.
        """

        try:

            for field in self.__fields__.values():

                if field.field_info.extra.get("unique"):

                    instance = await self.find_unique(
                        field.name, self.dict()[field.name]  # type: ignore
                    )
                    if instance:
                        return instance

            data = await self.q()(
                q.create(
                    q.collection(self.__class__.__name__.lower()), {"data": self.dict()}
                )
            )
            return self.__class__(
                **{
                    **data["data"],
                    "ref": data["ref"]["@ref"]["id"],
                    "ts": data["ts"] / 1000,
                }
            )

        except AioFaunaException as exc:

            print(exc)

            return None

    @classmethod
    async def update(cls, ref: int, **kwargs) -> Optional[AsyncFaunaModel]:
        """

        Creates a new document in FaunaDB.


        Parameters:
        -----------

        **kwargs:

            The data to create the new document with.


        Returns:
        --------

        Optional[AsyncFaunaModel]:

            An instance of the model if created successfully, None otherwise.
        """

        try:

            data = await cls.q()(
                q.update(
                    q.ref(q.collection(cls.__name__.lower()), ref), {"data": kwargs}
                )
            )
            return cls(
                **{
                    **data["data"],
                    "ref": data["ref"]["@ref"]["id"],
                    "ts": data["ts"] / 1000,
                }
            )

        except AioFaunaException as exc:

            print(exc)

            return None

    async def upsert(self) -> Optional[AsyncFaunaModel]:
        """

        Creates a new document in FaunaDB.


        Parameters:
        -----------

        **kwargs:

            The data to create the new document with.


        Returns:
        --------

        Optional[AsyncFaunaModel]:

            An instance of the model if created successfully, None otherwise.
        """

        try:
            if not self.ref:

                return await self.create()

            return await self.update(self.ref, **self.dict())  # type: ignore

        except AioFaunaException as exc:

            print(exc)

            return None

    @classmethod
    async def query(cls, query: str) -> Optional[List[AsyncFaunaModel]]:
        """

        Queries FaunaDB using a string query and returns a list of instances of the model.


        Args:

            query (str): The query to use.


        Returns:

            Optional[List[AsyncFaunaModel]]: A list of instances of the model if found, None otherwises.
        """

        try:

            refs = (await cls.q()(q.paginate(q.match(q.query(query)))))["data"]

            data = await asyncio.gather(*[cls.q()(q.get(ref)) for ref in refs])

            return [
                cls(
                    **{**d["data"], "ref": d["ref"]["@ref"]["id"], "ts": d["ts"] / 1000}
                )
                for d in data
            ]

        except AioFaunaException as exc:

            print(exc)

            return None



    @classmethod
    async def filter(cls, queries:List[Fql]) -> Optional[AsyncFaunaModel]:
        """

        Queries FaunaDB using a string query and returns a list of instances of the model.
        
        Args:
            queries (List[Fql]): The query to use.
            
        Returns:
            Optional[AsyncFaunaModel]: A list of instances of the model if found, None otherwises.
        """
        
        for query in queries:
            if query.operator not in [
                "==",
                ">",
                ">=",
                "<",
                "<=",
                "!=",
                "where",
                "like",
                "search",
                "in"
            ]:
                raise ValueError("Invalid operator")
     
            field = query.field
            
            value = query.value
            
            operator = query.operator
            
            if operator == "==":
                
                fql = q.get(q.index(f"{cls.__name__.lower()}_{field}_unique"), value)
                
            elif operator == "where":
                
                fql = q.match(q.index(f"{cls.__name__.lower()}_{field}", value))
                
            elif operator == "like":
                
                fql = q.contains_str(q.lowercase(q.var(field)), value)
                
            elif operator == "search":
                
                queries_ = []
                
                for k,v in cls.__fields__.items():
                    
                    if v.type_ == str:
                        
                        queries_.append(q.contains_str(q.lowercase(q.var(k)), value))
                        
                fql = q.or_(*queries_)
                
            elif operator == "in":
                
                fql = q.contains_path(q.var(field), value)
                
            elif operator == "!=":
                
                fql = q.not_(q.get(q.index(f"{cls.__name__.lower()}_{field}", value)))
                
            elif operator == ">":
                
                fql = q.filter_(q.gt(q.var(field), value), q.var("ref"))
                
            elif operator == ">=":
                
                fql = q.filter_(q.gte(q.var(field), value), q.var("ref"))
                
            elif operator == "<":
                
                fql = q.filter_(q.lt(q.var(field), value), q.var("ref"))
                
            elif operator == "<=":
                
                fql = q.filter_(q.lte(q.var(field), value), q.var("ref"))
                
            else:
                
                raise ValueError("Invalid operator")
            
            return await cls.q()(fql)
        
        return None