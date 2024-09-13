# mpd-webplayer

FastAPI <-> MPd player interface

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