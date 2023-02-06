"""
A simple player for VLC python bindings using PyQt5

update resource files:  
    - pyrcc5 -o resources.py resources.qrc

bundles a Python application and all its dependencies into a single package:
    - pyinstaller --onefile --add-data "SmartVideoPlayer.ico;." -i="SmartVideoPlayer.ico" -w SmartVideoPlayer.py

by Kai-Chun, Li
01/2023
"""

import platform
import time
import sys, os
try :
    import vlc
except :
    pass
try :
    import pafy
    show_url = True
except :
    show_url = False
import cv2 
from ctypes import CDLL
from resources import *
from pathlib import Path
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QInputDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, Qt, QTimer, QDir
from PyQt5.QtGui import QPalette, QColor, QKeyEvent

from Mediapipe.mediapipeDetector import MediapipeDetector


__appname__ = "Smart Video Player"
__version__ = "v1.0.0"
__app_ico__ = "SmartVideoPlayer.ico"
# Constants
VLC_WHITE = 16777215
CMD_OPTIONS = '--freetype-fontsize={} --freetype-color={}'
PERCENT_LABEL = '{}%'
POSITION_LABEL = '{} / {}'
SUB_SIZE_START_VALUE = 75
VOLUME_START_VALUE = 60

if getattr(sys, 'frozen', False):
    script_dir = Path(sys.executable).parents[0]
else :
    script_dir = Path(__file__).absolute().parents[0]
print("Project Path :", script_dir)

class StopWatch():
    def __init__(self, sec=10):
        self.timer = QtCore.QTimer()  # 初始化一个定时器
        self.timer.timeout.connect(self._operate)  # 计时结束调用operate()方法
        self.togger = False
        self.sec = sec
        self.num = 0
        self.track_label = "None"
        self.togger_label = "None"

    def _operate(self):
        """
        定时器定时时间到，操作处理
        """
        if (self.togger_label==self.track_label) :
            self.num += 1
            if (self.num >= self.sec):
                self.togger = True
        else :
            self.reset()

    def start(self):
        """
        计时开始
        """
        self.timer.start(1000)  # 设置计时间隔并启动

    def setlabel(self, track_label="None"):
        if self.track_label != track_label :
            self.reset()
            self.track_label = track_label

    def checklabel(self, track_label="None"):
        self.togger_label = track_label

    def reset(self):
        """
        复位
        """
        self.num = 0
        self.togger = False
        self.track_label = "None"
        self.togger_label = "None"

    def stop(self):
        """
        计时停止
        """
        self.timer.stop()  # 计时停止


