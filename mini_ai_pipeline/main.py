#load all required packages

from pipeline.loader import load_images
from pipeline.preprocess import preprocess_image
from pipeline.features import extract_features
from pipeline.classifier import classify

IMAGE_DIR = "data"  #giving path for folder containing images

def run_pipeline():                          #define function
    images = load_images(IMAGE_DIR)          #load images for folder

    if not images:
        print("No images found.")
        return

    for filename, image in images:                      #running to process all images
        processed = preprocess_image(image)             
        features = extract_features(processed)
        label = classify(features)

        print(f"{filename}")                                                            #printing required details from image
        print(f"  Mean Intensity: {features['mean_intensity']:.2f}")
        print(f"  Resolution: {features['resolution']}")
        print(f"  Classification: {label}")
        print("-" * 40)

if __name__ == "__main__":                                                              #function to prevent accidental executions
    run_pipeline()
