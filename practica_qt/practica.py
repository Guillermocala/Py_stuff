import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QApplication, QMainWindow, 
    QPushButton, QLabel, QLineEdit, QGridLayout, QWidget
    )

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.principal = QGridLayout()
        self.label = QLabel("practica qt")
        self.principal.addWidget(self.label, 0, 0, 1, 1)
        self.input = QLineEdit()
        self.principal.addWidget(self.input, 0, 1, 1, 1)
        self.button1 = QPushButton("Submit")
        self.principal.addWidget(self.button1, 0, 2, 1, 1)
        self.button1.clicked.connect(self.texto)
        self.setLayout(self.principal)
    
    def texto(self):
        res = "texto ingresado: " + self.input.displayText()
        print(res)

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Mi app de practica")
        self.initUI()
        self.initMenuBar()
        self.show()
        
    def initUI(self):
        self.ventana_principal = MainWindow()
        self.setCentralWidget(self.ventana_principal)
    
    def initMenuBar(self):
        self.menu_bar = self.menuBar()
        #opcion 1
        self.opcion1 = self.menu_bar.addMenu("Opcion1")
        self.subAction11 = self.opcion1.addAction("SubOpcion1")
        self.subAction12 = self.opcion1.addAction("SubOpcion2")
        self.subAction11.triggered.connect(self.imprimo)
        self.subAction12.triggered.connect(self.imprimo)
        self.opcion1.addSeparator()
        self.opcion1.addAction("Exit", self.close)
        #opcion2
        self.opcion2 = self.menu_bar.addMenu("Opcion2")
        self.subAction21 = self.opcion2.addAction("SubOpcion1")
        self.subAction22 = self.opcion2.addAction("SubOpcion2")
        self.subAction21.triggered.connect(self.imprimo)
        self.subAction22.triggered.connect(self.imprimo)
    
    def imprimo(self):
        print("soy una accion de los menus")

        
def ventana():
    app = QApplication(sys.argv)
    ventana = MyWindow()
    sys.exit(app.exec())

ventana()