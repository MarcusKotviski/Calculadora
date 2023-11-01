from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando Layout base
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # Titulo
        self.setWindowTitle('Calculadora')


    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
        self.ajustFixedSize()

    def ajustFixedSize(self):
        # uLTIMA COISAS A SEREM FEITAS
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())