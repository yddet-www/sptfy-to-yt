from SpotAPI import *

def run():
    playlist_url = input("Insert spotify playlist link:")
    print(get_playlist(playlist_url))
    
if __name__ == '__main__':
    run()