import os
import cv2
from src.image_loader import load_images_from_folder
from src.image_processor import convert_to_grayscale, resize_image
from src.analyzer import calculate_image_stats

RAW_IMAGE_DIR = "data"
OUTPUT_DIR = "output"
IMAGE_SIZE = (256, 256)

os.makedirs(OUTPUT_DIR, exist_ok=True)

images, image_names = load_images_from_folder(RAW_IMAGE_DIR)

for image, name in zip(images, image_names):
    gray_image = convert_to_grayscale(image)
    resized_image = resize_image(gray_image, IMAGE_SIZE)

    stats = calculate_image_stats(resized_image)

    output_path = os.path.join(OUTPUT_DIR, name)
    cv2.imwrite(output_path, resized_image)

    print(f"Image: {name}")
    print(f"Resolution: {stats['resolution']}")
    print(f"Mean Pixel Intensity: {stats['mean_intensity']}")
    print("-" * 40)
