from time import sleep
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

scope = "user-read-playback-state,user-modify-playback-state"
SPOTIPY_REDIRECT_URI = 'http://google.com/'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyOAuth('016bcf887a234e3b84b01b3b9c03fac8', '734727041537466d9b05c429cc9c65bf', redirect_uri = SPOTIPY_REDIRECT_URI, scope = scope))

  
def main(song_lists: dict[str, list[str]]):
    total_songs:list[str] = create_song_list(song_lists=song_lists)
    start_current_device_playback(total_songs)
        
        
def find_total_num_songs(song_lists: dict[str, list[str]]):
    song_count: int = 0 
    for player in song_lists:
        player_song_list: list[str] = song_lists[player]
        song_count += len(player_song_list)

def create_song_list(song_lists: dict[str, list[str]]):
    round_songs: list[str] = []
    for player in song_lists:
        player_song_list: list[str] = song_lists[player]
        for song in player_song_list:
            song_str: str = song
            round_songs.append(song_str)
    return get_song_uri_list(round_songs)


# def init_song_points(song_dict: dict[str, list[str]]):
#     song_points: dict[str, int] = {}
#     for key in song_dict:
#         song_list: list[str] = song_dict[key]
#         for song in song_list:
#             if song not in song_points.keys():
#                 song_points[song] = 1
    
  
def get_song_uri_list(names: list[str]):
    uri_list: list[str] = []
    print(names)
    for item in names:
        print(item)
        raw_search_result = spotify.search(q = str(item), limit=1, type='track')
        song_uri_single: str = raw_search_result['tracks']['items'][0]['uri']
        uri_list.append(song_uri_single)
    return uri_list

def start_current_device_playback(songs: list[str]):
    spotify.start_playback(uris = songs)

