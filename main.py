from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from youtube_search import YoutubeSearch
import json
import requests
import re

# uvicorn main:app --reload  

class Search(BaseModel):
    movie_name: str
    type: Union[str, None] = None
    class Config:
        schema_extra = {
            "example": {
                "movie_name": "Os Trapalhões",
                "type": "Filme"
            }
        }
class Platform(BaseModel):
    platform_name: str
    class Config:
        schema_extra = {
            "example": {
                "platform_name": "telecine-play"
            }
        }

app = FastAPI(    
    title='NassauFlix API',
    description='API desenvolvida para ser utilizada no projeto NassauFlix. Seu objetivo é converter nomes de Séries/Filmes em youtube links para ser apresentado na aplicação.')

@app.post("/", tags=["Obter Links"])
def post_root(search: Search):  

    if search.type is None:  
        search.type = ""

    results = YoutubeSearch("trailer " + search.type + " " + search.movie_name, max_results=1).to_json()

    link = "https://www.youtube.com" + json.loads(results)["videos"][0]["url_suffix"]
    title = json.loads(results)["videos"][0]["title"]
    duration = json.loads(results)["videos"][0]["duration"]   

    result = {"title": title,"link": link,"duration": duration }

    return result

@app.post("/plataforma/", tags=["Obter Filmes por Plataforma"])
def post_plataforma(plat: Platform):  


    filmes = []
    for pagina in range(0,50):
        url = f"https://www.filmelier.com/br/platforms/{plat.platform_name}/ajax?page={pagina}"
        site = requests.get(url).text
        
        regex = r"(?<=alt=)(.*?)(?= width=)"
        matches = re.finditer(regex, site)
        tamanho = len(site)
        for match in matches:
            filmes.append(match.group().replace("\"",""))
        
        if tamanho == 0:
            print("Página:", pagina)
            print("Tamanho:", tamanho)
            break

    return filmes


@app.get("/", tags=["Root"])
def read_root():
    return {"Abra nassauflix.herokuapp.com/docs para ver as especificações da API"}
