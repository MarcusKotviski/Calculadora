import sys

from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display

if __name__ == '__main__':
    # Cria aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display()
    display.setPlaceholderText('Digite algo')
    window.addToVLayout(display)

    # Executa
    window.ajustFixedSize()
    window.show()
    app.exec()