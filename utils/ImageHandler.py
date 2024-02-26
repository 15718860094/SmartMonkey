import base64
import cv2
import numpy as np

class ImageHandler(object):
    def __init__(self, image_path):
        self.image_path = image_path

    def encode_image_base64(self):
        with open(self.image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read())
        return encoded_image.decode("utf-8")