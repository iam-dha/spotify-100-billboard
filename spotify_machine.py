import spotipy
import requests
from dotenv import load_dotenv
import os
load_dotenv()
url = "https://accounts.spotify.com/"


class Spo():
    def __init__(self):
        self.client_id = os.environ['CLIENT_ID']
        self.client_secret = os.environ['CLIENT_SECRET']
        self.token = None
        self.get_access_token()
        self.header_auth = {
            "Authorization": f"Bearer  {self.token}"
        }

    def get_access_token(self):
        token_link = f"{url}/api/token"
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        res = requests.post(url=token_link, headers=header, data=body)
        self.token = res.json()['access_token']

    def search_song(self, song_name):
        search_endpoint = f"{url}v1/search"
        pass