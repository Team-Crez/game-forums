import re

from PIL import Image

from rjsmin import jsmin
from scripts.mime import MIMEType

if __name__ != "__main__":
    class FlaskFileReader:
        def __init__(self, template_folder="templates"):
            self.minify_regex = re.compile(r"^.+\.min\.js$")
            self.temp_path = template_folder

        def readFile(self, path):
            return open(path, 'rb').read()

        def readWeb(self, path):
            return open("{}/{}".format(self.temp_path, path), 'rb').read()

        def readWebText(self, path, **kwargs):
            text = open("{}/{}".format(self.temp_path, path), 'r', encoding='utf-8').read()
            for key, value in kwargs.items():
                re.sub(r"\\[\\[\\[ *{} *\\]\\]\\]".format(key), value, text)

            return text

        def readMinWeb(self, path, **kwargs):
            # open("{}/{}".format(self.temp_path, path), 'rb').read()
            return jsmin(self.readWebText(path)) if MIMEType.get_mimetype("{}/{}".format(self.temp_path, path)) == 'application/javascript' and (not self.minify_regex.match(path)) else self.readWeb(path)
            
        def loadImg(self, path):
            return Image.open("{}/{}".format(self.temp_path, path))