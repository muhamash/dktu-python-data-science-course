import numpy as np


def load_data() -> np.ndarray:
    """Load data from 160 files into one array. Files are located in cp/ex11/files/experiments.

    :return: The data from the files in one array.
    """
    A = np.zeros((160, 12))
    for i in range(160):
        filename = f"cp/ex11/files/experiments/experiment_{i:03}.csv"
        # data[i] = np.loadtxt(filename, delimiter=",")
        x = np.loadtxt(filename, delimiter=",")
        A[i, :] = x
    # return np.ndarray(data)
    # print(A)
    return A


def threshold_exceeded(data: np.ndarray, threshold: float) -> np.ndarray:
    """Return the index at which the threshold is exceeded for each experiment.

    :param data: The data to search.
    :param threshold: The threshold to compare against.
    :return: The index at which the threshold is exceeded for each row.
    """
    # return np.argmax(data > threshold, axis=1)
    b = []
    for i in range(data.shape[0]):
        x = data[i, :]
        for j in range(len(x)):
            if x[j] > threshold:
                break
        b.append(j)
    return np.array(b)


def get_mean(data: np.ndarray) -> np.ndarray:
    """Calculate the mean of the data.

    :param data: The data to calculate the mean of.
    :return: The mean of the data for each time-point.
    """
    return np.mean(data, axis=0)


def get_std(data: np.ndarray) -> np.ndarray:
    """Calculate the standard deviation of the data.

    :param data: The data to calculate the standard deviation of.
    :return: The standard deviation of the data for each time-point.
    """
    return np.std(data, axis=0)


# print(load_data)
# if __name__ == "__main__":
#     A = load_data()
#     b = threshold_exceeded(A, 2)
#     print(b)
#     print(A.shape)
