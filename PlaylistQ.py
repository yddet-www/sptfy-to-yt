import os

class Playlist:

    def __init__(self, src_playlist, trgt_playlist, lst):
        self.src_playlist = src_playlist # spotify playlist
        self.trgt_playlist = trgt_playlist # youtube playlsit
        self.tracks = lst

    def get_src(self):
        return self.src_playlist
    
    def get_trgt(self):
        return self.trgt_playlist
    
    def set_tracks(self, lst):
        self.tracks = lst
    
    def get_tracks(self):
        return self.tracks
    
    def tracks_num(self):
        return len(self.tracks)