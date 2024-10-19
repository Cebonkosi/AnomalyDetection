import numpy as np
import random

def dataStream():
    time = 0
    while True:
        value = np.sin(0.1 * time) + np.random.normal(0, 0.5)  # Base signal with noise
        if random.random() > 0.95:  # Introduce random anomalies
            value += np.random.normal(5, 2)
        yield value
        time += 1