# mpd-webplayer

FastAPI <-> MPd player interface

## Enpoints

### API Endpoint: `/play`

**Description**: Plays playlist.

- **Method**: GET
- **URL**: `/play`

### API Endpoint: `/pause`

**Description**: Pauses playing.

- **Method**: GET
- **URL**: `/pause`

### API Endpoint: `/stop`

**Description**: Stops playing.

- **Method**: GET
- **URL**: `/stop`

### API Endpoint: `/next`

**Description**: Plays next song in playlist.

- **Method**: GET
- **URL**: `/next`


### API Endpoint: `/volume`

**Description**: Sets volume to desired value.

- **Method**: GET
- **URL**: `/volume?volume=80`

### API Endpoint: `/volup`

**Description**: Increases volume by 5.

- **Method**: GET
- **URL**: `/volup`


### API Endpoint: `/voldown`

**Description**: Decreases volume by 5.

- **Method**: GET
- **URL**: `/voldown`


## Installation

Clone this repo 

``` git clone https://github.com/nejcmedved/mpd-webplayer.git ```

``` cd mpd-webplayer```

### Create virtual env

``` python3 -m venv venv ```

``` source venv/bin/activate ```

``` pip install -r requirements.txt ```

### Run manually

``` python mpd_webplayer.py ```

### Prepare service file

Edit mpd-webplayer.service to fit your installation needs

``` cp mpd-webplayer.service /lib/systemd/system ```

``` systemctl daemon-reload ```

``` systemctl start mpd-webplayer ```

``` systemctl enable mpd-webplayer ```