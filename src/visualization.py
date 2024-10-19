import matplotlib
matplotlib.use('Qt5Agg')  # Use Qt5 backend for GUI display
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def visualizeStream(data_gen, interval=100):
    """
    Visualizes the data stream and highlights anomalies in real-time.
    
    :param data_gen: Generator object providing (data, anomaly_flag) pairs
    :param interval: Time interval for updating the plot (in ms)
    """
    fig, ax = plt.subplots()
    data_points = []
    anomaly_points = []

    def update(frame):
        data, is_anomaly = next(data_gen)
        data_points.append(data)
        anomaly_points.append(data if is_anomaly else None)

        ax.clear()
        ax.plot(data_points, label="Data Stream")
        ax.scatter(range(len(anomaly_points)), anomaly_points, color='red', label="Anomalies")
        ax.legend(loc="upper left")
        ax.set_title('Real-Time Data Stream and Anomaly Detection')

    ani = animation.FuncAnimation(fig, update, interval=interval)
    plt.show()