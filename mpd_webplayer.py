from mpd import MPDClient
import uvicorn
from fastapi import FastAPI
import threading
import time
app = FastAPI()
client: MPDClient = MPDClient()  # create client object

PLAYER = "127.0.0.1"

def init_player():
    connect()
    client.clear()  # Clear current playlist
    songs = client.listall()
    for song in songs:
        client.add(song['file'])
        print(f" {song['file']}")
    print(f"status {client.status()}")
    close()

def connect():
    # client.timeout = 10  # network timeout in seconds (floats allowed), default: None
    client.connect(PLAYER, 6600)  # connect to localhost:6600

def close():
    client.disconnect()

@app.get("/play")
async def play():
    connect()
    # Shuffle the playlist
    client.shuffle()
    # play
    client.play()
    close()
    return {"message": "Playing"}


@app.get("/pause")
async def pause():
    connect()
    client.pause(1)
    close()
    return {"message": "Paused"}


@app.get("/stop")
async def pause():
    connect()
    client.stop()
    close()
    return {"message": "Stopped"}


@app.get("/next")
async def status():
    connect()
    client.next()
    close()
    return {"response": "OK"}


@app.get("/status")
async def status():
    connect()
    status = client.status()
    close()
    return {"status": status}


@app.get("/volume")
async def volume(volume: int):
    connect()
    client.setvol(volume)
    close()
    return {"message": f"volume: {volume}"}

@app.get("/volup")
async def volup():
    connect()
    client.volume(5)
    status = client.status()
    close()
    return {"message": f"volume: {status['volume']}"}


@app.get("/voldown")
async def voldown():
    connect()
    client.volume(-5)
    status = client.status()
    close()
    return {"message": f"volume: {status['volume']}"}


if __name__ == "__main__":
    init_player()
    uvicorn.run(app, host="0.0.0.0", port=8000)
