import cv2

def preprocess_image(image, size=(128, 128)):                                     #funciton to convert image to size of 128*128
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                #converting image to black and white
    resized = cv2.resize(gray, size)
    return resized
