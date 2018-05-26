import json

from acrcloud.recognizer import ACRCloudRecognizer

from Dictionary_Difference import DictDiffer
from Logger import Logger
from Music_metadata import MusicMetadata


class Recognizer:

    def __init__(self):

        self.log = Logger().log

        # Loading Necessary Information from Config File
        with open("./config/config.json") as config_file:
            config_data = json.load(config_file)
            self.ACRCloud_config = {"region": config_data["ACRCloud"]["region"].encode('utf8'),
                                    "host": config_data["ACRCloud"]["host"].encode('utf8'),
                                    "access_key": config_data["ACRCloud"]["access_key"].encode('utf8'),
                                    "access_secret": config_data["ACRCloud"]["access_secret"].encode('utf8'),
                                    "timeout": config_data["ACRCloud"]["timeout"]}

        self.log('info', 'initializing connection to ACR-Cloud service')
        self.acrcloud = ACRCloudRecognizer(self.ACRCloud_config)

    def recognize(self, track_location):
        """
        :param track_location: Track Location
        :return: (True, False) after recognition and editing the track
        """

        metainfo = self.get_metainfo(track_location)

        if metainfo["status"] != "Success":
            self.log('error', track_location + ' metadata not found')
            return False

        self.edit_metadata(track_location, metainfo)
        self.log('info', track_location + ' recognized!\tACR-Cloud results:\n' + str(metainfo))
        return True

    def edit_metadata(self, track_location, new_metadata):
        # TODO: CHECK THE FUCKKING TEST.PY
        # FUUUUUUUUUUCK THIS SHIT.
        # CHECK THE FUCKING STRING
        # CHECK THE FUCKING Genre OBJEECT
        # FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK

        track_data = MusicMetadata(track_location)
        track_metadata = track_data.metadata()
        del track_metadata['Genre']
        metadata_diff = DictDiffer(new_metadata, track_data.metadata())
        track_data.metadata_setter(metadata_diff.changed())  # Edit Changed Values
        track_data.metadata_setter(metadata_diff.added())  # Add New Values

    def get_metainfo(self, track_location):

        metainfo = self.get_acrcloud_metainfo(track_location)

        if metainfo["status"]["code"] == 3000:
            self.log('error', 'Unknown Error happend for track : ' + track_location + '\nACR-Cloud results:\n' + str(metainfo))
            return metainfo

        else:
            return {"album": metainfo["metadata"]["music"][0]["album"]["name"],
                    "album_artist": metainfo["metadata"]["music"][0]["artists"][0]["name"],
                    "artist": metainfo["metadata"]["music"][0]["artists"][0]["name"],
                    "genre": metainfo["metadata"]["music"][0]["genres"][0]["name"],
                    "publisher": metainfo["metadata"]["music"][0]["label"],
                    "release_date": metainfo["metadata"]["music"][0]["release_date"],
                    "title": metainfo["metadata"]["music"][0]["title"],
                    "status": metainfo["status"]["msg"]
                    }

    def get_acrcloud_metainfo(self, track_location):
        self.log('info', 'requesting from ACR-Cloud: ' + track_location)
        return json.loads(self.acrcloud.recognize_by_file(track_location, 20))
