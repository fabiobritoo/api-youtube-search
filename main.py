from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from youtube_search import YoutubeSearch
import json

# uvicorn main:app --reload  

class Item(BaseModel):
    nome_filme: str

app = FastAPI()

@app.post("/")
def post_root(item: Item):
    results = YoutubeSearch("trailer " + item.nome_filme, max_results=1).to_json()
    url = json.loads(results)["videos"][0]["url_suffix"]
    link = "https://www.youtube.com" + url
    return link


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}