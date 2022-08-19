from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from youtube_search import YoutubeSearch
import json

# uvicorn main:app --reload  

class Item(BaseModel):
    nome_filme: str
class Video(BaseModel):
    title: str
    link: str
    duration: str

app = FastAPI()

@app.post("/")
def post_root(item: Item):
    video: Video
    results = YoutubeSearch("trailer " + item.nome_filme, max_results=1).to_json()
    video.linklink = "https://www.youtube.com" + json.loads(results)["videos"][0]["url_suffix"]
    video.linktitle = json.loads(results)["videos"][0]["title"]
    video.linkduration = json.loads(results)["videos"][0]["duration"]   
    return video


@app.get("/")
def read_root():
    return {"Abra nassauflix.herokuapp.com/docs para ver as especificações da API"}
