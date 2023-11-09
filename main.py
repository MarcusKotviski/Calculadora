import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from Widgets.main_window import MainWindow
from Widgets.display import Display
from Widgets.buttons import ButtonsGrid
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
    info = Info('')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('Digite algo')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa
    window.adjustFixedSize()
    window.show()
    app.exec()