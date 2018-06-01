import swagger_client as LyricAPI

from swagger_client.rest import ApiException

LyricAPI.configuration.api_key['apikey'] = 'd58b51bad4512088ae210ba3f06c2909'


def findLyrics(title, artist):
    api_instance = LyricAPI.LyricsApi()

    Lyric_obj = api_instance.matcher_lyrics_get_get(q_track=title, q_artist=artist, format='json')

    Lyric = Lyric_obj.message.body.lyrics.lyrics_body

    return Lyric
