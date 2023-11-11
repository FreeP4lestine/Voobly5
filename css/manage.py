from PyQt5 import QtWidgets, uic
import sys
import os
from pathlib import Path
from colormap import rgb2hex, hex2rgb


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(cwd + '\\manager.ui', self)
        self.btns = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6,
                     self.btn_7, self.btn_8, self.btn_9, self.btn_10, self.btn_11, self.btn_12]
        for btn in self.btns:
            btn.clicked.connect(self.setcolor)
        self.show()
        self.btns[0].setText('🗸')
        self.btns[0].click()

    def setcolor(self):
        self.clearbtncheck()
        btn = self.sender()
        btn.setText('🗸')
        clr = btn.palette().button().color().name()
        inv = self.invertcolor(clr)
        css = 'color:' + inv + ';background:' + clr + ';border:1px solid #000000'
        btn.setStyleSheet(css)

    def clearbtncheck(self):
        for btn in self.btns:
            btn.setText('')

    def invertcolor(self, hex):
        rgb = list(hex2rgb(hex))
        rgb[0] = 255 - rgb[0]
        rgb[1] = 255 - rgb[1]
        rgb[2] = 255 - rgb[2]
        hex = rgb2hex(rgb[0], rgb[1], rgb[2])
        return hex


# the current working directory
cwd = os.path.dirname(os.path.realpath(__file__))
# show the app window
man = QtWidgets.QApplication(sys.argv)
man.setStyleSheet(Path(cwd + '\\manager.css').read_text())
win = Ui()
man.exec_()
