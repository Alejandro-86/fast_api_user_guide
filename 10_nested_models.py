from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item_list(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list[str] = []

class Item_set(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()

class Item_img(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None

class Item_img_list(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item_img]


@app.put("/items/1/{item_id}")
async def update_item(item_id: int, item: Item_list):
    results = {"item_id": item_id, "item": item}
    return results

@app.put("/items/2/{item_id}")
async def update_item(item_id: int, item: Item_set):
    results = {"item_id": item_id, "item": item}
    return results

@app.put("/items/3/{item_id}")
async def update_item(item_id: int, item: Item_img):
    results = {"item_id": item_id, "item": item}
    return results

@app.put("/items/4/{item_id}")
async def update_item(item_id: int, item: Item_img_list):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    for image in images:
        image.url
    return images

@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
