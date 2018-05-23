import os
import json


def find_musics(search_dir):
    music_list = []

    # search in given directory
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            # list of file types
            if file.endswith(".mp3") or file.endswith(".m4a"):
                music_list.append({'address': root, 'name': file})
    # write results to file
    with open('musicaddress.json', 'w') as outfile:
        json.dump(music_list, outfile)


# test function
directory = "E:\Downloads"
find_musics(directory)
