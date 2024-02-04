
import pandas as pd
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class PalElementPowerTable(QTableWidget):
    def __init__(self, elementPowerTable: pd.DataFrame):
        super().__init__()
        self.setColumnCount(len(elementPowerTable.columns))
        self.setRowCount(len(elementPowerTable))
        self.setHorizontalHeaderLabels(elementPowerTable.columns)
        for row in range(len(elementPowerTable)):
            for col in range(len(elementPowerTable.columns)):
                self.setItem(row, col, QTableWidgetItem(str(elementPowerTable.iloc[row, col])))

        for row in range(self.rowCount()):
            self.setRowHeight(row, 60)  # Set the row height as per your requirement
        for col in range(self.columnCount()):
            self.setColumnWidth(col, 120)

        self.setWindowTitle("Element Power Table")
        self.setGeometry(100, 100, 800, 600)