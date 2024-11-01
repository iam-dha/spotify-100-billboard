from crawler import Crawler
from spotify_machine import Spo
import spotipy
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
TOKEN_FILE_NAME = "token.txt"

date = input("Which day do you want to travel to? Type this format YYYY-MM-DD: ")
craw_tool = Crawler()
craw_tool.crawl(date_to_crawl=date)
data = craw_tool.get_data()

spo_track = []

spo_auth = spotipy.SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope="playlist-modify-private" ,redirect_uri= "http://example.com")
with open(file=TOKEN_FILE_NAME, mode='w') as file:
    file.write(spo_auth.get_access_token(as_dict=False))

with open(TOKEN_FILE_NAME) as file:
    token = file.read()
spo = spotipy.Spotify(auth=token, oauth_manager= spo_auth)
user_id = spo.current_user()['id']


for song in data:
    result = spo.search(q=f"track:{song} year{date[:4]}", type="track")
    try:
        spo_track.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        pass

playlist = spo.user_playlist_create(user=user_id, name = f"{date} Billboard 100", public=False, description=f"Top 100 Billboard on {date}")
spo.playlist_add_items(playlist_id=playlist['id'], items= spo_track)








