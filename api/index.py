from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests

app = FastAPI()

@app.get("/playlist")
def get_playlist():
    url = "https://raw.githubusercontent.com/Sanskar318/stream/master/playlist.m3u8"
    r = requests.get(url)
    return PlainTextResponse(content=r.text)

@app.get("/")
def home():
    return {"status": "Running"}
    
