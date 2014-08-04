# -*- coding: utf-8 -*-
from array import array
from os import getcwdu

from Uart import Uart
from Uart import List2Str
#设定utf-8编码
import sys
from PyQt4.uic.Compiler.qtproxies import QtCore, QtGui
from msilib.schema import SelfReg

import sys, os


from serial.serialwin32 import SerialException

#设置脚本地址 
#abspath = os.path.dirname(__file__)
#sys.path.append(abspath) 
#os.chdir(abspath) 

#重设utf-8编码
sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('UTF-8')
sys.getdefaultencoding()


#图形模块pyqt4
from PyQt4 import QtGui,QtCore,Qwt5
from PyQt4.QtCore import Qt

#数学模块
from math import sin, cos
import numpy as np
#时间中断
from time import sleep
#绘图模块
from guiqwt.plot import PlotManager, CurvePlot
from guiqwt.builder import make as guiqwt_make
import thread
#主窗口
from mainwindow_ui import Ui_Window
from widget import Widget_Show as review_widget
from setting import Widget_Show as setting_widget
from show_realdata import Widget_Show as show_realdata_widget
#文件永久化
import cPickle
#显示数据
PLOT_DEFINE = ([u"CCD_1中间值",u'CCD_2中间值',u'CCD_3中间值',u"打角/100",u"CCD_1状态",u"CCD_2状态"],)
COLORS = ("#00aaff", "red",'orange','white','blue')

DT = 0.001

def get_peak_data(x, y, x0, x1, n, rate):
    if len(x) == 0:
        return [0], [0]
        
    x = np.frombuffer(x)
    y = np.frombuffer(y)
    index0 = int(x0*rate)
    index1 = int(x1*rate)
    step = (index1 - index0) // n
    if step == 0:
        step = 1
    index1 += 2 * step
    if index0 < 0: 
        index0 = 0
    if index1 > len(x) - 1:
        index1 = len(x) - 1
    x = x[index0:index1+1]
    
    y = y[index0:index1+1]
    y = y[:len(y)//step*step]
    yy = y.reshape(-1, step)
    index = np.c_[np.argmin(yy, axis=1), np.argmax(yy, axis=1)]
    index.sort(axis=1)
    index += np.arange(0, len(y), step).reshape(-1, 1)
    index = index.reshape(-1)
    return x[index], y[index]

#新建一个图表
def Plot_Start_New(widget,PLOT_DEFINE,COLORS,x1,x2,y1,y2):
    newmanager = PlotManager(widget)
    newplots = []
    newcurves = {}
    for name in PLOT_DEFINE:
            plot = CurvePlot()
            #设置图表颜色
            plot.setStyleSheet('''QWidget{   
                                                                border: 1px solid #32435E;   
                                                                border-radius: 3px;   
                                                                font-size:11pt;   
                                                                color:white;   
                                                                font-family:"Microsoft YaHei UI";  
                                                                /* padding: 0 8px; */  
                                                                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   
                                                                                             stop: 0 #080B10,   
                                                                                             stop: 1.0 #212C3F);   
                                                                selection-background-color: #0A246A;   
                                                            } '''  
                                         )
            plot.axisScaleDraw(CurvePlot.Y_LEFT).setMinimumExtent(20)
            newplots.append(plot)
            newmanager.add_plot(plot)
            plot.plot_id = id(plot)
            for curve_color, curve_name in map(None,COLORS,name):
                if  u"状态" in curve_name or  u"打角/100" in curve_name :
                    newcurves[curve_name] = guiqwt_make.curve([0], [0],markerfacecolor = 'black', markeredgecolor=curve_color, title=curve_name,marker = 'Diamond',linestyle = 'NoPen',markersize = 6)
                else:    
                    newcurves[curve_name] = guiqwt_make.curve([0], [0], color=curve_color, title=curve_name)
                
                plot.add_item(newcurves[curve_name])
            #设置X轴y轴
            plot.set_axis_limits(newcurves[curve_name].yAxis(),y1,y2)
            plot.set_axis_limits(newcurves[curve_name].xAxis(),x1,x2)
            plot.add_item(guiqwt_make.legend("BL"))
            
    
    newmanager.register_standard_tools()
    newmanager.get_default_tool().activate()
    return (newmanager,newplots,newcurves)
QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))  

