from mpd import MPDClient
import time


def test():
    client = MPDClient()  # create client object
    client.timeout = 10  # network timeout in seconds (floats allowed), default: None
    client.idletimeout = None  # timeout for fetching the result of the idle command is handled seperately, default: None
    client.connect("127.0.0.1", 6600)  # connect to localhost:6600
    print(client.mpd_version)  # print the MPD version
    print(client.find("any", "house"))  # print result of the command "find any house"
    client.iterate = True
    client.update()

    client.setvol(100)
    # songs = client.lsinfo("/var/lib/mpd/music")
    # songs = client.lsinfo("/media/savna/ESD-ISO/New/")
    # print(f"songs {len(songs)}")
    songs = client.listall()
    to_play = None
    for song in songs:
        to_play = song['file']
        print(f" {song['file']}")
    print(f"playlist {client.status()}")
    file_to_play = to_play

    # Clear the current playlist, add the song, and play it
    client.clear()  # Clear current playlist
    client.add(file_to_play)  # Add the chosen song to the playlist
    client.play()  # Start playing
    client.setvol(100)
    time.sleep(100)
    client.close()  # send the close command
    client.disconnect()  # disconnect from the server


def main():
    print("Starting MPD web player")


if __name__ == "__main__":
    test()