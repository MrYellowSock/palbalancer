from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
import numpy as np
class HistogramWidget(QWidget):
    def __init__(self,data,name="Histrogram",xLabel="Value",yLabel="Frequency"):
        super().__init__()
        self.data = data
        
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        self.canvas = HistogramCanvas(data,name,xLabel,yLabel)
        
        self.meanLabel = QLabel(f"Mean : {np.mean(data):.2f}")
        self.medianLabel = QLabel(f"Median : {np.median(data):.2f}")
        self.sdLabel = QLabel(f"SD : {np.std(data):.2f}")

        self.meanLabel.setAlignment(Qt.AlignCenter)
        self.medianLabel.setAlignment(Qt.AlignCenter)
        self.sdLabel.setAlignment(Qt.AlignCenter)
        
        descriptionWidget= QWidget()
        descriptionLayout = QHBoxLayout()
        descriptionLayout.addWidget(self.meanLabel)
        descriptionLayout.addWidget(self.medianLabel)
        descriptionLayout.addWidget(self.sdLabel)
        descriptionWidget.setLayout(descriptionLayout)
       
        layout.addWidget(self.canvas)
        layout.addWidget(descriptionWidget)
        self.setLayout(layout)
        
class HistogramCanvas(FigureCanvas):
    def __init__(self,data,name,xLabel,yLabel, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(fig)
        self.setParent(parent)
        self.plot_histogram(data,name,xLabel,yLabel)

    def plot_histogram(self,data,name,xLabel,yLabel):

        # Create histogram
        self.ax.hist(data, alpha=0.5, color='blue', edgecolor='black')

        # Set labels and title
        self.ax.set_title(name)
        self.ax.set_xlabel(xLabel)
        self.ax.set_ylabel(yLabel)

        # Draw the plot
        self.draw()
