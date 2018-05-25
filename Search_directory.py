import os
import json


def search_directory(search_dir):
    music_list = []

    # search in given directory
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            # list of file types
            if file.endswith(".mp3") or file.endswith(".m4a"):
                music_list.append({'address': root, 'name': file})

    return music_list

