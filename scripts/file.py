if __name__ != "__main__":
    class FlaskFileReader:
        def __init__(self, template_folder="templates"):
            self.temp_path = template_folder

        def readFile(self, path):
            return open(path, 'rb').read()

        def readWeb(self, path):
            return open("{}/{}".format(self.temp_path, path), 'rb').read()