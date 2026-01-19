from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Live", "playlist": "/playlist.m3u8"}

@app.get("/playlist.m3u8")
def get_playlist():
    # Ye asli API link hai jo playlist generate karti hai
    try:
        # Note: Ye script backend link se data fetch karegi
        # Agar ye link kaam na kare toh hum direct scraper use karenge
        api_url = "https://raw.githubusercontent.com/Sanskar318/stream/master/playlist.m3u8"
        r = requests.get(api_url, timeout=10)
        return PlainTextResponse(content=r.text)
    except:
        return PlainTextResponse(content="#EXTM3U\n# Error: Could not fetch channels")
        
