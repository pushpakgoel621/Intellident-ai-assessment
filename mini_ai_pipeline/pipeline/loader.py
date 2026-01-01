import cv2
import os

def load_images(image_dir):                                                 #funciton to load images from image directory
    images = []

    for file in os.listdir(image_dir):                                      #loop to process each image in directory
        if file.lower().endswith((".jpg", ".png", ".jpeg")):                #selecting only image files from directory
            path = os.path.join(image_dir, file)
            img = cv2.imread(path)
            if img is not None:
                images.append((file, img))

    return images