def Set_Widget_Ui(Form):
    Form.setStyleSheet(u"*{   \n"
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
"     border: 0px solid #32435E;   \n"
"     position: absolute;   \n"
"     left: -0.1em;   \n"
"}   \n"
"QTabWidget#MainTabWidget::tab-bar {   \n"
"     left: -3px; /* move to the right by 5px */  \n"
"}   \n"
"QTabWidget#MainTabWidget QTabBar::tab {   \n"
"     height: 14ex;   \n"
"     width: 14ex;   \n"
"}   \n"
"QTabBar::tab {   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #292F31, stop: 1 #0C131E);   \n"
"}   \n"
"QTabBar::tab:selected{   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #113845,  stop: 1.0 #15A8FF);   \n"
"}   \n"
"QTabBar::tab:hover {   \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,   \n"
"                                 stop: 0 #113845,  stop: 1.0 #0E6F80);   \n"
"}   \n"
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
"} ")
#线程 采集数据
class GettingUartData_Thread(QtCore.QThread):    
    def __init__(self,uart,parent=None):
        super(self.__class__, self).__init__(parent)
        self.stoped = False
        self.mutex = QtCore.QMutex()
        self.uart = uart
        self.getwrong_message = None
        
    def run(self):
        ccddata  = None
        with QtCore.QMutexLocker(self.mutex):
            self.stoped = False
        
        try:
            self.uart.open()
        except SerialException,e:
            self.getwrong_message = e
            self.emit(QtCore.SIGNAL("UartData"), ccddata,self.getwrong_message)
        while True:
            if self.stoped  == True:
                return
            try:
                ccddata =   self.uart.GetData()
            except SerialException,e :
                self.getwrong_message = e
                self.emit(QtCore.SIGNAL("UartData"), ccddata,self.getwrong_message)
                
            self.emit(QtCore.SIGNAL("UartData"), ccddata,self.getwrong_message)
        
    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.uart.close()
            self.getwrong_message = None
            self.stoped = True
    
    def isStop(self):
        with QtCore.QMutexLocker(self.mutex):
            return self.stoped
        
#主窗口
class Windows(QtGui.QMainWindow,Ui_Window):
    def __init__(self,parent=None):
    
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) # Ui_Form.setupUi
        '''
        #最小化&关闭
        self.minibutton = QtGui.QToolButton(self)
        self.minibutton.setGeometry(self.width()-45,5,20,20)
        self.closebutton = QtGui.QToolButton(self)
        self.closebutton.setGeometry(self.width()-25,5,20,20)
        '''

        #加入设置窗口
        #setting_ui  = UI_Settings()
        #self.setting = QtGui.QWidget()
        #setting_ui.setupUi(self.setting)
        
        #新建窗口
        self.ShowData = []
        self.SD_data = []
        #打开的窗体
        self.open_widget = []
        #显示文件的路径
        self.ShowDataFileName = []
        #设置lineedit
        self.lineEdit.selectAll()
        self.lineEdit.setFocus()
        #curves曲线 名字:曲线
        self.curves = {}
        #图像管理器
        self.manager = PlotManager(self)
        #data 数据 double型 t
        self.data = {u"t":array("d")}
        for name in sum(PLOT_DEFINE, []):
            self.data[name] = array("d")
        self.data['tn'] = 0
        self.data['xmax'] = 0
        self.data['xmin']  = 0
        self.progressbar = []
        
        #车辆设置数据
        
        self.data['angle_p'] =  0
        self.data['angle_i'] = 0
        self.data['angle_d'] = 0
        self.data['speed_up_p'] = 0
        self.data['speed_up_i'] = 0
        self.data['speed_up_d'] = 0
        self.data['speed_curve'] = 0
        self.data['speed_straight'] = 0
        self.data['k_ccd'] = 0
        self.data['k_different'] = 0
        self.data['light_time'] = 0
        self.data['different_len'] = 0
        self.data['different_size'] = 0
        #主图表
        self.plots = []
        #副图标
        self.plots_extra = []
        #图表设置
        (self.manager,self.plots,self.curves) = Plot_Start_New(self,PLOT_DEFINE,COLORS,0,5,-5,200)
        for plot in self.plots:
            self.left_layout1.addWidget(plot)
        #self.manager.synchronize_axis(CurvePlot.X_BOTTOM, self.manager.plots.keys())
        
        
        #添加设置窗口
        self.setting_widget = setting_widget(self)
        self.open_widget.append(self.setting_widget)
        #连接 
        self.connect(self.pushButton_collect, QtCore.SIGNAL("clicked()"), self.AddingData_Start)
        self.connect(self.action_open,QtCore.SIGNAL("triggered()"),self.OpenFile)
        self.connect(self.action_save,QtCore.SIGNAL("triggered()"),self.SaveFile)
        self.connect(self.lineEdit,QtCore.SIGNAL("returnPressed()"),lambda:self.Line2Brower(self.lineEdit))
        #self.connect(self.lineEdit_2,QtCore.SIGNAL("returnPressed()"),lambda:self.Line2Brower(self.lineEdit_2))
        self.connect(self.checkBox_x, QtCore.SIGNAL("clicked()"), self.Flx)
        self.connect(self.checkBox_y, QtCore.SIGNAL("clicked()"), self.Auto)
        #self.connect(self.pushButton_car_setting,QtCore.SIGNAL("clicked()"),self.Settings)
        self.connect(self.pushButton_com,QtCore.SIGNAL("clicked()"), self.ReScanUart)
        self.connect(self.about_qt,QtCore.SIGNAL("triggered()"), lambda:QtGui.QMessageBox.aboutQt(self))
        self.connect(self.action_car,QtCore.SIGNAL("triggered()"),self.setting_widget.show)
        self.connect(self.pushButton_cleandata, QtCore.SIGNAL("clicked()"),self.CleanData)
        #self.connect(self.pushButton_run,QtCore.SIGNAL("clicked()"),self.CarStartRun)
