from google_images_download import google_images_download


def get_cover(album, artist):
    response = google_images_download.googleimagesdownload()
    args = {"keywords": album + " " + artist, "limit": 1, "print_urls": True, "specific_site": "wikipedia.org"}
    print(response.download(args))