from SpotAPI import *
from YtAPI import *

def run():
    url = input("Insert playlist link:")
    print(get_playlist(url))
    
if __name__ == '__main__':
    run()