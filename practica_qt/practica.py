import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Mi app de practica")
        self.initUI()
        
    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("practica")
        
        self.input = QLineEdit(self)
        self.input.move(0, 40)

        self.button1 = QPushButton("Submit", self)
        self.button1.move(0, 80)
        self.button1.clicked.connect(self.texto)
        
    def texto(self):
        res = "texto ingresado: " + self.input.displayText()
        print(res)
        
def ventana():
    app = QApplication(sys.argv)
    ventana = MyWindow()
    ventana.show()
    sys.exit(app.exec())

ventana()