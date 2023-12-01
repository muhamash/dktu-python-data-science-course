import numpy as np


def bacterial_area(npy_path: str) -> float:
    """Calculate the fraction of the image where pixel intensities are greater than 100.

    Parameters:
    :param npy_path: Path to the image data file in NumPy format.
    :return: The fraction of area in an image where there are bacteria.
    """
    # Load the image data from the NumPy file
    image_data = np.load(npy_path)

    # Calculate the area where pixel intensities are greater than 100
    bacteria_area = np.sum(image_data > 100)

    # Calculate the total number of pixels in the image
    total_pixels = np.prod(image_data.shape)

    # Calculate the fraction of area with intensities greater than 100
    fraction_area = bacteria_area / total_pixels

    return fraction_area
