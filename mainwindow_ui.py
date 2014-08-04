# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jul 25 23:23:58 2014
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName(_fromUtf8("Window"))
        Window.resize(700, 531)
        Window.setMinimumSize(QtCore.QSize(0, 80))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("png/joypad.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window.setWindowIcon(icon)
        Window.setStyleSheet(_fromUtf8("*{   \n"
"  font-size:10.5pt;   \n"
"  color:white;   \n"
"  font-family:\"Microsoft YaHei UI\";   \n"
"}\n"
"QMenuBar\n"
"{\n"
"    background: transparent;\n"
"    color: silver;\n"
"    \n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"    \n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    color: black;\n"
"    background-color: white;\n"
";\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"    margin-bottom:1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    background-color: #010101;\n"
"    \n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"    \n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"    background-color: white;\n"
"}\n"
"   \n"
"CallWidget QLineEdit#telEdt  \n"
"{   \n"
"  font-size:24px;   \n"
"}   \n"
"QMainWindow,QDialog{   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #1B2534, stop: 0.4 #010101,   \n"
"                                 stop: 0.5 #000101, stop: 1.0 #1F2B3C);   \n"
"}   \n"
"QWidget{   \n"
"    background:#121922;   \n"
"}   \n"
"QLabel{   \n"
"   background:transparent;   \n"
"}   \n"
"DailForm QLineEdit#phoneLineEdt{   \n"
"  font-size:36px;   \n"
"  font-weight: bold;   \n"
"}   \n"
"QPushButton,QToolButton{   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);  \n"
"    border-style: outset;  \n"
"    border-width: 1px;   \n"
"    border-radius: 5px;   \n"
"    border-color: #11223F;   \n"
"    padding: 1px;   \n"
"    min-width: 2em;\n"
"}   \n"
"QPushButton::hover,QToolButton::hover{   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #313C4F); \n"
"    border-color: #5D8B9E;  \n"
"    \n"
"}   \n"
"QPushButton::pressed,QToolButton::pressed{   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #717C8F); \n"
"    color: white;\n"
"    border-color: #5D8B9E;   \n"
"}   \n"
"QPushButton::disabled,QToolButton::disabled{   \n"
"    background: rgb(10, 10,10);\n"
"    border-color: #0A1320;   \n"
"    color:#6A6864;   \n"
"}   \n"
"QDialog QPushButton,QDialog QToolButton{   \n"
"  min-width:30px;   \n"
"  min-height:23px;   \n"
"}   \n"
"QToolButton[objectName=\"minimizeToolBtn\"] {   \n"
"    background: transparent;   \n"
"    border:none;   \n"
"    /*image:url(qss/minimize.png)*/\n"
"}   \n"
"QToolButton[objectName=\"minimizeToolBtn\"]:hover,QToolButton[objectName=\"minimizeToolBtn\"]:pressed {   \n"
"    /*image:url(qss/minimize_hover.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"maximizeToolBtn\"] {   \n"
"    background: transparent;   \n"
"    border:none;   \n"
"    /*image:url(qss/maximize.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"maximizeToolBtn\"]:hover,QToolButton[objectName=\"maximizeToolBtn\"]:pressed {   \n"
"    /*image:url(qss/maximize_hover.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"closeToolBtn\"],QToolButton[objectName=\"customCloseWindow\"] {   \n"
"    background: transparent;   \n"
"    border:none;   \n"
"    /*image:url(qss/close.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"closeToolBtn\"]:hover,QToolButton[objectName=\"closeToolBtn\"]:pressed{   \n"
"    /*image:url(qss/close_hover.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"customCloseWindow\"]:hover,QToolButton[objectName=\"customCloseWindow\"]:pressed{   \n"
"    /*image:url(qss/close_hover.png)*/   \n"
"}   \n"
"QToolButton[objectName=\"titleSetUpToolBtn\"]{   \n"
"    background: transparent;   \n"
"    border:none;   \n"
"    /*image:url(qss/setup.png)*/   \n"
"}   \n"
"DailForm QToolButton#oneToolBtn,QToolButton#OneToolBtn,QToolButton#twoToolBtn,QToolButton#threeToolBtn,   \n"
"         QToolButton#fourToolBtn,QToolButton#fiveToolBtn,QToolButton#sixToolBtn,   \n"
"         QToolButton#sevenToolBtn,QToolButton#eightToolBtn,QToolButton#nineToolBtn,   \n"
"         QToolButton#starToolBtn,QToolButton#zeroToolBtn,QToolButton#sharpToolBtn {   \n"
"    font-size:36px;   \n"
"    border-radius: 10px;   \n"
"}   \n"
"DailForm QToolButton#delToolBtn{   \n"
"    border-radius: 10px;   \n"
"}   \n"
"QFrame{   \n"
"    border-color:#32435E;   \n"
"    border-width:1px;   \n"
"    border-radius: 3px;   \n"
"}   \n"
"QLineEdit,QTextEdit {   \n"
"    border: 1px solid #32435E;   \n"
"    border-radius: 3px;   \n"
"    /* padding: 0 8px; */  \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);   \n"
"    selection-background-color: #0A246A;   \n"
"}   \n"
"QLineEdit::hover{   \n"
"  border-color:#5D8B9E;   \n"
"}   \n"
"QLineEdit[echoMode=\"3\"] {   \n"
"     lineedit-password-character: 9679;   \n"
"}   \n"
"#QLineEdit:read-only {   \n"
"     background: #543F7C;   \n"
"}   \n"
"QTabWidget::pane { /* The tab widget frame */  \n"
"     border: 1px solid #ffffff;   \n"
"     position: absolute;    \n"
"}   \n"
"QTabWidget#MainTabWidget::tab-bar {   \n"
"     left: -3px; /* move to the right by 5px */  \n"
"}   \n"
"QTabWidget#MainTabWidget QTabBar::tab {   \n"
"     height: 14ex;   \n"
"     width: 14ex;   \n"
"}   \n"
"QTabBar::tab {   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);  \n"
"}   \n"
"QTabBar::tab:selected{   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #717C8F); \n"
"    \n"
"}   \n"
"QTabBar::tab:hover {   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #313C4F); \n"
"    \n"
"}\n"
"QTabBar::tab:pressed{   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #717C8F); \n"
"    color: white;\n"
"    border-color: #5D8B9E;   \n"
"}     \n"
"#QTabBar::tab:selected {   \n"
"     border-color: #32435E;   \n"
"     border-right-color: #32435E; /* same as pane color */  \n"
"}   \n"
"#QTabBar::tab:!selected {   \n"
"     margin-left: 2px; /* make non-selected tabs look smaller */  \n"
"}   \n"
"#QTabBar:tab:first:selected {   \n"
"    margin-top: 0;   \n"
"}   \n"
"QTabBar:tab:last:selected {   \n"
"    margin-right: 0;   \n"
"}   \n"
"QTabBar:tab:only-one {   \n"
"     margin: 0;   \n"
"}   \n"
"QListWidget{   \n"
"    border: 1px solid #32435E;   \n"
"    background:#050609;   \n"
"}   \n"
"QListWidget::item:selected {   \n"
"     /*border: 0px solid #33CCFF;*/  \n"
"     border:none;   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #6A848C,  stop: 1.0 #0F9EAF);   \n"
"     padding:0px;   \n"
"     margin:0px;   \n"
"}   \n"
"#QListWidget::item:selected:!active {   \n"
"     border-width: 0px ;   \n"
"}   \n"
"#QListWidget::item:selected:active {   \n"
"     border-width: 1px;   \n"
"}   \n"
"  \n"
"QComboBox {   \n"
"     border: 1px solid #32435E;   \n"
"     border-radius: 3px;   \n"
"     padding: 1px 18px 1px 3px;   \n"
"     min-width: 6em;   \n"
"}   \n"
"QComboBox::hover{   \n"
"  border-color:#5D8B9E;   \n"
"}   \n"
"QComboBox:editable {   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);   \n"
"}   \n"
"QComboBox:!editable, QComboBox::drop-down:editable {   \n"
"      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);   \n"
"}   \n"
"/* QComboBox gets the \"on\" state when the popup is open */  \n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #080B10,   \n"
"                                 stop: 1.0 #212C3F);;   \n"
"}   \n"
"QComboBox:on { /* shift the text when the popup opens */  \n"
"     padding-top: 3px;   \n"
"     padding-left: 4px;   \n"
"}   \n"
"QComboBox::drop-down {   \n"
"     subcontrol-origin: padding;   \n"
"     subcontrol-position: top right;   \n"
"     width: 15px;   \n"
"     border-left-width: 1px;   \n"
"     border-left-color: 32435E;   \n"
"     border-left-style: solid; /* just a single line */  \n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */  \n"
"     border-bottom-right-radius: 3px;   \n"
"}   \n"
"QComboBox::down-arrow {   \n"
"     /*image: url(qss/downarrow.png);*/ \n"
"     \n"
"}   \n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */  \n"
"     top: 1px;   \n"
"     left: 1px;   \n"
"}   \n"
"QComboBox QAbstractItemView {   \n"
"     border: 2px solid #32435E;   \n"
"     selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #506B79,   \n"
"                                 stop: 1.0 #0D95A6);   \n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #1B2534, stop: 0.4 #010101,   \n"
"                                 stop: 0.5 #000101, stop: 1.0 #1F2B3C);   \n"
"} "))
        self.centralwidget = QtGui.QWidget(Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.toolButton_setting = QtGui.QToolButton(self.centralwidget)
        self.toolButton_setting.setObjectName(_fromUtf8("toolButton_setting"))
        self.gridLayout_3.addWidget(self.toolButton_setting, 1, 3, 1, 1)
        self.left_layout1 = QtGui.QGridLayout()
        self.left_layout1.setObjectName(_fromUtf8("left_layout1"))
        self.gridLayout_3.addLayout(self.left_layout1, 0, 0, 1, 5)
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.menubar.setFont(font)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setGeometry(QtCore.QRect(185, 183, 131, 155))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.menuMenu.setFont(font)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.about_Menu = QtGui.QMenu(self.menubar)
        self.about_Menu.setGeometry(QtCore.QRect(317, 183, 112, 74))
        self.about_Menu.setObjectName(_fromUtf8("about_Menu"))
        self.setting = QtGui.QMenu(self.menubar)
        self.setting.setObjectName(_fromUtf8("setting"))
        Window.setMenuBar(self.menubar)
        self.dockWidget = QtGui.QDockWidget(Window)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(291, 170))
        self.dockWidget.setMaximumSize(QtCore.QSize(300, 170))
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label32_11 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.label32_11.setFont(font)
        self.label32_11.setObjectName(_fromUtf8("label32_11"))
        self.horizontalLayout_16.addWidget(self.label32_11)
        self.comboBox_baudrate = QtGui.QComboBox(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.comboBox_baudrate.setFont(font)
        self.comboBox_baudrate.setObjectName(_fromUtf8("comboBox_baudrate"))
        self.comboBox_baudrate.addItem(_fromUtf8(""))
        self.comboBox_baudrate.addItem(_fromUtf8(""))
        self.comboBox_baudrate.addItem(_fromUtf8(""))
        self.comboBox_baudrate.addItem(_fromUtf8(""))
        self.horizontalLayout_16.addWidget(self.comboBox_baudrate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.checkBox_y = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBox_y.setObjectName(_fromUtf8("checkBox_y"))
        self.horizontalLayout_17.addWidget(self.checkBox_y)
        self.checkBox_x = QtGui.QCheckBox(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.checkBox_x.setFont(font)
        self.checkBox_x.setAcceptDrops(False)
        self.checkBox_x.setAutoFillBackground(False)
        self.checkBox_x.setChecked(True)
        self.checkBox_x.setObjectName(_fromUtf8("checkBox_x"))
        self.horizontalLayout_17.addWidget(self.checkBox_x)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_242 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.label_242.setFont(font)
        self.label_242.setObjectName(_fromUtf8("label_242"))
        self.horizontalLayout_18.addWidget(self.label_242)
        self.comboBox_com = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox_com.setMaximumSize(QtCore.QSize(187, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.comboBox_com.setFont(font)
        self.comboBox_com.setObjectName(_fromUtf8("comboBox_com"))
        self.horizontalLayout_18.addWidget(self.comboBox_com)
        self.pushButton_com = QtGui.QPushButton(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.pushButton_com.setFont(font)
        self.pushButton_com.setObjectName(_fromUtf8("pushButton_com"))
        self.horizontalLayout_18.addWidget(self.pushButton_com)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.pushButton_collect = QtGui.QPushButton(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        self.pushButton_collect.setFont(font)
        self.pushButton_collect.setObjectName(_fromUtf8("pushButton_collect"))
        self.horizontalLayout_19.addWidget(self.pushButton_collect)
        self.pushButton_cleandata = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_cleandata.setObjectName(_fromUtf8("pushButton_cleandata"))
        self.horizontalLayout_19.addWidget(self.pushButton_cleandata)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.dockWidget.setWidget(self.dockWidgetContents)
        Window.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(Window)
        self.dockWidget_2.setMinimumSize(QtCore.QSize(202, 150))
        self.dockWidget_2.setMaximumSize(QtCore.QSize(524287, 524287))
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textBrowser = QtGui.QTextBrowser(self.dockWidgetContents_2)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 30))
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        Window.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.dockWidget_3 = QtGui.QDockWidget(Window)
        self.dockWidget_3.setMaximumSize(QtCore.QSize(524287, 160))
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_light = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_light.setObjectName(_fromUtf8("label_light"))
        self.horizontalLayout.addWidget(self.label_light)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_status2 = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_status2.setObjectName(_fromUtf8("label_status2"))
        self.horizontalLayout_4.addWidget(self.label_status2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_status = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.horizontalLayout_2.addWidget(self.label_status)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_angle = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_angle.setObjectName(_fromUtf8("label_angle"))
        self.horizontalLayout_3.addWidget(self.label_angle)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.label_status3 = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_status3.setObjectName(_fromUtf8("label_status3"))
        self.horizontalLayout_5.addWidget(self.label_status3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        Window.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)
        self.action_exit = QtGui.QAction(Window)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.action_exit.setFont(font)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_save = QtGui.QAction(Window)
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.action_open = QtGui.QAction(Window)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_show = QtGui.QAction(Window)
        self.action_show.setObjectName(_fromUtf8("action_show"))
        self.action_reset = QtGui.QAction(Window)
        self.action_reset.setObjectName(_fromUtf8("action_reset"))
        self.action_hide = QtGui.QAction(Window)
        self.action_hide.setObjectName(_fromUtf8("action_hide"))
        self.action_show2 = QtGui.QAction(Window)
        self.action_show2.setObjectName(_fromUtf8("action_show2"))
        self.action_hide2 = QtGui.QAction(Window)
        self.action_hide2.setObjectName(_fromUtf8("action_hide2"))
        self.action_show3 = QtGui.QAction(Window)
        self.action_show3.setObjectName(_fromUtf8("action_show3"))
        self.action_hide3 = QtGui.QAction(Window)
        self.action_hide3.setObjectName(_fromUtf8("action_hide3"))
        self.about_qt = QtGui.QAction(Window)
        self.about_qt.setObjectName(_fromUtf8("about_qt"))
        self.action_car = QtGui.QAction(Window)
        self.action_car.setObjectName(_fromUtf8("action_car"))
        self.action_sd_open = QtGui.QAction(Window)
        self.action_sd_open.setObjectName(_fromUtf8("action_sd_open"))
        self.menuMenu.addAction(self.action_open)
        self.menuMenu.addAction(self.action_sd_open)
        self.menuMenu.addAction(self.action_save)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.action_exit)
        self.menu.addAction(self.action_show)
        self.menu.addAction(self.action_hide)
        self.menu.addSeparator()
        self.menu.addAction(self.action_show2)
        self.menu.addAction(self.action_hide2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_show3)
        self.menu.addAction(self.action_hide3)
        self.about_Menu.addAction(self.about_qt)
        self.setting.addAction(self.action_car)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.setting.menuAction())
        self.menubar.addAction(self.about_Menu.menuAction())

        self.retranslateUi(Window)
        QtCore.QObject.connect(self.action_exit, QtCore.SIGNAL(_fromUtf8("triggered()")), Window.close)
        QtCore.QObject.connect(self.action_show, QtCore.SIGNAL(_fromUtf8("triggered()")), self.dockWidget.show)
        QtCore.QObject.connect(self.action_hide, QtCore.SIGNAL(_fromUtf8("triggered()")), self.dockWidget.hide)
        QtCore.QObject.connect(self.action_show2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.dockWidget_2.show)
        QtCore.QObject.connect(self.action_hide2, QtCore.SIGNAL(_fromUtf8("triggered()")), self.dockWidget_2.hide)
        QtCore.QObject.connect(self.action_hide3, QtCore.SIGNAL(_fromUtf8("triggered()")), self.dockWidget_3.hide)
        QtCore.QObject.connect(self.action_show3, QtCore.SIGNAL(_fromUtf8("triggered()")), self.dockWidget_3.show)
        QtCore.QObject.connect(self.toolButton_setting, QtCore.SIGNAL(_fromUtf8("clicked()")), self.action_car.trigger)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        Window.setWindowTitle(_translate("Window", "小车助手@lvniqi", None))
        self.lineEdit.setText(_translate("Window", "Type an expression and press Enter!", None))
        self.toolButton_setting.setText(_translate("Window", "设置...", None))
        self.menuMenu.setTitle(_translate("Window", "文件", None))
        self.menu.setTitle(_translate("Window", "边栏", None))
        self.about_Menu.setTitle(_translate("Window", "关于", None))
        self.setting.setTitle(_translate("Window", "设置", None))
        self.dockWidget.setWindowTitle(_translate("Window", "采集设置", None))
        self.label32_11.setText(_translate("Window", "波特率", None))
        self.comboBox_baudrate.setItemText(0, _translate("Window", "115200", None))
        self.comboBox_baudrate.setItemText(1, _translate("Window", "57600", None))
        self.comboBox_baudrate.setItemText(2, _translate("Window", "19200", None))
        self.comboBox_baudrate.setItemText(3, _translate("Window", "9600", None))
        self.checkBox_y.setText(_translate("Window", "全自动调节", None))
        self.checkBox_x.setText(_translate("Window", "X轴跟踪", None))
        self.label_242.setText(_translate("Window", "串口", None))
        self.pushButton_com.setText(_translate("Window", "扫描", None))
        self.pushButton_collect.setText(_translate("Window", "开始采集", None))
        self.pushButton_cleandata.setText(_translate("Window", "清空数据", None))
        self.dockWidget_2.setWindowTitle(_translate("Window", "系统消息", None))
        self.dockWidget_3.setWindowTitle(_translate("Window", "状态", None))
        self.label.setText(_translate("Window", "亮度", None))
        self.label_light.setText(_translate("Window", "000", None))
        self.label_3.setText(_translate("Window", "状态2", None))
        self.label_status2.setText(_translate("Window", "未知", None))
        self.label_4.setText(_translate("Window", "状态1", None))
        self.label_status.setText(_translate("Window", "未知", None))
        self.label_2.setText(_translate("Window", "打角", None))
        self.label_angle.setText(_translate("Window", "000", None))
        self.label_5.setText(_translate("Window", "状态3", None))
        self.label_status3.setText(_translate("Window", "未知", None))
        self.action_exit.setText(_translate("Window", "退出", None))
        self.action_exit.setShortcut(_translate("Window", "Ctrl+Q", None))
        self.action_save.setText(_translate("Window", "保存", None))
        self.action_save.setShortcut(_translate("Window", "Ctrl+S", None))
        self.action_open.setText(_translate("Window", "打开", None))
        self.action_open.setShortcut(_translate("Window", "Ctrl+O", None))
        self.action_show.setText(_translate("Window", "显示采集设置", None))
        self.action_reset.setText(_translate("Window", "重置", None))
        self.action_hide.setText(_translate("Window", "隐藏采集设置", None))
        self.action_show2.setText(_translate("Window", "显示系统消息", None))
        self.action_hide2.setText(_translate("Window", "隐藏系统消息", None))
        self.action_show3.setText(_translate("Window", "显示状态", None))
        self.action_hide3.setText(_translate("Window", "隐藏状态", None))
        self.about_qt.setText(_translate("Window", "关于QT", None))
        self.action_car.setText(_translate("Window", "小车设置", None))
        self.action_sd_open.setText(_translate("Window", "导入SD卡文件", None))
        self.action_sd_open.setShortcut(_translate("Window", "Ctrl+Alt+O", None))

