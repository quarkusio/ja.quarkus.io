import os
import xml.etree.ElementTree as ET

class TmxManager:

    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

    def sort(self):
        tmx_file_path = os.path.join(self.base_dir, './l10n/tmx/quarkus.tmx')

        dom = ET.parse(tmx_file_path)
        body = dom.getroot().find('body')

        body[:] = sorted(body, key=lambda tu: tu.find('tuv/seg').text)
        dom.write(tmx_file_path, encoding="UTF-8")
