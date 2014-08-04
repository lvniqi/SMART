# -*- coding: utf-8 -*-
from PyQt4.uic.Compiler.qtproxies import QtCore, QtGui
#ͼ��ģ��pyqt4
from PyQt4 import QtGui,QtCore,Qwt5
from PyQt4.QtCore import Qt
from setting_ui import Ui_Form
import sys

class Widget_Show(QtGui.QDialog,Ui_Form):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setupUi(self) # Ui_Form.setupUi

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    widget = Widget_Show()
    #widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #widget.showFullScreen()
    widget.show()
    sys.exit(app.exec_())
