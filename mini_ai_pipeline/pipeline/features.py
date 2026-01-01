import numpy as np
                                                                        #declaring function to calculate mean intensity and resolution of image
def extract_features(image):
    mean_intensity = np.mean(image)
    height, width = image.shape
    resolution = height * width

    return {
        "mean_intensity": mean_intensity,
        "resolution": resolution
    }
