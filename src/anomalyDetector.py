import numpy as np
from collections import deque

def detectAnomalies(data_gen, window_size=50, threshold=3):
    """
    Detects anomalies in the data stream using the Z-score method.
    
    :param data_gen: Generator object for streaming data
    :param window_size: Size of the sliding window for Z-score calculation
    :param threshold: Z-score threshold to flag an anomaly
    :return: Yields data and a boolean flag (True if anomaly, else False)
    """
    window = deque(maxlen=window_size)
    
    for data in data_gen:
        if len(window) == window_size:
            mean = np.mean(window)
            std = np.std(window)
            if std == 0:  # Prevent division by zero
                z_score = 0
            else:
                z_score = (data - mean) / std
            yield data, abs(z_score) > threshold
        else:
            yield data, False  # Not enough data for anomaly detection
        window.append(data)
