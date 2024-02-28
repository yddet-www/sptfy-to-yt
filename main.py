import os
from SpotAPI import *
from YtAPI import *
from PlaylistQ import *
from datetime import datetime, date, time, timedelta

# Track the YT API limits
reset_time = None
quota = None

# Appened input onto queue text file
def append_to_file(line):
    file = open("queue.txt", "a", encoding="utf-8")
    file.write(line + "\n")
    file.close()
    
# Return a list of all lines in the queue text file
def read_lines():
    file = open("queue.txt", "r", encoding="utf-8")
    return file.readlines()   

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

    # yt_set_credentials()
    # new_playlist_id = create_playlist()

    

        # video_id = search_video(key_word)
        
        # print(f"{key_word} {video_id}")
        # insert_vid_to_playlist(playlist_id=new_playlist_id, video_id=video_id)


# TESTING PURPOSES
def test():
    track_list = [s.strip() for s in read_lines()]
    sptfy = "0Gc1CHlpYK0KuGrt8nPK2V"
    yt = "PL4kxuDsb-ujr231Wim7vsAvOeZVxSGWLk"
    playlist = Playlist(src_playlist=sptfy, trgt_playlist=yt, lst=track_list)
    
    today = datetime.now()
    reset = None
    
    if(reset == None):
        reset = datetime.combine(today.date(), time(2, 0, 0)) + timedelta(days=1)
    
    print(today)
    print(reset)
    print(today > reset)
    
    
def run_v2():
    # First line of text file strictly for quota info
    
    # with open("queue.txt", "r+") as txt:
    #     quota_data = txt.readline().split(";")
    
    txt = open("queue.txt", "r+") # DONT FORGET TO CLOSE
    quota_data = txt.readline().split(";")
    
    quota = quota_data[0]
    reset_time = datetime.fromisoformat(quota_data[1].strip("\n"))
    today = datetime.now()
    
    # Reset quota count every 02:00 AM CST
    if(today > reset_time):
        quota = 50
        reset_time = datetime.combine(today.date(), time(2, 0, 0)) + timedelta(days=1)
        
    start_p = txt.tell() # pointer to 2nd line
    
    if(not txt.readline().strip()):
        print("WEH KOSONG")
        
        playlist_url = "https://open.spotify.com/playlist/0Gc1CHlpYK0KuGrt8nPK2V?si=a4bc2dc9a7d7469f"
        
        tracks = []
        src_ID = get_playlist_ID(playlist_url)
        
        for index, track in enumerate(get_playlist(playlist_url)):
            title = track["title"]
            artists = " ".join(track["artists"])
    
            key_word = f"{title} {artists}"
            tracks.append(key_word)
            
        print(tracks)
    else:
        print("WADUH ISI")
        txt.seek(start_p) # reposition pointer to 2nd line
        
        queue = txt.readlines()
        print(queue)   
        print(len(queue))    
    
    txt.close()

if __name__ == "__main__":
    # run()
    # test()
    run_v2()