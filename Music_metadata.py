import eyed3


class MusicMetadata:

    def __init__(self, music_address):
        """
        :param music_address: Music File address
        """

        self.audiofile = eyed3.load(music_address)

    @property
    def metadata(self):
        return {'album': self.audiofile.tag.album,
                'album_artist': self.audiofile.tag.album_artist,
                'album_type': self.audiofile.tag.album_type,
                'artist': self.audiofile.tag.artist,
                'artist_origin': self.audiofile.tag.artist_origin,
                'artist_url': self.audiofile.tag.artist_url,
                'audio_file_url': self.audiofile.tag.audio_file_url,
                'audio_source_url': self.audiofile.tag.audio_source_url,
                'bpm': self.audiofile.tag.bpm,
                'cd_id': self.audiofile.tag.cd_id,
                'chapters': self.audiofile.tag.chapters,
                'comments': self.audiofile.tag.comments,
                'copyright_url': self.audiofile.tag.copyright_url,
                'disc_num': self.audiofile.tag.disc_num,
                'genre': self.audiofile.tag.genre,
                'images': self.audiofile.tag.images,
                'publisher': self.audiofile.tag.publisher,
                'release_date': self.audiofile.tag.release_date,
                'title': self.audiofile.tag.title,
                'track_num': self.audiofile.tag.track_num
                }

    @metadata.setter
    def metadata(self, data):

        try:
            self.audiofile.tag.album = data['album']
        except:
            pass

        try:
            self.audiofile.tag.album_artist = data['album_artist']
        except:
            pass

        try:
            self.audiofile.tag.album_type = data['album_type']
        except:
            pass

        try:
            self.audiofile.tag.artist = data['artist']
        except:
            pass

        try:
            self.audiofile.tag.artist_origin = data['artist_origin']
        except:
            pass

        try:
            self.audiofile.tag.artist_url = data['artist_url']
        except:
            pass

        try:
            self.audiofile.tag.audio_file_url = data['audio_file_url']
        except:
            pass

        try:
            self.audiofile.tag.audio_source_url = data['audio_source_url']
        except:
            pass

        try:
            self.audiofile.tag.bpm = data['bpm']
        except:
            pass

        try:
            self.audiofile.tag.cd_id = data['cd_id']
        except:
            pass

        try:
            self.audiofile.tag.chapters = data['chapters']
        except:
            pass

        try:
            self.audiofile.tag.comments = data['comments']
        except:
            pass

        try:
            self.audiofile.tag.copyright_url = data['copyright_url']
        except:
            pass

        try:
            self.audiofile.tag.disc_num = data['disc_num']
        except:
            pass

        try:
            self.audiofile.tag.genre = data['genre']
        except:
            pass

        try:
            self.audiofile.tag.images = data['images']
        except:
            pass

        try:
            self.audiofile.tag.publisher = data['publisher']
        except:
            pass

        try:
            self.audiofile.tag.release_date = data['release_date']
        except:
            pass

        try:
            self.audiofile.tag.title = data['title']
        except:
            pass

        try:
            self.audiofile.tag.track_num = data['track_num']
        except:
            pass

        self.audiofile.tag.save()

        return True

    def rename(self):
        new_name = self.audiofile.tag.track_num + ". " + self.audiofile.tag.title

        try:
            self.audiofile.rename(new_name)
            return True
        except:
            return False

        