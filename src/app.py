import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
# load the .env file variables
load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
conn = Spotify(client_credentials_manager=client_credentials_manager)

artist_id = '4GvEc3ANtPPjt1ZJllr5Zl'

results = conn.artist_top_tracks(artist_id)

if results:
    tracks = results['tracks'][:10]
    top_tracks_info = [
        {
            'name': track['name'],
            'popularity': track['popularity'],
            'duration_minutes': (track['duration_ms'] / (1000 * 60)) 
        }
        for track in tracks
    ]

    df_tracks = pd.DataFrame(top_tracks_info)
    
    print(df_tracks)

plt.figure(figsize=(10,6))
plt.scatter(df_tracks['duration_minutes'], df_tracks['popularity'], color='blue')

plt.title('scatter plot of popularity vs duration')
plt.xlabel('duration(min)')
plt.ylabel('popularity')
plt.grid(True)
plt.show()