class DetectorWorker(QtCore.QThread):
    sinVideoOut = QtCore.pyqtSignal(str, str)
    sinVolumeOut =  QtCore.pyqtSignal(int)
    sinAngleOut =  QtCore.pyqtSignal(int)

    def __init__(self, cameraNum=0, parent=None):
        super(DetectorWorker, self).__init__(parent)

        modelConfig = str(script_dir) + '/Mediapipe/face_inference.ini'
        MediapipeDetector.set_defaults(modelConfig)
        self.faceDetector =  MediapipeDetector()
        modelConfig = str(script_dir) + '/Mediapipe/hand_inference.ini'
        MediapipeDetector.set_defaults(modelConfig)
        self.handDetector =  MediapipeDetector()

        self.camCap = cv2.VideoCapture(cameraNum,cv2.CAP_DSHOW)
        if (self.camCap.isOpened() is True):
            print("\n==========Camera=========")
            print("Intelligent Control Open.")
            print("Camera ID:", cameraNum)
            print("=========================\n")
            self.working = True
        else :
            QMessageBox.warning(None, 'Warning', "No Found camera device. can't use it.")
            print("\n==========Camera=========")
            print("Camera ID:", cameraNum, "No Found it.")
            print("=========================\n")
            self.working = False

        self.is_display = False

        # 设置工作状态
        self.volume_status = False
        self.face_status = "unknown"
        self.gesture_status = "unknown"
        self.volume_list = []
        self.angle_list = []

        self.face_timer = StopWatch(sec=2)
        self.face_timer.start()
        self.gesture_timer = StopWatch(sec=1)
        self.gesture_timer.start()

    def exit(self):
        print("\n==========Camera=========")
        print("Intelligent Control Close.")
        print("=========================\n")
        # 线程状态改变与线程终止
        self.working = False
        time.sleep(1)
        cv2.destroyAllWindows()
        self.camCap.release()
        self.quit()
        self.wait()

    def _average(self, l): 
        avg = sum(l) / len(l) 
        return int(avg)

    def run(self):
        while self.working:
            if (self.camCap) :
                success, camImage = self.camCap.read()
                self.face_status = "unknown"
                self.gesture_status = "unknown"
                if success:
                    self.faceDetector.DetectFrame(camImage)
                    if ( len(self.faceDetector.object_info) != 0 )  :
                        for box, _, _ in self.faceDetector.object_info:
                            ymin, xmin, ymax, xmax, label = box
                            if (self.face_timer.togger) :
                                self.face_status = label
                    else :
                        self.face_timer.reset()

                    self.handDetector.DetectFrame(camImage)
                    if ( len(self.handDetector.object_info) != 0 )  :
                        for box, _, angle in self.handDetector.object_info:
                            ymin, xmin, ymax, xmax, label = box
                            self.gesture_timer.checklabel(label)
                            if (label in {"five", "fist"}) :
                                self.gesture_timer.setlabel(label)
                                self.volume_status = False
                                self.volume_list = []
                            elif (label == "seven" or self.volume_status) :
                                self.volume_status = True
                                slider_len = self.handDetector.GetSliderFromLandmark(camImage)
                                self.volume_list.append(slider_len)
                                if len(self.volume_list) > 10:
                                    self.volume_list.pop(0)
                                    if (self._average(self.volume_list)) : 
                                        self.sinVolumeOut.emit(self._average(self.volume_list))
                            else :
                                self.volume_list = []

                            if (self.gesture_timer.togger) :
                                self.gesture_status = label
                                if (label == "five"):
                                    self.angle_list.append(angle)
                                    if len(self.angle_list) > 10:
                                        self.angle_list.pop(0)
                                        if (self._average(self.angle_list)) : 
                                            self.sinAngleOut.emit(self._average(self.angle_list))

                    if self.face_timer.togger or self.gesture_timer.togger :    
                        self.sinVideoOut.emit(self.face_status, self.gesture_status)
                    else :
                        self.sinVideoOut.emit("None", "None")

                    if (self.is_display) :  
                        if (self.face_timer.togger) :
                            camImage = self.faceDetector.DrawDetectedOnFrame(camImage, 10)
                        else :
                            camImage = self.faceDetector.DrawDetectedOnFrame(camImage, 2)

                        if (self.gesture_timer.togger) :
                            camImage = self.handDetector.DrawDetectedOnFrame(camImage, 10)
                        else :
                            camImage = self.handDetector.DrawDetectedOnFrame(camImage, 2)

                        camImage = cv2.resize(camImage, (320, 240))
                        cv2.imshow('MediaPipe', camImage)
                    else :
                        cv2.destroyAllWindows()
                    cv2.waitKey(1)


