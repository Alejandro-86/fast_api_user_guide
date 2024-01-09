from typing import Any

from fastapi import FastAPI, Response
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse, RedirectResponse


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None  

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn_1(BaseUser):
    password: str

class Item_1(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.post("/items/0/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/0/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]

@app.post("/items/1/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/2/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

# Don't do this in production!
@app.post("/user/0/")
async def create_user(user: UserIn) -> UserIn:
    return user  

@app.post("/user/1/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

@app.post("/user/2/")
async def create_user(user: UserIn_1) -> BaseUser:
    return user

@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

