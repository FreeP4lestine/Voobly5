import sys
import os
from PyQt5 import QtWidgets, uic
from pathlib import Path
from colormap import rgb2hex, hex2rgb
import cssutils


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(cwd + '\\manager.ui', self)
        self.btns = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6,
                     self.btn_7, self.btn_8, self.btn_9, self.btn_10, self.btn_11, self.btn_12]
        for btn in self.btns:
            btn.clicked.connect(self.setcolor)
        self.show()

    def cssmap(self):
        self.cssbtn = {
            'QPushButton': {
                'normal': 'min-width: 140px;'
                'min-height: 30px;'
                'max-height: 30px;'
                'background-color: #393939;'
                'color: ' + self.selclr + ';'
                'border-radius: 4px;',

                'hover': 'background-color: ' + self.selclr + ';'
                'color: ' + self.invertcolor(self.selclr) + ';',

                'pressed': 'text-decoration: underline;'
            }
        }
        self.cssfile = {
            'messenger.css': [self.cssbtn['QPushButton']]
        }
        
    def setcolor(self):
        self.clearbtncheck()
        btn = self.sender()
        btn.setText('🗸')
        clr = btn.palette().button().color().name()
        inv = self.invertcolor(clr)
        css = 'color:' + inv + ';background:' + clr + ';border:1px solid #000000'
        btn.setStyleSheet(css)
        self.selclr = clr
        self.cssmap()
        
    def clearbtncheck(self):
        for btn in self.btns:
            btn.setText('')

    def invertcolor(self, hex):
        rgb = list(hex2rgb(hex))
        for a in range(len(rgb)):
            rgb[a] = 255 - rgb[a]
        hex = rgb2hex(rgb[0], rgb[1], rgb[2])
        return hex


# the current working directory
cwd = os.path.dirname(os.path.realpath(__file__))
# show the app window
man = QtWidgets.QApplication(sys.argv)
man.setStyleSheet(Path(cwd + '\\manager.css').read_text())
win = Ui()
man.exec_()
