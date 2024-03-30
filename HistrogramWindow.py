from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
class HistogramWindow(QMainWindow):
    def __init__(self,data,name="Histrogram",xLabel="Value",yLabel="Frequency"):
        super().__init__()
        self.data = data
        self.setWindowTitle("Histogram in PyQt5")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.canvas = HistogramCanvas(data,name,xLabel,yLabel)
        layout.addWidget(self.canvas)
class HistogramCanvas(FigureCanvas):
    def __init__(self,data,name,xLabel,yLabel, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(fig)
        self.setParent(parent)
        self.plot_histogram(data,name,xLabel,yLabel)

    def plot_histogram(self,data,name,xLabel,yLabel):

        # Create histogram
        self.ax.hist(data, bins=30, alpha=0.5, color='blue', edgecolor='black')

        # Set labels and title
        self.ax.set_title(name)
        self.ax.set_xlabel(xLabel)
        self.ax.set_ylabel(yLabel)

        # Draw the plot
        self.draw()
