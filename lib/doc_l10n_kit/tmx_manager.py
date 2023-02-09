import os
import xml.etree.ElementTree as ET
import json

class TmxManager:

    __base_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    __tmx_file_path = "l10n/tmx/quarkus.tmx"

    def __init__(self):
        __config_file_name = "{}/config/l10n-kit.json".format(self.__base_dir)
        with open(__config_file_name) as file:
            __config = json.load(file)
            self.__tmx_file_path = __config["tmx"]["filePath"]


    def sort(self):

        dom = ET.parse(self.__tmx_file_path)
        body = dom.getroot().find('body')

        body[:] = sorted(body, key=lambda tu: tu.find('tuv/seg').text)
        dom.write(self.__tmx_file_path, encoding="UTF-8")
