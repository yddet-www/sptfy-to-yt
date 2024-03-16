from SpotAPI import *
from YtAPI import *
from PlaylistQ import *
from datetime import datetime, time, timedelta

class _EarlyBreak(Exception): pass

# Global variables
reset_time = None
quota = 0        # Limit of how many tracks that can be processed
queue = []


def process_q(playlist_obj, index): 
    global quota, queue
    
    track_list = playlist_obj.get_tracks()
    yt_playlist = playlist_obj.get_trgt()
    
    while track_list and quota:
        vid_id = search_video(track_list.pop(0))
        insert_vid_to_playlist(yt_playlist, vid_id)
        quota -= 1
    
    if not track_list:
        del queue[index]    # checks whether all tracks are processed
                            # if yes, remove object from queue
    
    
def run():
    global reset_time, quota, queue
    yt_set_credentials()
    
    with open("queue.txt", "r", encoding="utf-8") as txt:               # UTF-8 is important btw
        session = [i.strip("\n").split(";") for i in txt.readlines()]   # Holds a list of lists
                                                                        # 1st index contains the quota data in form [quota, date]
                                                                        # the rest are saved playlist object arguments in form [src, trgt, ... tracks]
    
    quota_data = session[0]
    quota = int(quota_data[0])
    reset_time = datetime.fromisoformat(quota_data[1])
    today = datetime.now()
    
    if(today > reset_time): # Reseting quota counter
        quota = 50
        reset_time = datetime.combine(today.date(), time(2, 0, 0)) + timedelta(days=1)
        
    if(len(session) == 1):
        print("Your queue is empty.")
    else:
        print(f"You have {len(session) - 1} items in your queue.")
        
        for i in range(1, len(session)):
            src = session[i].pop(0)
            trgt = session[i].pop(0)
            playlist = Playlist(src, trgt, session[i])
            queue.append(playlist)
        
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
        
        try:
            match response:
                case "1":
                    url = input("Enter your Spotify playlist link:\n")
                    
                    src = get_playlist_ID(url)                
                    if(src == -1):
                        print("Invalid playlist link")
                        raise _EarlyBreak()
                    
                    if(not get_playlist(src)):
                        print("Playlist is private")
                        raise _EarlyBreak()
                    
                    # trgt = create_playlist()
                    tracks = []
                    
                    for index, track in enumerate(get_playlist(src)):
                        title = track["title"]
                        artists = " ".join(track["artists"])
        
                        key_word = f"{title} {artists}"
                        tracks.append(key_word)
                    
                    playlist = Playlist(src, trgt, tracks)
                    queue.append(playlist)
                    
                case "2":
                    queue_index = len(queue)
                    print(f"You have {queue_index} items in queue")
                    
                    if(quota == 0):
                        print(f"You have run out of quota. Please check back at {reset_time}")    
                    
                    elif(queue_index > 1):
                        index = input(f"Which item (1 - {queue_index}) would you like to process? (enter E to exit)\n")
                        if(index.isdigit() and int(index) > 0 and int(index) <= queue_index):
                            process_q(queue[int(index) - 1], int(index) - 1)
                            
                    
                    elif(queue_index == 1):
                        index = input(f"Would you like to process the entry? (Y/N)\n")
                        if(index == "Y" or index == "y"):
                            process_q(queue[0], 0)
                    
                    else:
                        print("Your queue is empty. Please add a new entry before processing.")
                    
                case "3":
                    queue_index = len(queue)
                    print(f"You have {queue_index} items in queue")
                    
                    if(queue_index > 1):
                        index = input(f"Which item (1 - {queue_index}) would you like to inspect? (enter E to exit)\n")
                        if(index.isdigit() and int(index) > 0 and int(index) <= queue_index):
                            print(queue[int(index) - 1].toString())
                    
                    elif(queue_index == 1):
                        index = input(f"Would you like to inspect the entry? (Y/N)\n")
                        if(index == "Y" or index == "y"):
                            print(queue[0].toString())
                    
                    else:
                        print("Your queue is empty. Please add a new entry before checking.")
                
                case "4":
                    queue_index = len(queue)
                    print(f"You have {queue_index} items in queue")
                    
                    if(queue_index > 1):
                        index = input(f"Which item (1 - {queue_index}) would you like to delete? (enter E to exit)\n")
                        if(index.isdigit() and int(index) > 0 and int(index) <= queue_index):
                            del queue[int(index) - 1]
                            print("Entry has been deleted")
                    
                    elif(queue_index == 1):
                        index = input(f"Would you like to delete the entry? (Y/N)\n")
                        if(index == "Y" or index == "y"):
                            del queue[0]
                            print("Entry has been deleted")
                    
                    else:
                        print("Your queue is empty. Need an existing entry before deleting.")
                    
                case "5":
                    print(f"You can transfer {quota} songs")
                    
                case "6":
                    print(f"Next quota reset is at {reset_time}")
                    
                case default:
                    app_flag = False # end session
        except _EarlyBreak:
            pass
        
    # SAVE SESSION
    with open("queue.txt", "w", encoding="utf-8") as txt: # UTF-8 is important btw
        new_quota = f"{quota};{reset_time}\n"
        session = [new_quota]
        
        while queue:
            session.append(queue.pop(0).toString() + "\n")
            
        txt.writelines(session)
    

if __name__ == "__main__":
    run()
    # test()