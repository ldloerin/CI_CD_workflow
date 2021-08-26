import json
import os


class ReadJsonFile(object):
    @staticmethod
    def is_json_path_valid(json_path):
        is_valid = os.path.exists(json_path)
        is_valid &= os.path.isfile(json_path)
        return is_valid

    @staticmethod
    def load(json_path, key=""):
        if ReadJsonFile.is_json_path_valid(json_path):
            try:
                with open(json_path, "r") as json_path:
                    inputs = json.load(json_path)
                    if key == "":
                        return inputs
                    elif key in inputs:
                        return inputs[key]
                    else:
                        print('No key in configuration file')
                        return {}
            except:
                print('Check configuration file for formatting errors')
                return {}
        else:
            print('Could not open configuration file')
            return {}
