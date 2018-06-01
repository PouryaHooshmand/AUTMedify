from google_images_download import google_images_download
from Logger import Logger
from Music_metadata import MusicMetadata



def get_cover(address):
    log = Logger().log
    MD = MusicMetadata(address).metadata()
    album = MD["album"]
    artist = MD["artist"]

    log('info', 'Downloading ' + album + " " + artist + " cover")

    response = google_images_download.googleimagesdownload()

    args = {"keywords": album + " " + artist, "limit": 1, "print_urls": True, "specific_site": "wikipedia.org"}
    try:
        result = response.download(args)
    except:
        log('error', 'Unknown error happened while downloading ' + str(album) + " " + str(artist) + " cover")
        return 0

    log('info', 'Download ' + str(album) + " " + str(artist) + " cover COMPLETED")

    return result[args["keywords"]][0]