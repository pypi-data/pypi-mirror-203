import sys

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src import palette
from src import utils
from src import mainwindow

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)


def main():
    utils.Exeption_handler(mainwindow.Mainwindow, app)


if __name__ == "__main__":
    main()
