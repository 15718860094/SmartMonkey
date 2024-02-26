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
    
    def calculate_mse(image1, image2):
        img1 = cv2.imread(image1)
        img2 = cv2.imread(image2)

        if img1.shape == img2.shape:
            err = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
            err /= float(img1.shape[0] * img1.shape[1])

            return err
        else:
            return None

image1_path = "image1.jpg"
image2_path = "image2.jpg"

mse = calculate_mse(image1_path, image2_path)
print("Mean Squared Error (MSE):", mse)