## What is this?
A script to push plex events to a device via pushover.

Requirements:

- Python 2.7
- flask
- [python-pushover](https://github.com/Thibauth/python-pushover)
- plex
- [plex webhooks configured](https://support.plex.tv/articles/115002267687-webhooks/)
- [pushover account](https://pushover.net)
- [pushover application](https://pushover.net/apps/build) (`plex-notify`)

### Configuration
Create a file named `keys.py` and add your pushover [user key](https://pushover.net/)  as `USER_KEY` and the application key as `API_KEY`


## Run

`python plex-notify.py`

or

`./plex-notify.py`
