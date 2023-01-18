import sys
import pyperclip as pc          # pip install pyperclip
from io import BytesIO
import win32clipboard as wcb    # pip install pywin32
from PIL import Image           # pip install pillow

from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget,
    QVBoxLayout, QPushButton
)

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setGeometry(0, 0, 200, 500)
        "inicializacion de componentes"
        self.initUI()
        "para mostrar la ventana, sin esto no pasa nada"
        self.show()

    def initUI(self):
        self.message = QLabel("Recursos para copia rápida")
        self.mainContainer = QWidget()
        self.container = QVBoxLayout(self.mainContainer)
        self.botonTexto = QPushButton("Copiar texto")
        self.botonTexto.clicked.connect(self.copyText)
        self.botonImagen = QPushButton("Copiar imagen")
        self.botonImagen.clicked.connect(self.copyImage)
        self.botonTexto.setFixedSize(QSize(220, 220))
        self.botonImagen.setFixedSize(QSize(220, 220))
        self.container.addWidget(self.message)
        self.container.addWidget(self.botonTexto)
        self.container.addWidget(self.botonImagen)
        self.setCentralWidget(self.mainContainer)

    def copyText(self):
        # el encoding es lo más importante para que copie los
        # caracteres especiales como emojis
        # ===========PATH DEL TEXTO
        filepath_texto = "data.txt"
        data = open(filepath_texto, "r", encoding='utf-8').read()
        pc.copy(data)

    def copyImage(self, filepath):
        # ===========PATH DE LA IMAGEN
        filepath_image = "promotor.jpg"
        image = Image.open(filepath_image)
        # operaciones de manejo de imagen
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        # operaciones con el clipboard
        wcb.OpenClipboard()
        wcb.EmptyClipboard()
        wcb.SetClipboardData(wcb.CF_DIB, data)
        wcb.CloseClipboard()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyApp()
    sys.exit(app.exec())