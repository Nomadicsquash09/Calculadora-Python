from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_DIR
from display import Display
from info import Info
# from styles import setupTheme
from buttons import ButtonsGrid
import sys


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    # setupTheme()

    icon = QIcon(str(WINDOW_ICON_DIR))
    window.setWindowIcon(icon)

    info = Info('')
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    buttonsGrid = ButtonsGrid(display, info, window)
    # buttonsGrid._makeGrid()
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
