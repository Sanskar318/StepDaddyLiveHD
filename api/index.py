from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "IPTV Server is Live!", "playlist_url": "/playlist"}

@app.get("/playlist")
async def get_playlist():
    # Aapka GitHub Raw M3U Link
    url = "https://raw.githubusercontent.com/Sanskar318/stream/master/playlist.m3u8"
    try:
        response = requests.get(url, timeout=10)
        # Playlist ko text format mein return karega
        return PlainTextResponse(content=response.text)
    except Exception as e:
        return {"error": f"Failed to fetch playlist: {str(e)}"}
        
