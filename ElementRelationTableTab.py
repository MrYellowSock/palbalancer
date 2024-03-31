
import pandas as pd
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from ElementRelationTable import ElementRelationTable
from ElementTable import ElementTable
class PalElementPowerTable(QTableWidget):
    def __init__(self, EntityRelationDF: pd.DataFrame):
        super().__init__()
        self.setColumnCount(len(EntityRelationDF.columns))
        self.setRowCount(len(EntityRelationDF))
        self.setHorizontalHeaderLabels(EntityRelationDF.columns)
        self.setVerticalHeaderLabels(EntityRelationDF.index)
        self.selectionModel().selectionChanged.connect(self.onSelectionChanged)
        for row in range(len(EntityRelationDF)):
            for col in range(len(EntityRelationDF.columns)):
                self.setItem(row, col, QTableWidgetItem(str(EntityRelationDF.iloc[row, col])))

        for row in range(self.rowCount()):
            self.setRowHeight(row, 60)  # Set the row height as per your requirement
        for col in range(self.columnCount()):
            self.setColumnWidth(col, 120)

        self.setWindowTitle("Element Power Table")
        self.setGeometry(100, 100, 800, 600)
    def onSelectionChanged(self,selected,deselected):
        for i in deselected.indexes():
            row,column = i.row(),i.column()
            temp =list(ElementTable.instance().datas.keys())
            attackType,targetType = temp[row],temp[column]
            item = self.item(row,column)
            statusList = ElementRelationTable.toStatusList(item.text())
            if statusList is not None:
                ElementRelationTable.Instance().setRelation(attackType,targetType,statusList)
                ElementRelationTable.Instance().WriteCSV()