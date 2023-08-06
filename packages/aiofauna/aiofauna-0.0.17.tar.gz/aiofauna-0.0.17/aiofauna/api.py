import asyncio
import aiohttp_cors
from typing import (
    Callable,
    Any,
    Awaitable,
    Union,
    List,
    Dict,
    Optional,
    Type,
    TypeVar,
    cast,
    overload,
)
from aiohttp.web import (
    Application,
    Request,
    Response,
    json_response,
    AppRunner,
    TCPSite,
)
from aiohttp.web_request import FileField
from aiofauna.odm import AsyncFaunaModel as BaseModel
from inspect import signature, isclass


def extract_parameters_without_request(params: dict):
    open_api_params = {}

    for name, param in params.items():
        type_ = param.annotation

        if type_ in (str, int, float, bool):
            open_api_params[name] = {
                "in": "query",
                "name": name,
                "required": True,
                "schema": {"type": type_, "default": param.default, "required": True},
            }

        elif issubclass(type_, BaseModel):
            open_api_params[name] = {
                "in": "body",
                "name": name,
                "required": True,
                "schema": {
                    "type": "object",
                    "default": param.default,
                    "required": True,
                },
            }

        elif issubclass(type_, FileField):
            open_api_params[name] = {
                "in": "formData",
                "name": name,
                "required": True,
                "schema": {"type": "file", "default": param.default, "required": True},
            }

        elif issubclass(type_, Request):
            continue

        else:
            continue

    return {}, open_api_params


def update_open_api(
    open_api: Dict[str, Any],
    path: str,
    method: str,
    func: Any,
    open_api_params: Dict[str, Any],
) -> None:
    # Ensure the required keys are present in the open_api dictionary"
    open_api["paths"].setdefault(path, {})[method.lower()] = {
        "summary": func.__name__,
        "description": func.__doc__,
        "parameters": list(open_api_params.values()),
        "responses": {"200": {"description": "OK"}},
    }


async def extract_parameters(request: Request, params: dict):
    args_to_apply = {}
    open_api_params = {}

    for name, param in params.items():
        type_ = param.annotation

        if type_ in (str, int, float, bool) and name in request.match_info:
            open_api_params[name] = {
                "in": "path",
                "name": name,
                "required": True,
                "schema": {"type": type_, "default": param.default, "required": True},
            }
            args_to_apply[name] = request.match_info[name]

        elif type_ in (str, int, float, bool) and name in request.query:
            open_api_params[name] = {
                "in": "query",
                "name": name,
                "required": True,
                "schema": {"type": type_, "default": param.default, "required": True},
            }
            args_to_apply[name] = type_(request.query[name])

        elif issubclass(type_, BaseModel):
            open_api_params[name] = {
                "in": "body",
                "name": name,
                "required": True,
                "schema": {
                    "type": "object",
                    "default": param.default,
                    "required": True,
                },
            }
            args_to_apply[name] = type_(**await request.json())

        elif issubclass(type_, FileField):
            open_api_params[name] = {
                "in": "formData",
                "name": name,
                "required": True,
                "schema": {"type": "file", "default": param.default, "required": True},
            }
            args_to_apply[name] = await request.post()

        elif issubclass(type_, Request):

            continue

        else:

            continue

    return args_to_apply, open_api_params


class Api(Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.openapi = {
            "openapi": "3.0.0",
            "info": {"title": "API", "version": "1.0.0"},
            "paths": {},
            "components": {},
        }
        self._route_open_api_params = {}
        
        @self.get("/openapi.json")
        async def openapi():
            return json_response(self.openapi)

    def document(self, path: str, method: str):
        def decorator(func):
            sig = signature(func)
            params = sig.parameters
            _, open_api_params = extract_parameters_without_request(params.copy())
            self._route_open_api_params[(path, method)] = open_api_params
            update_open_api(self.openapi, path, method, func, open_api_params)
            async def wrapper(*args, **kwargs):
                request: Request = args[0]
                args = args[1:]
                args_to_apply, _ = await extract_parameters(
                    request, params.copy()
                )
                if asyncio.iscoroutinefunction(func):
                    return await func(*args, **kwargs, **args_to_apply)
                return func(*args, **kwargs, **args_to_apply)
            wrapper._handler = func
            return wrapper
        return decorator
    
    def get(self, path: str, **kwargs):
        def decorator(func):
            self.router.add_get(path, self.document(path, "GET")(func), **kwargs)
            return func

        return decorator

    def post(self, path: str, **kwargs):
        def decorator(func):
            self.router.add_post(path, self.document(path, "POST")(func), **kwargs)
            return func

        return decorator

    def put(self, path: str, **kwargs):
        def decorator(func):
            self.router.add_put(path, self.document(path, "PUT")(func), **kwargs)
            return func

        return decorator

    def delete(self, path: str, **kwargs):
        def decorator(func):
            self.router.add_delete(path, self.document(path, "DELETE")(func), **kwargs)
            return func

        return decorator

    def patch(self, path: str, **kwargs):
        def decorator(func):
            self.router.add_patch(path, self.document(path, "PATCH")(func), **kwargs)
            return func

        return decorator

    def head(self, path: str, **kwargs):
        def decorator(func):
            self.router.add_head(path, self.document(path, "HEAD")(func), **kwargs)
            return func

        return decorator

    def options(self, path: str, **kwargs):
        def decorator(func):
            self.router.add_options(
                path, self.document(path, "OPTIONS")(func), **kwargs
            )
            return func

        return decorator

    def static(self, path: str, directory: str, **kwargs):
        def decorator(func):
            self.router.add_static(path, directory, **kwargs)
            return func

        return decorator
    
    async def docs(self, request):
        return json_response(self.openapi)
    
    async def listen(self, host: str = "0.0.0.0", port: int = 8000, **kwargs):
        
        cors = aiohttp_cors.setup(self, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
        })
        for route in list(self.router.routes()):
            cors.add(route)  
            handler = route.handler._handler
            path = route.resource.canonical
            method = route.method.lower()
            open_api_params = self._route_open_api_params.get((path, method), {})
            update_open_api(self.openapi, path, method, handler, open_api_params)
            
        self.router.add_get("/docs", self.document("/docs", "GET")(self.docs))
            
        runner = AppRunner(self)
        
        await runner.setup()
        
        site = TCPSite(runner, host, port)
        
        await site.start()
        
        print(f"http://{host}:{port}/docs")
        
        while True:
            
            await asyncio.sleep(3600)
            
            
