"""
Data preprocessing for Parkinson's disease screening
using spiral drawing images
"""

import numpy as np
import cv2

def load_and_preprocess_image(image_path, img_size=(128, 128)):
    """
    Load a spiral image, resize, normalize, and expand dimensions.

    Parameters:
        image_path (str): Path to spiral image
        img_size (tuple): Target image size

    Returns:
        numpy.ndarray: Preprocessed image
    """

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        return None

    image = cv2.resize(image, img_size)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=-1)

    return image
