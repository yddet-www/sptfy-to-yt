import os
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv


load_dotenv()
credentials = None
api_key = os.getenv("YT_API_KEY")


# Getting the OAuth credentials, call this at the top of the code
def yt_set_credentials():
    global credentials
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json", scopes=["https://www.googleapis.com/auth/youtube"]
    )
        
    flow.run_local_server(port=8080, prompt="consent")
    credentials = flow.credentials    


# Creating a playlist for user YT account and returns it's ID
def create_playlist(playlist_title="Made by yddet"):
    youtube = build("youtube", "v3", credentials=credentials)
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": playlist_title,  # Maybe change this to match the Spotify playlist name
                "description": "Converted playlist from Spotify to Youtube."
            },
            "status": {
                "privacyStatus": "public"
            }
        }
    )

    response = request.execute()
    return response["id"]


# Searching videos by keyword and returns the first result's video ID
def search_video(keyword):
    youtube = build("youtube", "v3", credentials=credentials)
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=keyword
    )
    
    response = request.execute()
    return response["items"][0]["id"]["videoId"]


# Insert video into playlist by their IDs
def insert_vid_to_playlist(playlist_id, video_id):
    youtube = build("youtube", "v3", credentials=credentials)

    request = youtube.playlistItems().insert(
        part="snippet,id",
        body={
          "snippet": {
            "playlistId": playlist_id,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": video_id
            }
          }
        }
    )
    
    response = request.execute()