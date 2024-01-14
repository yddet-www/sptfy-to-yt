import requests
import base64
import os
from dotenv import load_dotenv

# Getting client ID and client secret from .env file
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# The Spotify token URL
token_url = "https://accounts.spotify.com/api/token"

client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

headers = {
    "Authorization": f"Basic {client_creds_b64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials"
}

def getToken():
    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code == 200:
    # Extract the access token from the response
        access_token = response.json()["access_token"]
        return access_token
    else:
        print("Failed to get access token:", response.status_code, response.text)

def clientCreds():
    print("client_id: " + client_id)
    print("client_secret: " + client_secret)
    
def get_playlist_ID(url):
    if(url.find("https://open.spotify.com/playlist/") == -1 ): # if the URL is not legal, return -1
        return -1
    else:
        playlist_id = url[34:56] # pulls the 22 length ID from the playlist URL
        return playlist_id
    
def get_playlist(url):
    playlist_id = get_playlist_ID(url)
    tracks_list = []
    
    if(playlist_id == -1):
        return "Invalid playlist link"
    
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    
    headers = {
        "Authorization": f"Bearer {getToken()}"
    }
    
    while playlist_url:
        response = requests.get(playlist_url, headers=headers)
        
        if(response.status_code == 200):
            tracks = response.json()["items"]
            track_names = [track["track"]["name"] for track in tracks]
            tracks_list.extend(track_names)
            playlist_url = response.json()["next"]
        else:
            print("Failed to get playlist tracks:", response.status_code, response.text)
            return None
    
    return tracks_list
    
    