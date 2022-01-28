class MIMEType:
    default_mimetype = 'text/plain'
    mimetypes = {
        'js': 'application/javascript',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif',
        'css': 'text/css',
    }

    @classmethod
    def get_mimetype(cls, file):
        extension = file.split('.')[-1]
        if extension.count("/"):
            return cls.default_mimetype
        else:
            return cls.mimetypes.get(extension, cls.default_mimetype)