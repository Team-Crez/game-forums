import os, copy
import numpy as np
from PIL import Image

class ImageModifier:
    @staticmethod
    def image_resizer(paths, sizes):
        img_paths = {}
        img_path_list = []

        for path in paths:
            img = Image.open(path)
            img_names = [path]

            for size in sizes:
                size_img = copy.copy(img)
                splitted_path = os.path.split(path)[1]
                splitted_path_text = os.path.splitext(splitted_path)
                img_resized = ImageModifier.resize_image(size_img, size)
                img_name = "{}/{}_x{}{}".format(os.path.dirname(path), splitted_path_text[0], size, splitted_path_text[1])
                img_resized.save(img_name)

                img_names.append(img_name)

            [img_path_list.append(img_name) for img_name in img_names]

            img_paths[path] = img_names
            
        return img_paths, img_path_list

    @staticmethod
    def image_changer(paths, extension, image_type = None, **kwargs):
        if not image_type: image_type = extension
        
        img_paths = {}
        img_path_list = []

        for path in paths:
            img = Image.open(path)
            splitted_path = os.path.split(path)[1]
            img_name = '{}/{}.{}'.format(os.path.dirname(path), os.path.splitext(splitted_path)[0], extension)
            img.save(img_name, image_type, **kwargs)

            img_paths[path] = img_name
            img_path_list.append(path)
            img_path_list.append(img_name)

        return img_paths, img_path_list

    @staticmethod
    def resize_image(img, scale, method = Image.LANCZOS):
        finalImg = copy.copy(img)
        if scale < 0: finalImg = finalImg.transpose(Image.ROTATE_180)
        scale = abs(scale)

        if scale == 1: return finalImg
        elif scale > 1: scale = 1
        
        size = np.array(finalImg.size, dtype=np.int64)
        finalImg = finalImg.resize((size * scale).astype(np.int64), method)
        return finalImg