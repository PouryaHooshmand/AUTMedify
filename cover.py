import eyed3
from google_images_download import google_images_download
import os


def fix_cover(address, album, artist):
    # check if cover was downloaded
    if not os.path.exists(os.getcwd() + "\\downloads\\" + album + " " + artist):
        response = google_images_download.googleimagesdownload()
        # search album name + artist name in wikipedia
        args = {"keywords": album + " " + artist, "limit": 1, "print_urls": True, "specific_site": "wikipedia.org"}
        response.download(args)
        # return directory of cover art
    dir = os.getcwd() + "\\downloads\\" + album + " " + artist
    os.chdir(dir)
    file = [f for f in os.listdir('.') if os.path.isfile(f)][0]
    cover = dir + "\\" + file
    audiofile = eyed3.load(address)

    audiofile.tag.images.set(3, open(cover, 'rb').read(), 'image/jpeg')

    audiofile.tag.save()


# test
fix_cover("E:\\Music\\cold.mp3","wrong side of heaven", "five finger death punch")