#------------------------------------------------------小车设置连接----------------------------------------------------------------------------
    #    self.connect(self.setting_widget.pushButton_Stop, QtCore.SIGNAL("clicked()"),lambda :self.SetAngleP(20))
        self.connect(self.setting_widget.pushButton_Stop, QtCore.SIGNAL("clicked()"),self.CarStopRun)
        self.connect(self.setting_widget.apply, QtCore.SIGNAL("clicked()"),self.SettingApply)
        self.connect(self.setting_widget.pushButton_Start, QtCore.SIGNAL("clicked()"),self.CarStartRun)       
        #进度条
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Warning, "", "", QtGui.QMessageBox.NoButton,parent = self )
        msgBox.setStandardButtons( QtGui.QMessageBox.NoButton )
        l = msgBox.layout()
        self.progressbar.append(msgBox)
        l.itemAtPosition( l.rowCount() - 1, 0 ).widget().hide()
        progress = QtGui.QProgressBar()
        self.progressbar.append(progress)
        progress.setValue(0)
        l.addWidget(progress,l.rowCount(), 0, 1, l.columnCount(), Qt.AlignCenter )
        
#--------------------------------------------------添加图像窗口-------------------------------------------------------------------------------
        self.ccd_realshow = []
        t = 0
        t_past = 0
        ccd_realshow = show_realdata_widget()
        
        data = {}
        
        data[u't'] = 0
        data[u't_past'] = 0
        temp_d = array('d')
        for i in range(128):
                temp_d.append(0)
                
        ccd_realshow.setWindowTitle(u"图像显示")
        ccd_realshow.setGeometry(200,200,400,400)
        
        for x in range(3):
            (memger,plots,curves) = Plot_Start_New(
                                                                                ccd_realshow,
                                                                                (
                                                                                     (u'CCD图像%d'%(x+1),
                                                                                      u'CCD图像%d左'%(x+1),
                                                                                      u'CCD图像%d中'%(x+1),
                                                                                      u'CCD图像%d右'%(x+1),
                                                                                     ),
                                                                                 ),
                                                                                ('white','red','green','blue'),0,128,0,255
                                                                              )

            temp_data = data.copy()
            temp_data[u'CCD图像%d'%(x+1)] = temp_d[:]
            temp_data[u'CCD图像%d左'%(x+1)] = temp_d[:]
            temp_data[u'CCD图像%d中'%(x+1)] = temp_d[:]
            temp_data[u'CCD图像%d右'%(x+1)] = temp_d[:]
            
            self.ccd_realshow.append([u'CCD图像%d'%(x+1),ccd_realshow,plots,curves,temp_data])
            for plot in plots: 
                ccd_realshow.gridLayout.addWidget(plot)
                
        for x in self.ccd_realshow:
            for y in x[2]:     
                y.hide()
                
        
        ccd_realshow.checkBox_ccd1.setChecked(0)
        ccd_realshow.checkBox_ccd2.setChecked(0)
        ccd_realshow.checkBox_ccd3.setChecked(0)
        self.connect(ccd_realshow.checkBox_ccd1, QtCore.SIGNAL("stateChanged(int)"),lambda x: self.Ccd_Realshow_Setting(0,x))
        self.connect(ccd_realshow.checkBox_ccd2, QtCore.SIGNAL("stateChanged(int)"),lambda x: self.Ccd_Realshow_Setting(1,x))
        self.connect(ccd_realshow.checkBox_ccd3, QtCore.SIGNAL("stateChanged(int)"),lambda x: self.Ccd_Realshow_Setting(2,x))
        self.connect(self.setting_widget.checkBox_ccd1,QtCore.SIGNAL("stateChanged(int)"),ccd_realshow.checkBox_ccd1.setChecked)
        self.connect(self.setting_widget.checkBox_ccd2,QtCore.SIGNAL("stateChanged(int)"),ccd_realshow.checkBox_ccd2.setChecked)
        self.connect(self.setting_widget.checkBox_ccd3,QtCore.SIGNAL("stateChanged(int)"),ccd_realshow.checkBox_ccd3.setChecked)
        self.connect(ccd_realshow.checkBox_ccd1,QtCore.SIGNAL("stateChanged(int)"),self.setting_widget.checkBox_ccd1.setChecked)
        self.connect(ccd_realshow.checkBox_ccd2,QtCore.SIGNAL("stateChanged(int)"),self.setting_widget.checkBox_ccd2.setChecked)
        self.connect(ccd_realshow.checkBox_ccd3,QtCore.SIGNAL("stateChanged(int)"),self.setting_widget.checkBox_ccd3.setChecked)
        self.connect(self.setting_widget.checkBox_ccd3,QtCore.SIGNAL("stateChanged(int)"),ccd_realshow.checkBox_ccd3.setChecked)
        self.connect(self.setting_widget.pushButton_real_data_Show,QtCore.SIGNAL("clicked()"),ccd_realshow.show)
        self.connect(ccd_realshow.pushButton_single, QtCore.SIGNAL("clicked()"),self.SdRunSingle)
        self.connect(ccd_realshow.pushButton_back, QtCore.SIGNAL("clicked()"),self.SdRunSingleBack)
