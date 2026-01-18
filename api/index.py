from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Live", "endpoint": "/playlist"}

@app.get("/playlist")
def get_playlist():
    # Aapka GitHub Raw M3U Link
    url = "https://raw.githubusercontent.com/Sanskar318/stream/master/playlist.m3u8"
    try:
        r = requests.get(url, timeout=10)
        return PlainTextResponse(content=r.text)
    except:
        return PlainTextResponse(content="Error fetching playlist", status_code=500)
        
