import os

class Playlist:

    def __init__(self, src_playlist, trgt_playlist, lst: list):
        self.src_playlist = src_playlist # spotify playlist
        self.trgt_playlist = trgt_playlist # youtube playlsit
        self.trackList = lst
        
    def get_src(self):
        return self.src_playlist
    
    def get_trgt(self):
        return self.trgt_playlist
    
    def tracks_list(self):
        return self.trackList
    
    def tracks_num(self):
        return len(self.trackList)