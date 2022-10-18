import ctypes
import keyboard
import configparser
import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
from Utils.Utilities import strtobool, is_key, is_mouse



class Ui_MainWindow(object):
    def __init__(self):
        self.Trigger = False
        self.Wallhack = False
        self.Bhop = False
        self.Noflash = False
        self.Togglefov = False
        self.Fov = False
        self.Fovkey = ""
        self.Radar = False
        self.Fovt = int()
        self.auto_strafe = False
        self.WRGB = [0, 0, 0]
        self.Ergb = [0, 0, 0]
        self.Argb = [0, 0, 0]
        self.Allies = False
        self.Enemies = False
        self.Healthbased = False
        self.Fovvaluke = int()
        self.Holdfov = False
        self.Eteam = False
        self.Chams = False
        self.spotted = False
        self.healthbasedWH = False



    def createConfig(self):
        self.update()
        config = configparser.ConfigParser()
        config["Visual"] = {
            "Glow": self.Wallhack,
            "GlowColor": self.comboBox_3.currentText(),
            "Chams": self.Chams,
            "Enemies": self.Enemies,
            "Teammates": self.Allies,
            "EColor": self.comboBox.currentText(),
            "AColor": self.comboBox_2.currentText(),
            "NoFlash": self.Noflash,
            "Radar": self.Radar,
        }
        config["BHOP"] = {
            "Bhop": self.Bhop,
            "AutoStrafe": self.auto_strafe
        }


        self.filename = self.lineEdit_9.text() + ".ini"
        with open(f"./Configs/{self.filename}", "w+") as configfile:
            config.write(configfile)
        self.label_14.setText(self.lineEdit_9.text())

    def loadConfig(self):
        config = configparser.ConfigParser()
        self.filename = self.lineEdit_10.text() + ".ini"
        self.filepath = f"./Configs/{self.filename}"
        if os.path.isfile(self.filepath):
            config.read(self.filepath)
            booleana = False
            if booleana:
                print("booli...")
            else:
                try:
                    self.checkBox.setChecked(strtobool(config["Visual"]["Glow"]))
                    self.comboBox_3.setCurrentText(config["Visual"]["GlowColor"])
                    self.checkBox_2.setChecked(strtobool(config["Visual"]["Chams"]))
                    self.checkBox_4.setChecked(strtobool(config["Visual"]["Enemies"]))
                    self.checkBox_5.setChecked(strtobool(config["Visual"]["Teammates"]))
                    self.comboBox.setCurrentText(config["Visual"]["EColor"])
                    self.comboBox_2.setCurrentText(config["Visual"]["AColor"])
                    self.checkBox_3.setChecked(strtobool(config["Visual"]["NoFlash"]))
                    self.checkBox_6.setChecked(strtobool(config["Visual"]["Radar"]))
                    self.checkBox_16.setChecked(strtobool(config["MISC"]["Bhop"]))
                    self.checkBox_17.setChecked(strtobool(config["MISC"]["AutoStrafe"]))
                except Exception as e:
                    pass
            self.label_14.setText(self.lineEdit_10.text())

        else:
            ctypes.windll.user32.MessageBoxW(0, "No file with this name exists", "Wrong File Error", 1)

    def saveConfig(self):
        self.filename = self.lineEdit_11.text() + ".ini"
        if os.path.isfile(f"./Configs/{self.filename}"):
            try:
                self.update()
                config = configparser.ConfigParser()
                config["Visual"] = {
                    "Glow": self.Wallhack,
                    "GlowColor": self.comboBox_3.currentText(),
                    "Chams": self.Chams,
                    "Enemies": self.Enemies,
                    "Teammates": self.Allies,
                    "EColor": self.comboBox.currentText(),
                    "AColor": self.comboBox_2.currentText(),
                    "NoFlash": self.Noflash,
                    "Radar": self.Radar,
                }
                config["NIMIC"] = {
                    "Bhop": self.Bhop,
                    "AutoStrafe": self.auto_strafe
                }
                with open(f"./Configs/{self.filename}", "w") as configfile:
                    config.write(configfile)
                self.label_14.setText(self.lineEdit_11.text())
            except Exception as e:
                print(e)
                pass
        else:
            ctypes.windll.user32.MessageBoxW(0, "Create a new config file first", "This file doesnt exist", 1)

    def update(self):
        update = True
        while update:
            self.Wallhack = self.checkBox.isChecked()
            self.Chams = self.checkBox_2.isChecked()
            self.Noflash = self.checkBox_3.isChecked()
            self.Enemies = self.checkBox_4.isChecked()
            self.Allies = self.checkBox_5.isChecked()
            if self.comboBox.currentText() == "GREEN":
                self.Ergb = [0, 255, 0]
            elif self.comboBox.currentText() == "RED":
                self.Ergb = [255, 0, 0]
            elif self.comboBox.currentText() == "BLUE":
                self.Ergb = [0, 0, 255]
            elif self.comboBox.currentText() == "ORANGE":
                self.Ergb = [255, 69, 0]
            if self.comboBox_2.currentText() == "GREEN":
                self.Argb = [0, 255, 0]
            elif self.comboBox_2.currentText() == "RED":
                self.Argb = [255, 0, 0]
            elif self.comboBox_2.currentText() == "BLUE":
                self.Argb = [0, 0, 255]
            elif self.comboBox_2.currentText() == "ORANGE":
                self.Argb = [255, 69, 0]
            if self.comboBox_3.currentText() == "Healthbased":
                self.healthbasedWH = True
                self.WRGB = [0, 0, 0]
            elif self.comboBox_3.currentText() == "GREEN":
                self.healthbasedWH = False
                self.WRGB = [0, 255, 0]
            elif self.comboBox_3.currentText() == "RED":
                self.healthbasedWH = False
                self.WRGB = [255, 0, 0]
            elif self.comboBox_3.currentText() == "BLUE":
                self.healthbasedWH = False
                self.WRGB = [0, 0, 255]
            elif self.comboBox_3.currentText() == "Orange":
                self.healthbasedWH = False
                self.WRGB = [255, 69, 0]
            self.Radar = self.checkBox_6.isChecked()
            self.spotted = self.checkBox_12.isChecked()
            self.Bhop = self.checkBox_16.isChecked()
            self.auto_strafe = self.checkBox_17.isChecked()
            if self.checkBox_19.isChecked():
                if 0 < int(self.lineEdit_7.text()) < 100:
                    self.random = 5 + (int(self.lineEdit_7.text()) / 5)
                else:
                    ctypes.windll.user32.MessageBoxW(0, "", "Error in Config", 0)
            if self.Fov and not (is_key(self.Fovkey) or is_mouse(self.Fovkey)):
                ctypes.windll.user32.MessageBoxW(0, "Please select a correct Fovkey", "Error in Config", 0)
            self.label_14.setText("None/Unsaved")
            update = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 633)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 861, 671))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(50, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(50, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(50, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(70, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_5.setGeometry(QtCore.QRect(70, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(270, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_6.setGeometry(QtCore.QRect(50, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(200, 520, 211, 51))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(270, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_16 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_16.setGeometry(QtCore.QRect(70, 60, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_16.setFont(font)
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_17.setGeometry(QtCore.QRect(70, 100, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_17.setFont(font)
        self.checkBox_17.setObjectName("checkBox_17")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 520, 211, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(180, 150, 151, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(180, 100, 151, 31))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.checkBox_7 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_7.setGeometry(QtCore.QRect(50, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_8.setGeometry(QtCore.QRect(70, 70, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_9.setGeometry(QtCore.QRect(70, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_10.setGeometry(QtCore.QRect(70, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(70, 200, 51, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(130, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox_12 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_12.setGeometry(QtCore.QRect(70, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_13.setGeometry(QtCore.QRect(390, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setObjectName("checkBox_13")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 300, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(390, 60, 201, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 390, 51, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(130, 390, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.checkBox_19 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_19.setGeometry(QtCore.QRect(70, 440, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_19.setFont(font)
        self.checkBox_19.setObjectName("checkBox_19")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 520, 211, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 480, 51, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(130, 480, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_4, "")
        font = QtGui.QFont()
        font.setPointSize(15)
        font = QtGui.QFont()
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 110, 201, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(150, 60, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(20, 200, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_10.setGeometry(QtCore.QRect(150, 210, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 260, 201, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(150, 520, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 410, 211, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setGeometry(QtCore.QRect(10, 350, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_11.setGeometry(QtCore.QRect(150, 360, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(390, 60, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setGeometry(QtCore.QRect(390, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mame Mature"))
        self.checkBox.setText(_translate("MainWindow", "WH-CLR"))
        self.checkBox_2.setText(_translate("MainWindow", "CHAMS"))
        self.checkBox_3.setText(_translate("MainWindow", "NOFLASH"))
        self.checkBox_4.setText(_translate("MainWindow", "ENEMIES"))
        self.checkBox_5.setText(_translate("MainWindow", "TEAMMATES"))
        self.comboBox.setItemText(0, _translate("MainWindow", "GREEN"))
        self.comboBox.setItemText(1, _translate("MainWindow", "RED"))
        self.comboBox.setItemText(2, _translate("MainWindow", "BLUE"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ORANGE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Healthbased"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "GREEN"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "RED"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "BLUE"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "ORANGE"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Healthbased"))
        self.checkBox_6.setText(_translate("MainWindow", "RADAR"))
        self.pushButton.setText(_translate("MainWindow", "UPDATE"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Healthbased"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "GREEN"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "RED"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "BLUE"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "ORANGE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "WH"))
        self.checkBox_16.setText(_translate("MainWindow", "BHOP"))
        self.checkBox_17.setText(_translate("MainWindow", "AUTO STRAFE"))
        self.pushButton_3.setText(_translate("MainWindow", "UPDATE"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "BHOP"))
        self.checkBox_7.setText(_translate("MainWindow", "[objectWindow]"))
        self.checkBox_8.setText(_translate("MainWindow", "[objectWindow]"))
        self.checkBox_9.setText(_translate("MainWindow", "[objectWindow]"))
        self.checkBox_10.setText(_translate("MainWindow", "[objectWindow]"))
        self.lineEdit.setText(_translate("MainWindow", "69"))
        self.label.setText(_translate("MainWindow", "[objectWindow]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "AIM"))
        self.checkBox_12.setText(_translate("MainWindow", "[objectWindow]"))
        self.checkBox_13.setText(_translate("MainWindow", "[objectWindow]"))
        self.lineEdit_2.setText(_translate("MainWindow", "[objectWindow]"))
        self.lineEdit_4.setText(_translate("MainWindow", "[objectWindow]"))
        self.lineEdit_6.setText(_translate("MainWindow", "69"))
        self.label_4.setText(_translate("MainWindow", "[objectWindow]"))
        self.checkBox_19.setText(_translate("MainWindow", "[objectWindow]"))
        self.pushButton_2.setText(_translate("MainWindow", "[objectWindow]"))
        self.lineEdit_7.setText(_translate("MainWindow", "69"))
        self.label_5.setText(_translate("MainWindow", "[objectWindow]"))
        self.pushButton_5.setText(_translate("MainWindow", "Create new Config"))
        self.label_9.setText(_translate("MainWindow", "Config Name"))
        self.lineEdit_9.setText(_translate("MainWindow", ""))
        self.label_10.setText(_translate("MainWindow", "Config Name"))
        self.lineEdit_10.setText(_translate("MainWindow", ""))
        self.pushButton_6.setText(_translate("MainWindow", "Load Config"))
        self.label_11.setText(_translate("MainWindow", "./Configs"))
        self.pushButton_7.setText(_translate("MainWindow", "Save current Config"))
        self.label_12.setText(_translate("MainWindow", "Config Name"))
        self.lineEdit_11.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", "Current Config:"))
        self.label_14.setText(_translate("MainWindow", "None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Config"))
        self.pushButton.clicked.connect(self.update)
        self.pushButton_2.clicked.connect(self.update)
        self.pushButton_3.clicked.connect(self.update)
        self.pushButton_5.clicked.connect(self.createConfig)
        self.pushButton_6.clicked.connect(self.loadConfig)
        self.pushButton_7.clicked.connect(self.saveConfig)