#--------------------------------------------------添加图像窗口-------------------------------------------------------------------------------
        self.connect(self.action_sd_open,QtCore.SIGNAL("triggered()"),self.OpenSDFile)
        
        #定时显示
        self.startTimer(40)
#--------------------------------------------------添加图像窗口设置-------------------------------------------------------------------------------        
    def Ccd_Realshow_Setting(self,num,i):
        data = self.ccd_realshow[int(num)][2]
        if not i:
            for x in data:
                #self.CarStopShowCCD1();
                x.hide()
        else:
            for x in data:
                #self.CarShowCCD1();
                x.show()
                
    def CleanData(self):
        self.data = {u"t":array("d")}
        for name in sum(PLOT_DEFINE, []):
            self.data[name] = array("d")
        self.data['tn'] = 0
        self.data['xmax'] = 0
        self.data['xmin']  = 0
        for plot in self.plots:
            plot.replot()
        
        #车辆设置数据
        self.data['angle_p'] =  0
        self.data['angle_i'] = 0
        self.data['angle_d'] = 0
        self.data['speed_up_p'] = 0
        self.data['speed_up_i'] = 0
        self.data['speed_up_d'] = 0
        self.data['speed_curve'] = 0
        self.data['speed_straight'] = 0
        self.data['k_ccd'] = 0
        self.data['k_different'] = 0
        self.data['light_time'] = 0
        self.data['different_len'] = 0
        self.data['different_size'] = 0
        self.textBrowser.clear()
        self.timerEvent(None)
        
    def show(self):
        QtGui.QMainWindow.show(self)
        #加入串口
        self.uart = Uart()
        self.ReScanUart()
        
        
    def Line2Brower(self,lineEdit):
        text = unicode(lineEdit.text()).upper()
        #打开收集
        if text in  (u'COLLECT',u'CLT'):
            self.AddingData_Start()
        #退出
        elif text in (u'EXIT',u'QUIT'):
            self.close()
        #跟踪x
        elif text in (u'FLX',u'follow x'):
            if  self.checkBox_x.isChecked():
                self.checkBox_x.setChecked(0)
            else:
                self.checkBox_x.setChecked(1)
            self.Flx()
        #自动模式  
        elif text in (u'AUTO',):
            if  self.checkBox_y.isChecked():
                self.checkBox_y.setChecked(0)
            else:
                self.checkBox_y.setChecked(1)
            self.Auto()
        #清除
        elif text in (u'CLEAR',):
            self.textBrowser.clear()
        #出错
        else:
            try:
                
                self.textBrowser.append("{0} = <b>{1}</b>".format(text,
                                    eval(text)))
            except:
                self.textBrowser.append("<font color=red>{0} is invalid!</font>"
                                    .format(text))
    #打开follow x
    def Flx(self):
        if  self.checkBox_x.isChecked():
            self.textBrowser.append(u"<font color=green><b>x跟踪</b>  已 <b>开启</b>!</font>")
        else:
            self.textBrowser.append(u"<font color=green><b>x跟踪</b>  已 <b>关闭</b>!</font>")
    #自动模式         
    def Auto(self):
        if  self.checkBox_y.isChecked():
            self.textBrowser.append(u"<font color=green><b>自动跟踪</b>  已 <b>开启</b>!</font>")
        else:
            self.textBrowser.append(u"<font color=green><b>自动跟踪</b>  已 <b>关闭</b>!</font>")

    #打开文件
    def OpenFile(self):
        filename = QtGui.QFileDialog.getOpenFileNames(
                                                     self, caption=u'打开文件',
                                                     directory =  os.getcwd(),
                                                     filter = u"数据库文件(*.db);;All files (*.*)",
                                                     selectedFilter = u"数据库文件(*.db)"
                                                     )
        
        for x in  filename:
            
            if x in self.ShowDataFileName:
                id2 = self.ShowDataFileName.index(x)
                self.ShowData[id2][0].show()
                
            else:
                
                try:
                    data = cPickle.load(open(x,'r'))
                    
                    #图像初始化
                    
                    
                except cPickle.UnpicklingError :
                    QtGui.QMessageBox.warning(self,u"文件出错",u"文件出错!请检查！")
                    continue
                
                #添加菜单栏
                a = review_widget()
                if not self.ShowData:
                    self.showdata_menu = self.menubar.addMenu(u'已打开文件')
                action = self.showdata_menu.addAction(x)
                self.connect(action,QtCore.SIGNAL("triggered()"),a.show)
                a.setWindowTitle(x)
                (manager,plots,curves) = Plot_Start_New(a,PLOT_DEFINE,COLORS,0,5,-5,200)
                plot = plots[0]
                for key, curve in curves.iteritems():
                    xdata = data["t"]
                    ydata = data[key]
                    x, y = get_peak_data(xdata, ydata, 0, 12, 1000, 1/DT)
                    curve.set_data(x, y)
                    plot.replot()
                #完成后设置    
                a.gridLayout.addWidget(plot)
                #图表 文件
                self.ShowData.append((a,plot,curves,data))
                
                #设置窗口名
                self.ShowDataFileName.append(x)
                
                #设置 车辆设置
                '''
                a.label_angle_p.setText(str(data['angle_p']))
                a.label_angle_i.setText(str(data['angle_i']))
                a.label_angle_d.setText(str(data['angle_d']))
                a.label_speed_up_p.setText(str(data['speed_up_p']))
                a.label_speed_up_i.setText(str(data['speed_up_i']))
                a.label_spped_up_d.setText(str(data['speed_up_d']))
                a.label_speed_curve.setText(str(data['speed_curve']))
                a.label_speed_straight.setText(str(data['speed_straight']))
                a.label_k_ccd.setText(str(data['k_ccd']))
                a.label_k_different.setText(str(data['k_different']))
                a.label_light_time.setText(str(data['light_time']))
                a.label_different_len.setText(str(data['different_len']))
                a.label_different_size.setText(str(data['different_size']))
                '''
                a.show()
    #打开SD文件
    def OpenSDFile(self):
        self.SD_data = []
        filename = QtGui.QFileDialog.getOpenFileName(
                                                     self, caption=u'打开文件',
                                                     directory =  os.getcwd(),
                                                     filter = u"数据库文件(*.txt);;All files (*.*)",
                                                     selectedFilter = u"数据库文件(*.txt)"
                                                     )
        file1 = open(filename,'r')
        self.SD_data.append(file1)
        self.SD_data.append(0)
        ccd_realshow = self.ccd_realshow[0][1]
        ccd_realshow.checkBox_ccd1.setChecked(1)
        ccd_realshow.checkBox_ccd2.setChecked(1)
        ccd_realshow.checkBox_ccd3.setChecked(1)
        ccd_realshow.show()
    #运行SD 单步
    def SdRunSingle(self):
        if self.SD_data:
            file1 = self.SD_data[0]
            print 'len',len(self.SD_data),' ',self.SD_data[1]+2
            if self.SD_data[1] +2 == len(self.SD_data):
                for x in range(4):
                    temp = eval(file1.readline())
                    if temp:
                        self.SD_data[1] += 1
                        self.SD_data.append(temp)
                        self.AddingData(temp,None)
            else:
                for x in range(4):
                    temp = self.SD_data[ self.SD_data[1] +2 ]
                    self.SD_data[1] += 1
                    self.AddingData(temp,None)
                
    #单步倒退
    def SdRunSingleBack(self):
        print 'len',len(self.SD_data),' ',self.SD_data[1]+2
        if self.SD_data[1] > 0:
            for x in range(4):
                self.SD_data[1] -= 1
                temp = self.SD_data[ self.SD_data[1] +2 ]
                self.AddingData(temp,None)
            
    #保存文件
    def SaveFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(
                                                     self, caption=u'保存文件',
                                                     directory =  os.getcwd(),
                                                     filter = u"数据库文件(*.db);;All files (*.*)",
                                                     selectedFilter = u"数据库文件(*.db)"
                                                     )
        if filename:
            file1 = open(filename,'w')
            cPickle.dump(self.data, file1)
            file1.close()
        
        
    #开始采集
    def AddingData_Start(self):
        string =   self.pushButton_collect.text( )
        
        if string == u'开始采集':
            self.ReScanUart()
            if not self.uart.freeport:
                pass
                
            else:
                self.pushButton_collect.setText(u'关闭采集')
                #打开端口
                for x in self.uart.freeport:
                    if str(self.comboBox_com.currentText()) in x:
                        self.uart.setPort(x[0])
                self.uart.setBaudrate(self.comboBox_baudrate.currentText())
                #清空
                #self.CleanData()
                #串口数据线程
                self.adddata  = GettingUartData_Thread(self.uart)
                #采集串口数据
                self.connect(self.adddata, QtCore.SIGNAL("UartData"), self.AddingData)
                self.adddata.start()
                self.textBrowser.append(u"<font color=green><b>采集</b>  已 <b>开始</b>!</font>")
                #禁止修改
                self.comboBox_com.setDisabled(True)
                self.comboBox_baudrate.setDisabled(True)
                
        else:
            
            #停止收集
            self.AddingData_Stop()
            
            self.textBrowser.append(u"<font color=green><b>采集</b>  已 <b>停止</b>!</font>")
            self.pushButton_collect.setText(u'开始采集')
                
            #打开修改
            self.comboBox_com.setDisabled(False)
            self.comboBox_baudrate.setDisabled(False)
    #停止采集
    def AddingData_Stop(self):
        self.ProgressBar_Open("请稍候","串口关闭中...")
        self.adddata.stop()
        for x in range(100):
                self.ProgressBar_SetValue(x)
                sleep(0.001)
        if  self.adddata.isStop():
            self.disconnect(self.adddata, QtCore.SIGNAL("UartData"),
                                self.AddingData)
        self.adddata.stop()
        self.adddata.quit()
        self.adddata.wait()
        self.adddata.deleteLater()
        self.ProgressBar_SetValue(100)
        self.ProgressBar_Stop()
    
    #得到数据
    def AddingData(self,data,message):
        #图像数据
        ccddata =  data
        if message:
            self.AddingData_Start()
            print message
            QtGui.QMessageBox.warning(self,u"串口错误",str(message))
            self.ProgressBar_Open("请稍候","串口重置中...")
            for x in range(100):
                self.ProgressBar_SetValue(x)
                sleep(0.05)
            self.ProgressBar_Stop()
            self.ReScanUart()
        elif ccddata  != None:
            datalen =  len(ccddata)
            if datalen == 129:
                data_raw = array('d')
                num = ccddata[0]
                if num in range(1,4):
                
                    ccddata.pop(0)
                    data_raw.fromlist(ccddata)
                    
                    for x in self.ccd_realshow:
                        if 'CCD图像%d'%num in x:
                            data = x[4]
                            data['t'] = data['t'] +1
                            data[u'CCD图像%d'%num] = data_raw
                else:
                    print  ccddata
                
            elif  datalen == 14:
                for x in range(3):
                    ccd_realshow = self.ccd_realshow[x]
                    temp = []
                    temp.append(ccddata[0])
                    temp.append(ccddata[4])
                    temp.append(ccddata[8])
                    temp.append(ccddata[3])
                    temp.append(ccddata[7])
                    temp.append(ccddata[13])
                    self.AddingData(temp,None)
                    for y in range(128):
                        ccd_realshow[4][u'CCD图像%d左'%(x+1)][y] = 0
                    ccd_realshow[4][u'CCD图像%d左'%(x+1)][ccddata[x*4]] = 255
                    for y in range(128):
                        ccd_realshow[4][u'CCD图像%d中'%(x+1)][y] = 0
                    ccd_realshow[4][u'CCD图像%d中'%(x+1)][ccddata[x*4+1]] = 255
                    for y in range(128):
                        ccd_realshow[4][u'CCD图像%d右'%(x+1)][y] = 0
                    ccd_realshow[4][u'CCD图像%d右'%(x+1)][ccddata[x*4+2]] = 255
                    
            elif len(ccddata) == 7:
                t = self.data['tn']
                
                self.data[u"t"].append(t)
                self.data[u"CCD_1中间值"].append(ccddata[0])
                self.data[u"CCD_2中间值"].append(ccddata[1])
                self.data[u"CCD_3中间值"].append(ccddata[2])
                #self.data[u"打角/100"].append(ccddata[2])
                self.data[u"CCD_1状态"].append(ccddata[3]*30)
                self.data[u"CCD_2状态"].append(ccddata[4]*30)
                light = "%d"%ccddata[5]
                angle =  "%d"%ccddata[2]
                status =  ccddata[3]
                status2 = ccddata[4]
                status3 = ccddata[6]
                
                if status != 3:
                    if status == 1:
                        status =u'找到两条线'
                    else:
                        status =u'找到一条线'
                    if self.data[u"CCD_1状态"][len(self.data[u"CCD_1状态"])-2] == 90:
                        self.textBrowser.append(u"<font color=green>{0} </font>"
                                                                .format(u"t =%.3f时 CCD_1找到线!中点:\t%d"%(t,ccddata[0]))
                                                                )
                        
                else:
                    status =u'找不到线'
                    if self.data[u"CCD_1状态"][len(self.data[u"CCD_1状态"])-2] != 90:
                        self.textBrowser.append(u"<font color=red>{0} </font>"
                                                                .format(u"t =%.3f时 CCD_1找不到线!中点:\t%d"%(t,ccddata[0]))
                                                                )
                        
                if status2 != 3:
                    if status2 == 1:
                        status2 =u'找到两条线'
                    else:
                        status2 =u'找到一条线'
                    if self.data[u"CCD_2状态"][len(self.data[u"CCD_2状态"])-2] == 90:
                        self.textBrowser.append(u"<font color=green>{0} </font>"
                                                                .format(u"t =%.3f时 CCD_2找到线!中点:\t%d"%(t,ccddata[1]))
                                                                )
                        
                else:
                    status2 =u'找不到线'
                    if self.data[u"CCD_2状态"][len(self.data[u"CCD_2状态"])-2] != 90:
                        self.textBrowser.append(u"<font color=red>{0} </font>"
                                                                .format(u"t =%.3f时 CCD_2找不到线!中点:\t%d"%(t,ccddata[1]))
                                                                )
                if status3 != 3:
                    if status3 == 1:
                        status3 =u'找到两条线'
                    else:
                        status3 =u'找到一条线'
                    if self.data[u"CCD_2状态"][len(self.data[u"CCD_2状态"])-2] == 90:
                        self.textBrowser.append(u"<font color=green>{0} </font>"
                                                                .format(u"t =%.3f时 CCD_3找到线!中点:\t%d"%(t,ccddata[1]))
                                                                )
                        
                else:
                    status3 =u'找不到线'
                    if self.data[u"CCD_2状态"][len(self.data[u"CCD_2状态"])-2] != 90:
                        self.textBrowser.append(u"<font color=red>{0} </font>"
                                                                .format(u"t =%.3f时 CCD_3找不到线!中点:\t%d"%(t,ccddata[1]))
                                                                )
                        
                self.label_light.setText(light)
                self.label_angle.setText(angle)
                self.label_status.setText(status)
                self.label_status2.setText(status2)
                #时间线
                self.data['tn'] += DT
            else:
                print datalen
            '''
            #-----------------------------------------------------------
            t = self.data['tn']
            self.data[u"t"].append(t)
            self.data[u"左侧"].append(sin(t)*64+64)
            self.data[u"中间值"].append(sin(2*t)*64+64)
            self.data[u"右侧"].append(sin(3*t)*64+64)
            self.data[u"打角"].append(sin(4*t)*64+64)
            self.data[u"状态"].append(sin(5*t)*64+64)
            light = "%d"%(sin(2*t)*64+64)
            angle =  "%d"%(sin(3*t)*64+64)
            status =  "%d"%(sin(4*t)*64+64)
            if not int(t*(1/DT))%(1/DT/10):
                self.label_light.setText(light)
                self.label_angle.setText(angle)
                self.label_status.setText(status)
            sleep(0.01)
    		#时间线
            self.data['tn'] += DT
            #-----------------------------------------------------------
            '''
            
            

        
    #进度条
    def ProgressBar_Open(self,title,body):
        self.progressbar[0].setWindowTitle(unicode(str(title)))
        self.progressbar[0].setText(unicode(str(body)))
        self.progressbar[1].setValue(0)
        self.progressbar[0].show()
        
        
    def ProgressBar_SetValue(self,value):
        self.progressbar[1].setValue(value)
        
    def ProgressBar_Stop(self):
        self.progressbar[0].hide()
        self.progressbar[0].close()
    #重新扫描        
    def ReScanUart(self):
        now = self.comboBox_com.currentText()
        if self.uart.isOpen() :
            self.uart.close()
            
        self.uart.setBaudrate(self.comboBox_baudrate.currentText())
        self.comboBox_com.clear()
        
        if not self.uart.SetPortAuto():
            QtGui.QMessageBox.warning(self,u"找不到串口",u"找不到串口!\n请重新扫描！")
        else :
            for x in self.uart.freeport:
                #print x
                pass
            self.comboBox_com.addItems(map(lambda x:x[1],self.uart.freeport))
                
            if now in  map(lambda x:x[1],self.uart.freeport):
                self.comboBox_com.setCurrentIndex(self.comboBox_com.findText(now))
            
    #定时
    def timerEvent(self, event):
        
        #主图表
        if self.data["t"]:
            tt = self.data["tn"]
            xmin, xmax = self.plots[0].get_axis_limits('bottom')
            if self.checkBox_x.isChecked():
                xmin += tt - xmax
                xmax = tt
            if (xmax != self.data['xmax']) or (xmin != self.data['xmin']) or (tt <self.data['xmax']):
                self.data['xmax'] = xmax
                self.data['xmin'] = xmin
                for key, curve in self.curves.iteritems():
                    xdata = self.data["t"]
                    ydata = self.data[key]
                    x, y = get_peak_data(xdata, ydata, xmin, xmax, 500, 1/DT)
                    curve.set_data(x, y)
            
            for plot in self.plots:
                if self.checkBox_y.isChecked():
                    plot.do_autoscale()
                elif self.checkBox_x.isChecked():
                    plot.set_axis_limits("bottom", xmin, xmax)
                    plot.replot()
                else:
                    plot.replot()
            
        #其它图表
        for x in self.ShowData:
            plot = x[1]
            curves = x[2]
            data = x[3]
            if x[2]:
                tt = data["tn"]
                xmin, xmax = plot.get_axis_limits('bottom')
                if (xmax != data['xmax']) or (xmin != data['xmin']) or (tt <data['xmax']):
                    data['xmax'] = xmax
                    data['xmin'] = xmin
                    for key, curve in curves.iteritems():
                        xdata = data["t"]
                        
                        ydata = data[key]
                        x, y = get_peak_data(xdata, ydata, xmin, xmax, 1000, 1/DT)
                        curve.set_data(x, y)
                    plot.replot()
                    
        #ccd真实图像
        for x in self.ccd_realshow:
            plots = x[2]
            curves = x[3]
            data = x[4]
            for plot in plots:
                if data[u't'] != data[u't_past']:
                    data[u't_past'] = data[u't']
                    xmin, xmax = plot.get_axis_limits('bottom')
                    for key, curve in curves.iteritems():
                            xdata = array('d')
                            xdata.fromlist(range(128))
                            ydata = data[key]
                            (x, y) = get_peak_data(xdata, ydata, xmin, xmax, 1000, 1)
                            curve.set_data(xdata, ydata)
                    
                    plot.set_axis_limits(curve.xAxis(),0,128)
                    plot.set_axis_limits(curve.yAxis(),0,256)
                    plot.replot()
    
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            u"确认退出?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No, )
        if reply == QtGui.QMessageBox.Yes:
            for x in self.ccd_realshow:
                x[1].close()
            for x in self.open_widget:
                x.close()
            if self.uart.isOpen() :
                self.AddingData_Stop()
            for x in self.ShowData:
                x[1].close()
            event.accept()
        else:
            event.ignore()
