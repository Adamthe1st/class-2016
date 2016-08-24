import numpy as np


def find_min(data, threshold):

    m = np.min(data)
    avg = np.mean(data)
    pos = np.argmin(data)

    if abs(m - avg) / abs(avg) > threshold:
        return pos
    else:
        return None
