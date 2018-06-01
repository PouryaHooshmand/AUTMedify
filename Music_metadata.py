import eyed3

__version__ = 0.1


class MusicMetadata:

    def __init__(self, music_address):
        """
        :param music_address: Music File address
        """
        self.music_address = music_address
        self.audiofile = eyed3.load(self.music_address)

    def metadata(self):
        return {'album': self.audiofile.tag.album,
                'album_artist': self.audiofile.tag.album_artist,
                'artist': self.audiofile.tag.artist,
                'genre': str(self.audiofile.tag.genre),
                'title': self.audiofile.tag.title,
                'track_num': self.audiofile.tag.track_num
                }

    def metadata_setter(self, data):

        try:
            self.audiofile.album = data['album'].decode('utf-8')
        except:
            pass

        try:
            self.audiofile.album_artist = data['album_artist'].decode('utf-8')
        except:
            pass

        try:
            self.audiofile.artist = data['artist'].decode('utf-8')
        except:
            pass

        try:
            self.audiofile.genre = data['genre'].decode('utf-8')
        except:
            pass

        try:
            self.audiofile.picture = data['image']
        except:
            pass

        try:
            self.audiofile.title = data['title'].decode('utf-8')
        except:
            pass

        try:
            self.audiofile.track = data['track_num'].decode('utf-8')
        except:
            pass

        try:
            if data['lyric']:
                track = eyed3.load(self.music_address)
                track.tag.lyrics.set(data['lyric'].decode('utf-8'))
                track.tag.save()
        except:
            pass

        self.audiofile.tag.save()

        return True
