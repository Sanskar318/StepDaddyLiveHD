from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Server is Live", "msg": "Use /playlist to get M3U"}

@app.get("/playlist")
def get_playlist():
    # Aapki main playlist ka link
    target_url = "https://raw.githubusercontent.com/Sanskar318/stream/master/playlist.m3u8"
    r = requests.get(target_url)
    return r.text
  
