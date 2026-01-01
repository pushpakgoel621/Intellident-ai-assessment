import os
import cv2

def load_images_from_folder(folder_path):
    images = []
    image_names = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        image = cv2.imread(file_path)

        if image is None:
            print(f"Skipping unreadable file: {file_name}")
            continue

        images.append(image)
        image_names.append(file_name)

    return images, image_names
