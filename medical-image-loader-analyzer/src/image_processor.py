import cv2

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def resize_image(image, size=(256, 256)):
    return cv2.resize(image, size)
