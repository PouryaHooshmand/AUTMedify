import eyed3

audiofile = eyed3.load("/mnt/Data/Multimedia/Music/Femme Fatale (Spotify Playlist) (MP3 320Kbps) - (7tunes)/Femme Fatale (Spotify Playlist) (MP3 320Kbps) - (7tunes)/11 - Lorde - Bravado.mp3")

# audiofile.tag.artist = u"LORDE_KABIR"
# audiofile.tag.save()

print(audiofile.tag.lyrics)

"""
audiofile.tag.artist = u"Integrity"
audiofile.tag.album = u"Humanity Is The Devil"
audiofile.tag.album_artist = u"Integrity"
audiofile.tag.title = u"Hollow"
audiofile.tag.track_num = 2
"""