import eyed3

import stagger

__version__ = 0.1


class MusicMetadata:

    def __init__(self, music_address):
        """
        :param music_address: Music File address
        """
        self.music_address = music_address
        self.musicfile = stagger.read_tag(music_address)

    def metadata(self):
        return {'album': self.musicfile.album,
                'album_artist': self.musicfile.album_artist,
                'artist': self.musicfile.artist,
                'disc_num': self.musicfile.disc,
                'genre': self.musicfile.genre,
                'release_date': self.musicfile.date,
                'title': self.musicfile.title,
                'track_num': self.musicfile.track
                }

    def metadata_setter(self, data):

        try:
            self.musicfile.album = data['album'].decode('utf-8')
        except:
            pass

        try:
            self.musicfile.album_artist = data['album_artist'].decode('utf-8')
        except:
            pass

        try:
            self.musicfile.artist = data['artist'].decode('utf-8')
        except:
            pass

        try:
            self.musicfile.disc = data['disc_num'].decode('utf-8')
        except:
            pass

        try:
            self.musicfile.genre = data['genre'].decode('utf-8')
        except:
            pass

        try:
            self.musicfile.picture = data['image']
        except:
            pass

        try:
            self.musicfile.date = data['release_date'].decode('utf-8')
        except:
            pass

        try:
            self.musicfile.title = data['title'].decode('utf-8')
        except:
            pass

        try:
            self.musicfile.track = data['track_num'].decode('utf-8')
        except:
            pass

        try:
            if data['lyric']:
                track = eyed3.load(self.music_address)
                track.tag.lyrics.set(data['lyric'].decode('utf-8'))
                track.tag.save()
        except:
            pass

        self.musicfile.write()

        return True
