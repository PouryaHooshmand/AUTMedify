from google_images_download import google_images_download

from Logger import Logger
from Music_metadata import MusicMetadata


def get_cover(track_address):
    track_data = MusicMetadata(track_address)
    track_metadata = track_data.metadata()
    album = track_metadata['album']
    artist = track_metadata['artist']

    log = Logger().log

    log('info', 'Downloading ' + album + " " + artist + " cover")
    response = google_images_download.googleimagesdownload()

    args = {"keywords": album + " " + artist, "limit": 1, "print_urls": True, "specific_site": "wikipedia.org"}
    try:
        result = response.download(args)

    except:
        log('error', 'Unknown error happened while downloading ' + str(album) + " " + str(artist) + " cover")
        return 0

    log('info', 'Download ' + str(album) + " " + str(artist) + " cover COMPLETED")

    cover = result[args["keywords"]][0]

    track_data.metadata_setter({'cover': cover})

    return True