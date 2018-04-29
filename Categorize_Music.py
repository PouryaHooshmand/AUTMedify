import json
import os
import shutil

from Music_metadata import MusicMetadata
from Logger import Logger

class CategorizeMusic:

    def __init__(self, music_list):
        """
        :param music_list: get Music List
        """

        self.music_list = music_list
        self.logger = Logger.log

        # Loading Necessary Information from Config File
        with open("/home/milad/College/Medify/config/config.json") as config_file:
            config_data = json.load(config_file)
            self.music_location = config_data['music']['location']

    def move_files(self):

        for music_file in self.music_list:

            metadata = MusicMetadata(music_file['address']).metadata  # Get Metadata
            file_dst = self.music_location + metadata['artist'] + '/' + metadata['album']

            # Create directories and move file
            if not os.path.exists(file_dst):
                os.makedirs(file_dst)
                self.logger('info', 'directory not found!\nCreating directory: ' + file_dst)

            try:
                shutil.move(src=music_file['address'], dst=file_dst)
            except shutil.Error as shutil_error:
                self.logger('error', "File can't be moved\n" + str(shutil_error))
            except IOError as io_error:
                self.logger('error', str(io_error))
            except:
                self.logger('error', 'Unknown Error')
