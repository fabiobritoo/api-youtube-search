from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from youtube_search import YoutubeSearch
import json

# uvicorn main:app --reload  

class Item(BaseModel):
    nome_filme: str


app = FastAPI(    
    title='NassauFlix API',
    description='API desenvolvida para ser utilizada no projeto NassauFlix. Seu objetivo é converter nomes de Séries/Filmes em youtube links para ser apresentado na aplicação.')

@app.post("/")
def post_root(item: Item):    
    results = YoutubeSearch("trailer " + item.nome_filme, max_results=1).to_json()
    link = "https://www.youtube.com" + json.loads(results)["videos"][0]["url_suffix"]
    title = json.loads(results)["videos"][0]["title"]
    duration = json.loads(results)["videos"][0]["duration"]   
    result = {"title": title,"link": link,"duration": duration }

    return result


@app.get("/", tags=["Endpoints"])
def read_root():
    return {"Abra nassauflix.herokuapp.com/docs para ver as especificações da API"}
