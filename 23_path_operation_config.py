
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Tags(Enum):
    items = "items"
    users = "users"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/0/", response_model=Item, tags=["items"])
async def create_item(item: Item):
    return item


@app.get("/items/0/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/0/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]

@app.get("/items/1/", tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]


@app.get("/users/1/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]

@app.post(
    "/items/1/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
)
async def create_item(item: Item):
    return item

@app.post(
        "/items/2/", 
        response_model=Item, 
        summary="Create an item",
        response_description="The created item",
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