class VideoPlayer(QMainWindow):
    def __init__(self, __appname__):
        super(__class__, self).__init__()
        try :
            vlc_base_dir = os.path.join(os.environ["ProgramFiles"], "VideoLAN", "VLC", "libvlc.dll")
            CDLL(vlc_base_dir)
        except :
            QMessageBox.critical(None, 'Error', "No Found libvlc.dll. Please check and download 'VLC media player' x64 version.")

        self.__appname__ = __appname__
        self.path = QDir.currentPath()
        self.instance = vlc.Instance(CMD_OPTIONS.format(SUB_SIZE_START_VALUE, VLC_WHITE))
        self.mediaplayer = self.instance.media_player_new()
        self.media = None
        self.detector = False
        self.detectorThread = None
        self.isFaceClose = False
        self.isGestureClose = False
        self.isBtnClose = False
        self.setControlPb = 1
        self.setupUi()
        self.connects()

    def setupUi(self):
        if (Path.is_file(Path(__app_ico__))):
            self.setWindowIcon(QtGui.QIcon(__app_ico__))
        else :
            self.setWindowIcon(QtGui.QIcon(':/SmartVideoPlayer'))
        self.setObjectName("MainWindow")
        self.resize(814, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QWidget { background-color : black;} ")

        #-----------------------
        #         Meun
        #-----------------------
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionLoadMedia = QtWidgets.QAction(self)
        self.actionLoadMedia.setObjectName("actionLoadMedia")
        self.actionLoadURL = QtWidgets.QAction(self)
        self.actionLoadURL.setObjectName("actionLoadURL")
        self.actionShowDetector = QtWidgets.QAction(self)
        self.actionShowDetector.setObjectName("actionShowDetector")
        self.menuFile.addAction(self.actionLoadMedia)
        if (show_url) : self.menuFile.addAction(self.actionLoadURL)
        self.menuFile.addAction(self.actionShowDetector)
        self.menubar.addAction(self.menuFile.menuAction())

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.actionShowInfo = QtWidgets.QAction(self)
        self.actionShowInfo.setObjectName("actionShowInfo")
        self.menuHelp.addAction(self.actionShowInfo)
        self.menubar.addAction(self.menuHelp.menuAction())

        #-----------------------
        #      Video Frame
        #-----------------------
        self.displayVLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.displayVLayout.setContentsMargins(0, 0, 0, 0)
        self.displayVLayout.setSpacing(6)
        self.displayVLayout.setObjectName("verticalLayout_2")
        self.vlcFrame = QtWidgets.QFrame(self.centralwidget)
        self.vlcFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vlcFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vlcFrame.setObjectName("vlcFrame")
        self.displayVLayout.addWidget(self.vlcFrame)

        #-----------------------
        #     Control Panel
        #-----------------------
        self.controlsWidget = QtWidgets.QWidget(self.centralwidget)
        self.controlsWidget.setMaximumSize(QtCore.QSize(16777215, 85))
        self.controlsWidget.setObjectName("controlsWidget")
        radius = 30
        self.controlsWidget.setStyleSheet(
            """
            background:rgb(20, 20, 20);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(self.controlsWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Create the "Playback rate" label
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbRateLabel = QtWidgets.QLabel(" >> {}x".format(self.mediaplayer.get_rate()), self)
        self.pbRateLabel.setFont(QtGui.QFont('Lucida', 10, QtGui.QFont.Bold))
        self.pbRateLabel.setStyleSheet("color: rgb(240, 240, 240); ")
        self.horizontalLayout.addWidget(self.pbRateLabel)

        # Btn
        iconSize = QtCore.QSize(25, 25)
        self.horizontalLayout.addStretch(1)
        self.btn_layout_qss = '''
            QPushButton {
                padding-bottom: 4px; border:none;
            }
            QPushButton:hover {
                padding-bottom: 2px; 
                border:1px solid rgb(100, 100, 100); 
                background: rgb(40, 40, 40); 
            }'''
        self.buttonCamera = QtWidgets.QPushButton(self.controlsWidget)
        self.buttonCamera.setFixedSize(35, 35)
        self.buttonCamera.setStyleSheet(self.btn_layout_qss)
        if (Path.is_file(Path.joinpath(script_dir, "assets/control-center.png"))) :
            self.buttonCamera.setIcon(QtGui.QIcon(str(Path.joinpath(script_dir, "assets/control-center.png"))))
        else :
            self.buttonCamera.setIcon(QtGui.QIcon(":/buttonCamera"))
        self.buttonCamera.setIconSize(iconSize)
        self.buttonCamera.setObjectName("buttonCamera")
        self.horizontalLayout.addWidget(self.buttonCamera)
        self.buttonImport = QtWidgets.QPushButton(self.controlsWidget)
        self.buttonImport.setFixedSize(35, 35)
        self.buttonImport.setStyleSheet(self.btn_layout_qss)
        if Path.is_file(Path.joinpath(script_dir, "assets/file-import.png")):
            self.buttonImport.setIcon(QtGui.QIcon(str(Path.joinpath(script_dir, "assets/file-import.png"))))
        else :
            self.buttonImport.setIcon(QtGui.QIcon(":/buttonImport"))
        self.buttonImport.setIconSize(iconSize)
        self.buttonImport.setObjectName("buttonImport")
        self.horizontalLayout.addWidget(self.buttonImport)
        self.buttonBackward = QtWidgets.QPushButton(self.controlsWidget)
        self.buttonBackward.setFixedSize(35, 35)
        self.buttonBackward.setStyleSheet(self.btn_layout_qss)
        if Path.is_file(Path.joinpath(script_dir, "assets/fast-backward.png")):
            self.buttonBackward.setIcon(QtGui.QIcon(str(Path.joinpath(script_dir, "assets/fast-backward.png"))))
        else :
            self.buttonBackward.setIcon(QtGui.QIcon(":/buttonBackward"))
        self.buttonBackward.setIconSize(iconSize)
        self.buttonBackward.setObjectName("buttonBackward")
        self.horizontalLayout.addWidget(self.buttonBackward)
        self.buttonPlay = QtWidgets.QPushButton(self.controlsWidget)
        self.buttonPlay.setFixedSize(35, 35)
        self.buttonPlay.setStyleSheet(self.btn_layout_qss)
        if Path.is_file(Path.joinpath(script_dir, "assets/play.png")):
            self.buttonPlay.setIcon(QtGui.QIcon(str(Path.joinpath(script_dir, "assets/play.png"))))
        else :
            self.buttonPlay.setIcon(QtGui.QIcon(":/buttonPlay"))
        self.buttonPlay.setIconSize(iconSize)
        self.buttonPlay.setObjectName("buttonPlay")
        self.horizontalLayout.addWidget(self.buttonPlay)
        self.buttonPause = QtWidgets.QPushButton(self.controlsWidget)
        self.buttonPause.hide()
        self.buttonPause.setFixedSize(35, 35)
        self.buttonPause.setStyleSheet(self.btn_layout_qss)
        if Path.is_file(Path.joinpath(script_dir, "assets/pause.png")):
            self.buttonPause.setIcon(QtGui.QIcon(str(Path.joinpath(script_dir, "assets/pause.png"))))
        else :
            self.buttonPause.setIcon(QtGui.QIcon(":/buttonPause"))
        self.buttonPause.setIconSize(iconSize)
        self.buttonPause.setObjectName("buttonPause")
        self.horizontalLayout.addWidget(self.buttonPause)
        self.buttonForward = QtWidgets.QPushButton(self.controlsWidget)
        self.buttonForward.setFixedSize(35, 35)
        self.buttonForward.setStyleSheet(self.btn_layout_qss)
        if Path.is_file(Path.joinpath(script_dir, "assets/fast-forward.png")):
            self.buttonForward.setIcon(QtGui.QIcon(str(Path.joinpath(script_dir, "assets/fast-forward.png"))))
        else :
            self.buttonForward.setIcon(QtGui.QIcon(":/buttonForward"))
        self.buttonForward.setIconSize(iconSize)
        self.buttonForward.setObjectName("buttonForward")
        self.horizontalLayout.addWidget(self.buttonForward)
        self.buttonUndo = QtWidgets.QPushButton(self.controlsWidget)
        self.buttonUndo.setFixedSize(35, 35)
        self.buttonUndo.setStyleSheet(self.btn_layout_qss)
        if Path.is_file(Path.joinpath(script_dir, "assets/undo.png")):
            self.buttonUndo.setIcon(QtGui.QIcon(str(Path.joinpath(script_dir, "assets/undo.png"))))
        else :
            self.buttonUndo.setIcon(QtGui.QIcon(":/buttonStop"))
        self.buttonUndo.setIconSize(iconSize)
        self.buttonUndo.setObjectName("buttonStop")
        self.horizontalLayout.addWidget(self.buttonUndo)

        # Volume
        self.horizontalLayout.addStretch(1)
        self.volumeLabel = QtWidgets.QLabel(self.controlsWidget)
        self.volumeLabel.setFont(QtGui.QFont('Lucida', 8, QtGui.QFont.Bold))
        self.volumeLabel.setStyleSheet("color: rgb(240, 240, 240); ")
        self.volumeLabel.setObjectName("volumeLabel")
        self.horizontalLayout.addWidget(self.volumeLabel)
        self.volumeSlider = QtWidgets.QSlider(self.controlsWidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout.addWidget(self.volumeSlider)
        self.volumePercentLabel = QtWidgets.QLabel(self.controlsWidget)
        self.volumePercentLabel.setFont(QtGui.QFont('Lucida', 8, QtGui.QFont.Bold))
        self.volumePercentLabel.setStyleSheet("color: rgb(240, 240, 240); ")
        self.volumePercentLabel.setObjectName("volumePercentLabel")
        self.horizontalLayout.addWidget(self.volumePercentLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Slider
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.positionSlider = QtWidgets.QSlider(self.controlsWidget)
        self.positionSlider.setStyleSheet('''
            QSlider {
                border-radius: 5px;
            }
            QSlider::groove:horizontal {
                height: 5px;
                background: #000;
            }
            QSlider::handle:horizontal{
                background: rgb(150, 150, 150);
                width: 16px;
                height: 16px;
                margin:-6px 0;
                border-radius:8px;
            }
            QSlider::sub-page:horizontal{
                background:#f90;
            }
        ''')
        self.positionSlider.setMaximum(1000)
        self.positionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.positionSlider.setObjectName("positionSlider")
        self.horizontalLayout2.addWidget(self.positionSlider)
        self.positionLabel = QtWidgets.QLabel(self.controlsWidget)
        self.positionLabel.setFont(QtGui.QFont('Lucida', 8, QtGui.QFont.Bold))
        self.positionLabel.setStyleSheet("color: rgb(240, 240, 240); ")
        self.positionLabel.setObjectName("positionLabel")

        self.horizontalLayout2.addWidget(self.positionLabel)
        self.verticalLayout.addLayout(self.horizontalLayout2)

        self.displayVLayout.addWidget(self.controlsWidget)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(self.__appname__)
        self.positionLabel.setText(_translate("MainWindow", "0:0:0 / 0:0:0"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume"))
        self.volumePercentLabel.setText(_translate("MainWindow", "%"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionLoadMedia.setText(_translate("MainWindow", "Load Media"))
        self.actionLoadURL.setText(_translate("MainWindow", "Load URL"))
        self.actionShowDetector.setText(_translate("MainWindow", "Show Detector"))
        self.actionShowInfo.setText(_translate("MainWindow", "Info"))

    def connects(self):
        # event to enter/quit fullscreen mode and play/pause
        self.keyPressEvent = self.keyPressEvent
        # vlc frame background color
        self.palette = self.vlcFrame.palette()
        self.palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.vlcFrame.setPalette(self.palette)
        self.vlcFrame.setAutoFillBackground(True)
        # position slider
        self.positionSlider.valueChanged.connect(self.set_position)
        self.positionSlider.sliderReleased.connect(self.restart_timer)
        # buttons
        self.buttonCamera.clicked.connect(self.useSmartControl)
        self.buttonImport.clicked.connect(self.OpenMediaFile)
        self.buttonBackward.clicked.connect(self.decrPbRate)
        self.buttonPlay.clicked.connect(self.play)
        self.buttonPause.clicked.connect(self.pause)
        self.buttonForward.clicked.connect(self.incrPbRate)
        self.buttonUndo.clicked.connect(self.undo)
        # volume slider
        self.volumeSlider.valueChanged.connect(self.setVolume)
        self.volumeSlider.setValue(VOLUME_START_VALUE)
        # load file action
        self.actionLoadMedia.triggered.connect(self.OpenMediaFile)
        # load url action
        if (show_url) :
            self.actionLoadURL.triggered.connect(self.OpenUrlPath)
        # show detector action
        self.actionShowDetector.triggered.connect(self.showSmartControl)
        self.actionShowInfo.triggered.connect(self.ShowInfoDialog)
        # timer to postion slider update
        self.timer = QTimer(self)
        self.timer.setInterval(150)
        self.timer.timeout.connect(self._updatePositionSlider)

    def __getDetectorLabel(self, face_label, gesture_label) :
        """
        Get face/hand label togger from DetectorWorker Class.

        Args:
            face_label: Get current face detector label 
                        (default - 'None', class list - 'face', 'unknown').
            gesture_label: Get current gesture detector label 
                           (default - 'None', class list - 'five', 'fist', 'seven', 'unknown').

        Returns:
            None
        """

        if face_label == "face" and not self.mediaplayer.is_playing() and not self.isGestureClose and not self.isBtnClose:
            self.isFaceClose = False
            self.play(True)
        elif face_label != "face" and self.mediaplayer.is_playing() and ( "None" not in {face_label, gesture_label}) :
            self.isFaceClose = True
            self.pause(True)

        if gesture_label == "five" and (self.isGestureClose or self.isBtnClose) :
            self.isGestureClose = False
            self.play(True)
        elif gesture_label == "fist" :
            self.isGestureClose = True
            self.pause(True)

    def __getDetectorDistance(self, volume):
        """
        Get distance between thumb/index finger from DetectorWorker Class.

        Args:
            volume: Convert the pixels lengths between the index finger and the thumb finger.

        Returns:
            None
        """
        self.volumeSlider.setValue(volume)

    def __getDetectorAngle(self, angle) :
        """
        Get angle togger from DetectorWorker Class.
        angle < 0: decr pb rate.
        angle >= 0: incr pb rate.

        i) |angle| <= 20 -> 1x rate.
        ii) 20 < |angle| <= 40 -> 2x rate.
        iii) |angle| > 40 -> 4x rate. 

        Args:
            angle: Get current angle when detect five label.

        Returns:
            None
        """
        angle = -angle
        if ( angle < -40 and self.setControlPb != -4):
            self.setControlPb = -4
            self.mediaplayer.set_rate(0.25)  
        elif ( -40 <= angle < -20 and self.setControlPb != -2):
            self.setControlPb = -2
            self.mediaplayer.set_rate(0.5)  
        elif ( -20 <= angle <= 20 and self.setControlPb != 1):
            self.setControlPb = 1
            self.mediaplayer.set_rate(1)  
        elif ( 20 < angle <= 40 and self.setControlPb != 2):
            self.setControlPb = 2
            self.mediaplayer.set_rate(2)  
        elif (angle > 40 and self.setControlPb != 4):
            self.setControlPb = 4
            self.mediaplayer.set_rate(4)    
        self._updatePbRateLabel()

    @pyqtSlot(QKeyEvent)
    def keyPressEvent(self, event):
        # in case of escape key
        if event.key() == Qt.Key_Escape:
            # showing full screen
            if self.windowState() == Qt.WindowNoState:
                self.menubar.hide()
                self.statusbar.hide()
                self.controlsWidget.hide()
                self.setWindowState(Qt.WindowFullScreen)
            # returning from fullscreen
            else:
                self.menubar.show()
                self.statusbar.show()
                self.controlsWidget.show()
                self.setWindowState(Qt.WindowNoState)
        # in case of P key -> play/pause switch
        elif event.key() == Qt.Key_P:
            if self.mediaplayer.is_playing(): self.pause()
            else: self.play()
        # otherwise we just accept the event
        event.accept()

    @pyqtSlot()
    def useSmartControl(self):
        self.isGestureClose = False
        self.isFaceClose = False

        if (self.detector) :
            self.buttonCamera.setStyleSheet(self.btn_layout_qss)
            self.detector = False
            self.detectorThread.exit()
        else :
            self.detectorThread = DetectorWorker()
            self.detectorThread.sinVideoOut.connect(self.__getDetectorLabel)
            self.detectorThread.sinVolumeOut.connect(self.__getDetectorDistance)
            self.detectorThread.sinAngleOut.connect(self.__getDetectorAngle)
            self.detectorThread.start()
            if self.detectorThread.working :
                self.buttonCamera.setStyleSheet("QPushButton{background-color: maroon; border:1px solid rgb(255, 0, 0); }")
                self.detector = True
            else :
                self.detector = False

    @pyqtSlot()
    def showSmartControl(self):
        if (self.detector) :
            self.detectorThread.is_display = not self.detectorThread.is_display
        
    @pyqtSlot()
    def OpenMediaFile(self, default_file_path=None):
        """
        Open Video File from PC.
        
        If input path is None will jump out select file dialog, 
        others are automatically loaded smart control and enabled.

        Args:
            default_file_path: input str path.

        Returns:
            None
        """

        if (default_file_path == None) :
            # opening and verifying file
            default_file_path = QFileDialog.getOpenFileName(self, "Choose Media File", self.path)
            if not default_file_path[0]: return
        else :
            if not Path.is_file(Path(default_file_path)) : return 
            self.useSmartControl()
            default_file_path = [default_file_path]

        # initializing media
        self.try_release_media()
        self.media = self.instance.media_new(default_file_path[0])
        # updating path
        self.path = default_file_path[0]
        # put the media in the media player
        self.mediaplayer.set_media(self.media)
        # parse the metadata of the file
        self.media.parse()
        # set the title of the track as window title
        self.setWindowTitle(self.media.get_meta(0))

        # checking o.s. to integrate mediaplayer on qframe
        self.set_player_on_qframe()
        self.play()
        time.sleep(0.1)
        # getting fps
        self.fps = self.mediaplayer.get_fps()
        self.rate = self.mediaplayer.get_rate()
        self.totalTimeString = self.mediaplayer.get_length()
        self.totalFrame = int(self.mediaplayer.get_length() * self.fps/1000)
        print("\n==========Video==========")
        print("File:", self.path)
        print("File Type:", self.path.split(".")[-1])
        print("FPS:", self.fps)
        print("Current Rate:", self.rate)
        print("Total Frames:", self.totalFrame)
        print("Video Length:", self.msToHMS(self.totalTimeString))
        print("=========================\n")

    @pyqtSlot()
    def OpenUrlPath(self):
        # url dialog and checking
        url, ok = QInputDialog.getText(self, 'Open Stream', 'Put the media url:')
        if not ok or not url: return
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        # release and new instances
        self.try_release_media()
        self.mediaplayer.release()
        self.mediaplayer = self.instance.media_player_new()
        Media = self.instance.media_new(url)
        Media.get_mrl()
        self.mediaplayer.set_media(Media)
        # self.mediaplayer.set_mrl(url, "network-caching=2000")

        self.set_player_on_qframe()
        # getting media from opened url
        self.media = self.mediaplayer.get_media()
        self.media.parse()
        self.setWindowTitle(self.media.get_meta(0))
        self.timer.start()

        # checking o.s. to integrate mediaplayer on qframe
        self.play()
        time.sleep(0.1)

    @pyqtSlot()
    def ShowInfoDialog(self):
        msg = u'Author: {0} \n\nApp Name: {1} \nApp Version: {2}'.format("Kai-Chun, Li", __appname__, __version__)
        QMessageBox.information(self, u'Information', msg)

    @pyqtSlot()
    def play(self, detector_status=False):
        if (not detector_status and not self.mediaplayer.is_playing()) :
            self.isBtnClose = False

        # playing media
        if self.mediaplayer.play() >= 0:
            self.mediaplayer.play()
            self.timer.start()
            self.buttonPause.show()
            self.buttonPlay.hide()

    @pyqtSlot()
    def pause(self, detector_status=False):
        if (not detector_status and self.mediaplayer.is_playing()) :
            self.isBtnClose = True

        # pausing media
        self.mediaplayer.set_pause(True)
        self.timer.stop()
        self.buttonPlay.show()
        self.buttonPause.hide()

    @pyqtSlot()
    def undo(self):
        # stopping player
        self.mediaplayer.set_position(0)
        self._updatePositionSlider()

    @pyqtSlot()
    def decrPbRate(self, rate=None):
        """Decrease the movie play rate by a factor of 2."""
        if (self.mediaplayer.get_state() != vlc.State.Playing) :
            return 
        
        if (self.mediaplayer.play() >= 0):
            if self.mediaplayer.get_rate() == rate:
                return
            if self.mediaplayer.get_rate() <= 0.125:
                return

            if (rate == None) :
                rate = self.mediaplayer.get_rate() * 0.5
            self.mediaplayer.set_rate(rate)
            self._updatePbRateLabel()

    @pyqtSlot()
    def incrPbRate(self, rate=None):
        """Increase the movie play rate by a factor of 2."""
        if (self.mediaplayer.get_state() != vlc.State.Playing) :
            return 
        
        if (self.mediaplayer.play() >= 0):
            if self.mediaplayer.get_rate() == rate:
                return
            if self.mediaplayer.get_rate() >= 4:
                return

            if (rate == None) :
                rate = self.mediaplayer.get_rate() * 2
            self.mediaplayer.set_rate(rate)
            self._updatePbRateLabel()

    @pyqtSlot(int)
    def setVolume(self, volume):
        # updating player volume
        self.mediaplayer.audio_set_volume(int(volume*1.5))
        # updating label
        self.volumePercentLabel.setText(PERCENT_LABEL.format(volume))

    @pyqtSlot()
    def release(self):
        # release media player
        self.mediaplayer.release()
        # release and new instance
        self.instance.release()
        self.instance = vlc.Instance(CMD_OPTIONS.format(SUB_SIZE_START_VALUE, VLC_WHITE))
        # new media player
        self.mediaplayer = self.instance.media_player_new()
        # checking o.s. to set player on qframe
        self.set_player_on_qframe()
        # release and new media
        self.try_release_media()
        self.media = self.instance.media_new(self.path)
        self.mediaplayer.set_media(self.media)
        # update position and play
        self.mediaplayer.set_position(0)
        self._updatePositionSlider()
        self.buttonPlay.show()
        self.buttonPause.hide()

    @pyqtSlot(int)
    def set_position(self, pos):
        # set the media position to where the slider was dragged (converts to float between 0 and 1)
        self.timer.stop()
        self.mediaplayer.set_position(pos / 1000.0)

    @pyqtSlot()
    def restart_timer(self):
        self.timer.start()

    @pyqtSlot()
    def _updatePositionSlider(self):
        # set the sliders position to its corresponding media position (qslider only accepts int)
        pos = int(self.mediaplayer.get_position() * 1000)
        # blocking signals and updating value
        self.positionSlider.blockSignals(True)
        self.positionSlider.setValue(pos)
        self.positionSlider.blockSignals(False)
        # updating position label
        self._updatePositionLabel()

    def _updatePositionLabel(self):
        # media length in milliseconds
        length = self.mediaplayer.get_length()
        current = self.mediaplayer.get_time()
        # updating label
        self.positionLabel.setText(POSITION_LABEL.format(self.msToHMS(current), self.msToHMS(length)))

        if self.mediaplayer.get_state() == vlc.State.Ended :
            self.release()

    def _updatePbRateLabel(self):
        if (self.mediaplayer.get_rate() < 1) :
            self.pbRateLabel.setText("<< {}x".format(str(self.mediaplayer.get_rate())))
        else :
             self.pbRateLabel.setText(">> {}x".format(str(self.mediaplayer.get_rate())))

    def try_release_media(self):
        if self.media is not None: self.media.release()

    def set_player_on_qframe(self):
        if platform.system() == "Linux": 
            self.mediaplayer.set_xwindow(int(self.vlcFrame.winId()))
        elif platform.system() == "Windows": 
            self.mediaplayer.set_hwnd(int(self.vlcFrame.winId()))

    @staticmethod
    def msToHMS(value):
        seconds = int((value/1000)%60)
        minutes = int((value/(1000*60))%60)
        hours = int((value/(1000*60*60))%24)
        return ':'.join((str(hours), str(minutes), str(seconds)))
    
# main function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(__app_ico__))
    player = VideoPlayer(__appname__)
    player.show()

    sys_file_path = ""
    if len(sys.argv) >= 2:
        sys_file_path = sys.argv[1]
    time.sleep(0.5)
    print("cmd video path :", sys_file_path)
    player.OpenMediaFile(sys_file_path)

    sys.exit(app.exec_())
