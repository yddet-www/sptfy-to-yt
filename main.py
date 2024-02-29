import os
from SpotAPI import *
from YtAPI import *
from PlaylistQ import *
from datetime import datetime, date, time, timedelta

# Track the YT API limits
reset_time = None
quota = None
queue = []

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
        track_list = get_playlist(get_playlist_ID("https://open.spotify.com/playlist/0Gc1CHlpYK0KuGrt8nPK2V?si=a4bc2dc9a7d7469f"))
        
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
    track_list = []
    sptfy = "0Gc1CHlpYK0KuGrt8nPK2V"
    yt = "PL4kxuDsb-ujr231Wim7vsAvOeZVxSGWLk"
                
    for index, track in enumerate(get_playlist(sptfy)):
        title = track["title"]
        artists = " ".join(track["artists"])
    
        key_word = f"{title} {artists}"
        track_list.append(key_word)
                
    playlist = Playlist(sptfy, yt, track_list)
    print(playlist.print())
    
    
    
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
        print("Antrian mu kosong.")
        
    else:
        print("Antrian mu ada isi.")
        txt.seek(start_p) # reposition pointer to 2nd line
        saved = txt.readlines()
        print(saved)
        print(len(saved))
    
    txt.close()
        
    app_flag = True
    
    while(app_flag):          
        menu = """
==============================
Choose the following options:
1) Add to queue
2) Process queue
3) Check queue
4) Remove from queue
5) Check quota left
6) Check next reset
7) Exit
"""
        response = input(menu)
        
        match response:
            case "1":
                url = input("Enter your Spotify playlist link:\n")
                
                src = get_playlist_ID(url)
                tracks = []
                trgt = "PL4kxuDsb-ujr231Wim7vsAvOeZVxSGWLk" # later change to create_playlist()
                
                for index, track in enumerate(get_playlist(src)):
                    title = track["title"]
                    artists = " ".join(track["artists"])
    
                    key_word = f"{title} {artists}"
                    tracks.append(key_word)
                
                playlist = Playlist(src, trgt, tracks)
                queue.append(playlist)
                
            case "2":
                print("You chose option 2")
                
            case "3":
                queue_index = len(queue)
                print(f"You have {queue_index} items in queue")
                
                if(queue_index > 1):
                    index = input(f"Which item (1 - {queue_index}) would you like to inspect? (enter E to exit)\n")
                    if(index.isdigit() and int(index) > 0 and int(index) <= queue_index):
                        print(queue[int(index) - 1].print())
                
                elif(queue_index == 1):
                    index = input(f"Would you like to inspect the entry? (Y/N)\n")
                    if(index == "Y" or index == "y"):
                        print(queue[0].print())
                
                else:
                    print("Your queue is empty. Please add a new entry before checking.")
            
            case "4":
                print("You chose option 4")
                
            case "5":
                print(f"You can transfer {quota} songs")
                
            case "6":
                print(f"Next quota reset is at {reset_time}")
                
            case default:
                app_flag = False # end session


if __name__ == "__main__":
    # run()
    # test()
    run_v2()