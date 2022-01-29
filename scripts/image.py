import os, copy
from PIL import Image

class ImageModifier:
    @staticmethod
    def image_resizer(path, *sizes):
        img = Image.open(path)

        for size in sizes:
            size_img = copy.copy(img)
            splitted_path = os.path.split(path)[1]
            img_resized = size_img.resize((int(size_img.width * size), int(size_img.height * size)), Image.LANCZOS)
            img_resized.save("{}/{}_x{}{}".format(os.path.dirname(path), os.path.splitext(splitted_path)[0], size, os.path.splitext(splitted_path)[1]))