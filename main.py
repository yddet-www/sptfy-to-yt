import os
from SpotAPI import *
from YtAPI import *
from Enqueue import *

def run():
    # YOUTUBE QUOTA LIMIT RUINING EVERYTHING, SO WE MAKING A QUEUE
    if(os.stat("queue.txt").st_size == 0):
        print("is empty")
        # playlist_url = input("Enter your spotify playlist's URL: ")
        track_list = get_playlist("https://open.spotify.com/playlist/0Gc1CHlpYK0KuGrt8nPK2V?si=a4bc2dc9a7d7469f")
        
        for index, track in enumerate(track_list):
            title = track["title"]
            artists = " ".join(track["artists"])
    
            key_word = f"{title} {artists}"
        
            append_to_file(key_word)
    else:
        print("isnt empty")
    
    print(read_lines())
    
    
    
    
    
    # yt_set_credentials()
    # new_playlist_id = create_playlist()

    
    
        # video_id = search_video(key_word)
        
        # print(f"{key_word} {video_id}")
        # insert_vid_to_playlist(playlist_id=new_playlist_id, video_id=video_id)
    
if __name__ == '__main__':
    run()