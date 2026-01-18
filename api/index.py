from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is Running! Use /playlist to get your M3U link."}

@app.get("/playlist")
async def get_playlist():
    # Aapka original M3U link
    url = "https://raw.githubusercontent.com/Sanskar318/stream/master/playlist.m3u8"
    try:
        response = requests.get(url)
        return PlainTextResponse(content=response.text)
    except Exception as e:
        return {"error": str(e)}
        
