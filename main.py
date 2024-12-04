import sys
import sqlite3
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


# класс главного экрана
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cofee.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        cur = self.con.cursor()
        result = cur.execute(f"select * from cofee").fetchall()
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setColumnCount(len(self.titles))
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
