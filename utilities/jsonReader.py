from ddt import ddt,data,file_data, unpack
import json

class ReadFromJSON():

    def get_json_data(filepath):
        return json.load(open(filepath))