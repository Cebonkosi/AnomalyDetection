from dataStreamSimulator import dataStream
from anomalyDetector import detectAnomalies
from visualization import visualizeStream

if __name__ == "__main__":
    # Simulate a real-time data stream
    data_gen = dataStream()
    
    # Apply anomaly detection to the data stream
    anomaly_gen = detectAnomalies(data_gen)
    
    # Visualize the data and detected anomalies in real-time
    visualizeStream(anomaly_gen)
