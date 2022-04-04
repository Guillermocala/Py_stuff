import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class LabelPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout_principal = QtWidgets.QVBoxLayout(self)
        self.pestañas = QtWidgets.QTabWidget()
        self.layout_principal.addWidget(self.pestañas)

        self.gb_alfabetos = QtWidgets.QGroupBox("Pantalla principal alfabetos")

        self.principal_alfabetos = QtWidgets.QVBoxLayout()
        
        self.label1 = QtWidgets.QLabel("Ingresar alfabeto: ")
        self.input1 = QtWidgets.QLineEdit()
        self.button1 = QtWidgets.QPushButton("add")
        self.principal_alfabetos.addWidget(self.label1)
        self.principal_alfabetos.addWidget(self.input1)
        self.principal_alfabetos.addWidget(self.button1)
        self.gb_alfabetos.setLayout(self.principal_alfabetos)

        self.pestañas.addTab(self.gb_alfabetos, "Alfabetos")
        self.principal_alfabetos.addStretch(0)
        self.button1.clicked.connect(self.clickme)

    def clickme(self):
        print("Button clicked, Hello!")
            
        
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    label = LabelPrincipal()
    label.resize(500,500)
    label.show()

    sys.exit(app.exec())