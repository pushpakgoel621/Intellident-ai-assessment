def classify(features):                                         #declaring function to classify images on basis of Dark/Bright image
    mean_intensity = features["mean_intensity"]

    if mean_intensity > 127:
        return "Bright Image"
    else:
        return "Dark Image"