#-----------------------------------------------------------------------------------------------------
    def CarGetReturn(self):
        data = []
        for x in range(3):
            self.ProgressBar_SetValue(20*(x+1))
            temp = self.uart.GetData()
            if temp:
                data.append(temp )
            
        for x in data:
            print x[:2]
            if x and  len(x) == 2:
                if List2Str(x) == 'OK':
                    return True
        return False
    
    def CarControl(self,command):
        if self.pushButton_collect.text( ) == u'关闭采集' :
            self.AddingData_Start()
        self.uart.open()
        command()
        self.uart.close()
        self.uart.open()
        if not self.CarGetReturn():
            QtGui.QMessageBox.warning(self,u"错误",u"控制错误！")
        self.uart.close()
            
    def CarStopRun(self):
        x = lambda  :self.uart.write('\nSTOP\n')
        self.CarControl(x)
            
    def CarStartRun(self):
        x = lambda  :self.uart.write('\nSTART\n')    
        self.CarControl(x)
        
    def SetAngleP(self,Kp):
        Kp = int(Kp)
        temp = [Kp,]
        Kp = List2Str(temp)
        x = lambda  :self.uart.write('\nSET_KP_ANGLE\n%s'%Kp)    
        self.CarControl(x)
    def SetAngleD(self,Kd):
        Kd = int(Kd)
        temp = [Kd,]
        Kd = List2Str(temp)
        x = lambda  :self.uart.write('\nSET_KD_ANGLE\n%s'%Kd)    
        self.CarControl(x)      
        
    def CarShowCCD1(self):
        x = lambda  :self.uart.write('\nCCD1_SEND\n')    
        self.CarControl(x)
    def CarStopShowCCD1(self):
        x = lambda  :self.uart.write('\nCCD1_STOP_SEND\n')    
        self.CarControl(x)
    def SettingApply(self):
        self.SetAngleP(20)
        self.SetAngleD(15)
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    widget = Windows()
    #widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #widget.showFullScreen()
    widget.show()
    sys.exit(app.exec_())
