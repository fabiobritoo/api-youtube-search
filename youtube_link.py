import requests
from youtube_search import YoutubeSearch
import json

import webbrowser

def findYT(search):

    results = YoutubeSearch("trailer " + search, max_results=1).to_json()
    url = json.loads(results)["videos"][0]["url_suffix"]
    link = "https://www.youtube.com" + url

    webbrowser.open_new(link)

findYT("Hulk")

