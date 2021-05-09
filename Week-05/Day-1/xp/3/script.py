class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        lyrics = []
        lyrics.append("There’s a lady who's sure")
        lyrics.append("all that glitters is gold")
        lyrics.append("and she’s buying a stairway to heaven")

    def __str__(self):
        return '/'.join(self.lyrics)

starway = Song.sing_me_a_song()