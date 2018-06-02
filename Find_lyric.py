import swagger_client as LyricAPI


from Music_metadata import MusicMetadata

LyricAPI.configuration.api_key['apikey'] = 'd58b51bad4512088ae210ba3f06c2909'


def findLyrics(track_location):
    api_instance = LyricAPI.LyricsApi()

    track = MusicMetadata(track_location)

    track_metadata = track.metadata()

    title = track_metadata['title']
    artist = track_metadata['artist']

    Lyric_obj = api_instance.matcher_lyrics_get_get(q_track=title, q_artist=artist, format='json')

    Lyric = Lyric_obj.message.body.lyrics.lyrics_body

    track.metadata_setter({'lyric': Lyric})

    return 1
