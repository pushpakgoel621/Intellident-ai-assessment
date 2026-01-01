import numpy as np

def calculate_image_stats(image):
    height, width = image.shape
    mean_intensity = np.mean(image)

    return {
        "resolution": f"{width} x {height}",
        "mean_intensity": round(float(mean_intensity), 2)
    }
