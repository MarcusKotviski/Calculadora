import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from Widgets.main_window import MainWindow
from Widgets.display import Display
from Widgets.info import Info
from static.styles import setupTheme
from static.variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria aplicação
    app = QApplication(sys.argv)
    # Style
    setupTheme()
    window = MainWindow()

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('Digite algo')
    window.addToVLayout(display)

    # Executa
    window.ajustFixedSize()
    window.show()
    app.exec()