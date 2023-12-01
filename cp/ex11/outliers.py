import numpy as np
from cp.ex11.bacterial_growth import get_mean, get_std


def outliers(data: np.ndarray) -> np.ndarray:
    """Return the experiment indices of outlier experiments based on final bacteria counts.

    Parameters:
    data (ndarray): The data to search.

    Returns:
    ndarray: Array containing indices of outlier experiments.
    """

    # Calculate the final bacteria counts for each experiment (last time-step)
    final_counts = data[:, -1]  # Assuming the last column represents the final counts

    # Calculate the mean and standard deviation of all final counts
    mean_count = get_mean(final_counts)
    std_count = get_std(final_counts)

    # Calculate the threshold for outliers
    outlier_threshold = mean_count + 2 * std_count

    # Identify outlier experiments
    outlier_indices = np.where(final_counts > outlier_threshold)[0]

    return outlier_indices
