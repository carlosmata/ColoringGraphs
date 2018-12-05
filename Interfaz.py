import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, \
    QPushButton, QAction, QLineEdit, QMessageBox, \
    QCalendarWidget, QLabel, QVBoxLayout, QDialog, QTableWidget, \
    QTableWidgetItem, QGroupBox, QGridLayout, QCheckBox, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QDate
import sip
import Vertex, Graph


# class App(QWidget): QMainWindow
class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        # super().__init__()
        self.title = 'Problema de Scheduling'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480

        self.numberOfColumns = 0
        self.numberOfRows = 0

        self.graph = None

        # self.textoQuery = QLineEdit(self)

        self.addColumn = QPushButton('Agregar Materia', self)
        self.addRow = QPushButton('Agregar Alumno', self)
        self.beginCalculation = QPushButton("Realizar Análisis", self)

        self.tableWidget = QTableWidget(self)

        # set row count
        self.tableWidget.setRowCount(0)

        # set column count
        self.tableWidget.setColumnCount(0)

        self.horizontalHeaders = []
        self.verticalHeaders = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.textoQuery.move(20, 20)
        # self.textoQuery.resize(280, 40)

        self.tableWidget.setGeometry(55, 55, 550, 400)
        self.tableWidget.clicked.connect(self.on_click)
        self.tableWidget.show()

        self.addColumn.move(0, 10)
        self.addColumn.clicked.connect(self.AddColumn)

        self.addRow.move(95, 10)
        self.addRow.clicked.connect(self.AddRow)

        self.beginCalculation.move(190, 10)
        self.beginCalculation.clicked.connect(self.BeginCalculation)

        #Testing
        for j in range(7):
            self.numberOfColumns += 1
            self.tableWidget.setColumnCount(self.numberOfColumns)
            self.horizontalHeaders.append("ColTest" + str(j))
            self.tableWidget.setHorizontalHeaderLabels(self.horizontalHeaders)
            for i in range(self.numberOfRows):
                self.tableWidget.setItem(i, self.numberOfColumns - 1, QTableWidgetItem(" "))
            self.tableWidget.resizeColumnsToContents()

        for j in range(6):
            self.numberOfRows += 1
            self.tableWidget.setRowCount(self.numberOfRows)
            self.verticalHeaders.append("RowTest" + str(j))
            self.tableWidget.setVerticalHeaderLabels(self.verticalHeaders)
            for i in range(self.numberOfColumns):
                self.tableWidget.setItem(self.numberOfRows - 1, i, QTableWidgetItem(" "))
            self.tableWidget.resizeRowsToContents()
        #Testing

        self.show()

    def AddColumn(self):
        text, okPressed = QInputDialog.getText(self, "Get text", "Nombre de la Materia:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.numberOfColumns += 1
            self.tableWidget.setColumnCount(self.numberOfColumns)
            self.horizontalHeaders.append(text)
            self.tableWidget.setHorizontalHeaderLabels(self.horizontalHeaders)
            for i in range(self.numberOfRows):
                self.tableWidget.setItem(i, self.numberOfColumns - 1, QTableWidgetItem(" "))
            self.tableWidget.resizeColumnsToContents()

    def AddRow(self):
        text, okPressed = QInputDialog.getText(self, "Get text", "Nombre del Alumno:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.numberOfRows += 1
            self.tableWidget.setRowCount(self.numberOfRows)
            self.verticalHeaders.append(text)
            self.tableWidget.setVerticalHeaderLabels(self.verticalHeaders)
            for i in range(self.numberOfColumns):
                self.tableWidget.setItem(self.numberOfRows - 1, i, QTableWidgetItem(" "))
            self.tableWidget.resizeRowsToContents()

    def on_click(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            if self.tableWidget.item(currentQTableWidgetItem.row(), currentQTableWidgetItem.column()).text() == " ":
                self.tableWidget.setItem(currentQTableWidgetItem.row(),
                                         currentQTableWidgetItem.column(),
                                         QTableWidgetItem("x"))
            else:
                self.tableWidget.setItem(currentQTableWidgetItem.row(),
                                         currentQTableWidgetItem.column(),
                                         QTableWidgetItem(" "))

    def BeginCalculation(self):
        print(self.tableWidget.item(0, 1).text())
        # Se Crean los Vértices primero
        vertices = []
        for header in self.horizontalHeaders:
            vertices.append(Vertex.Vertex(header))
        # Se establecen las aristas
        for j in range(self.numberOfRows):
            aristas = []
            for i in range(self.numberOfColumns):
                if self.tableWidget.item(j, i).text() != " ":
                    # agrergar aristas
                    aristas.append(vertices[i])
            for vertex in aristas:
                vertex.setEdgesWithoutSelf(aristas)

        self.graph = Graph.GraphC(vertices)
        self.graph.coloring()
        print(self.graph.print())
        self.ventana2 = VentanaGrafo()
        self.ventana2.show()


class VentanaGrafo(QMainWindow):

    def __init__(self):
        super(VentanaGrafo, self).__init__()
        QMainWindow.__init__(self)

        self.title = "Grafo Pintado"
        self.setWindowTitle(self.title)

        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480

        self.setGeometry(self.left, self.top, self.width, self.height)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
