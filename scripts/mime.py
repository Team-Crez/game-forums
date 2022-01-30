import json

class MIMEType:
    default_mimetype = 'text/plain'
    mimetypes = json.load(open("./resources/mimetypes.json", "r"))

    @classmethod
    def get_mimetype(cls, file):
        extension = file.split('.')[-1]
        if extension.count("/"):
            return cls.default_mimetype
        else:
            return cls.mimetypes.get(extension, cls.default_mimetype)