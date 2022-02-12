import json

class MIMEType:
    default_mimetype = 'text/plain'
    mimetypes = json.load(open("./resources/mimetypes.json", "r"))
    image_mimes = ["image/webp", "image/jpeg", "image/png", "image/gif"]

    @classmethod
    def get_mimetype(cls, file):
        extension = file.split('.')[-1]
        if extension.count("/"):
            return cls.default_mimetype
        else:
            return cls.mimetypes.get(extension, cls.default_mimetype)

    @classmethod
    def is_image(cls, file):
        extension = file.split('.')[-1]
        if extension.count("/"):
            return False
        else:
            if cls.mimetypes.get(extension, cls.default_mimetype) in cls.image_mimes:
                return True
            else: return False