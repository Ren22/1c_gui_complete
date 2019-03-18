# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1093, 911)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnImprtSettings = QtWidgets.QPushButton(self.centralWidget)
        self.btnImprtSettings.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btnImprtSettings.setObjectName("btnImprtSettings")
        self.gridLayout.addWidget(self.btnImprtSettings, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.LogsTextBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.LogsTextBrowser.setMaximumSize(QtCore.QSize(16777215, 120))
        self.LogsTextBrowser.setObjectName("LogsTextBrowser")
        self.gridLayout.addWidget(self.LogsTextBrowser, 1, 1, 4, 1)
        self.btnStartAnalysis = QtWidgets.QPushButton(self.centralWidget)
        self.btnStartAnalysis.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btnStartAnalysis.setObjectName("btnStartAnalysis")
        self.gridLayout.addWidget(self.btnStartAnalysis, 4, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(11111111, 11111111))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.gen_settings = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gen_settings.sizePolicy().hasHeightForWidth())
        self.gen_settings.setSizePolicy(sizePolicy)
        self.gen_settings.setObjectName("gen_settings")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gen_settings)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.gen_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.helpText = QtWidgets.QTextEdit(self.gen_settings)
        self.helpText.setMaximumSize(QtCore.QSize(16777215, 100))
        self.helpText.setObjectName("helpText")
        self.gridLayout_3.addWidget(self.helpText, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.gen_settings)
        self.groupBox.setMaximumSize(QtCore.QSize(661, 140))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEditMainFolder = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditMainFolder.setObjectName("lineEditMainFolder")
        self.gridLayout_2.addWidget(self.lineEditMainFolder, 0, 1, 1, 1)
        self.btnCellProfiler = QtWidgets.QToolButton(self.groupBox)
        self.btnCellProfiler.setObjectName("btnCellProfiler")
        self.gridLayout_2.addWidget(self.btnCellProfiler, 2, 2, 1, 1)
        self.btnPython = QtWidgets.QToolButton(self.groupBox)
        self.btnPython.setObjectName("btnPython")
        self.gridLayout_2.addWidget(self.btnPython, 1, 2, 1, 1)
        self.btnMainFolder = QtWidgets.QToolButton(self.groupBox)
        self.btnMainFolder.setObjectName("btnMainFolder")
        self.gridLayout_2.addWidget(self.btnMainFolder, 0, 2, 1, 1)
        self.lineEditCellProfiler = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditCellProfiler.setObjectName("lineEditCellProfiler")
        self.gridLayout_2.addWidget(self.lineEditCellProfiler, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEditPythonPath = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditPythonPath.setObjectName("lineEditPythonPath")
        self.gridLayout_2.addWidget(self.lineEditPythonPath, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.gen_settings)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btnUdpFile = QtWidgets.QToolButton(self.groupBox_3)
        self.btnUdpFile.setObjectName("btnUdpFile")
        self.gridLayout_6.addWidget(self.btnUdpFile, 0, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_6.addWidget(self.pushButton_4, 0, 4, 1, 1)
        self.btnImzMLFilename = QtWidgets.QToolButton(self.groupBox_3)
        self.btnImzMLFilename.setObjectName("btnImzMLFilename")
        self.gridLayout_6.addWidget(self.btnImzMLFilename, 1, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_6.addWidget(self.pushButton_5, 1, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 2, 0, 1, 2)
        self.lineEditMetadata = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditMetadata.setObjectName("lineEditMetadata")
        self.gridLayout_6.addWidget(self.lineEditMetadata, 2, 2, 1, 1)
        self.btnMALDImetadata = QtWidgets.QToolButton(self.groupBox_3)
        self.btnMALDImetadata.setObjectName("btnMALDImetadata")
        self.gridLayout_6.addWidget(self.btnMALDImetadata, 2, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_6.addWidget(self.pushButton_7, 2, 4, 1, 1)
        self.lineEditimzMLName = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditimzMLName.setObjectName("lineEditimzMLName")
        self.gridLayout_6.addWidget(self.lineEditimzMLName, 1, 2, 1, 1)
        self.lineEditUdpFile = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditUdpFile.setObjectName("lineEditUdpFile")
        self.gridLayout_6.addWidget(self.lineEditUdpFile, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_6)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.gen_settings)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEditMSLogin = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEditMSLogin.setObjectName("lineEditMSLogin")
        self.gridLayout_7.addWidget(self.lineEditMSLogin, 0, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_7.addWidget(self.pushButton_8, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEditMSPass = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEditMSPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditMSPass.setObjectName("lineEditMSPass")
        self.gridLayout_7.addWidget(self.lineEditMSPass, 1, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_7.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 2, 0, 1, 1)
        self.lineEditMSDb = QtWidgets.QListWidget(self.groupBox_4)
        self.lineEditMSDb.setObjectName("lineEditMSDb")
        item = QtWidgets.QListWidgetItem()
        self.lineEditMSDb.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lineEditMSDb.addItem(item)
        self.gridLayout_7.addWidget(self.lineEditMSDb, 2, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_7.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 3, 0, 1, 1)
        self.comboBoxFdr = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBoxFdr.setObjectName("comboBoxFdr")
        self.comboBoxFdr.addItem("")
        self.comboBoxFdr.addItem("")
        self.comboBoxFdr.addItem("")
        self.gridLayout_7.addWidget(self.comboBoxFdr, 3, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_11.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_7.addWidget(self.pushButton_11, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.gridLayout_5.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gen_settings)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.btnCpPipeFile = QtWidgets.QToolButton(self.groupBox_2)
        self.btnCpPipeFile.setObjectName("btnCpPipeFile")
        self.gridLayout_8.addWidget(self.btnCpPipeFile, 6, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_15.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_8.addWidget(self.pushButton_15, 6, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_8.addWidget(self.label_19, 6, 0, 1, 1)
        self.lineEditCPpipeFile = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditCPpipeFile.setObjectName("lineEditCPpipeFile")
        self.gridLayout_8.addWidget(self.lineEditCPpipeFile, 6, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_8.addWidget(self.label_17, 2, 0, 1, 1)
        self.lineEditCompositeImg = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditCompositeImg.setObjectName("lineEditCompositeImg")
        self.gridLayout_8.addWidget(self.lineEditCompositeImg, 5, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_8.addWidget(self.pushButton_6, 2, 3, 1, 1)
        self.btnStitchedPostMDapiImg = QtWidgets.QToolButton(self.groupBox_2)
        self.btnStitchedPostMDapiImg.setObjectName("btnStitchedPostMDapiImg")
        self.gridLayout_8.addWidget(self.btnStitchedPostMDapiImg, 3, 2, 1, 1)
        self.btnStitchedPreMSampleImg = QtWidgets.QToolButton(self.groupBox_2)
        self.btnStitchedPreMSampleImg.setObjectName("btnStitchedPreMSampleImg")
        self.gridLayout_8.addWidget(self.btnStitchedPreMSampleImg, 4, 2, 1, 1)
        self.lineEditStitPostMDapiImage = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditStitPostMDapiImage.setObjectName("lineEditStitPostMDapiImage")
        self.gridLayout_8.addWidget(self.lineEditStitPostMDapiImage, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_8.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_8.addWidget(self.label_18, 5, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_8.addWidget(self.pushButton_12, 5, 3, 1, 1)
        self.btnStitchedPreMDapiImg = QtWidgets.QToolButton(self.groupBox_2)
        self.btnStitchedPreMDapiImg.setObjectName("btnStitchedPreMDapiImg")
        self.gridLayout_8.addWidget(self.btnStitchedPreMDapiImg, 2, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_8.addWidget(self.label_15, 3, 0, 1, 1)
        self.lineEditStitPreMDapiImage = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditStitPreMDapiImage.setObjectName("lineEditStitPreMDapiImage")
        self.gridLayout_8.addWidget(self.lineEditStitPreMDapiImage, 2, 1, 1, 1)
        self.btnStitchedPreMBfImg = QtWidgets.QToolButton(self.groupBox_2)
        self.btnStitchedPreMBfImg.setObjectName("btnStitchedPreMBfImg")
        self.gridLayout_8.addWidget(self.btnStitchedPreMBfImg, 0, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_8.addWidget(self.label_16, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_8.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.lineEditStitPreMSampleImage = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditStitPreMSampleImage.setObjectName("lineEditStitPreMSampleImage")
        self.gridLayout_8.addWidget(self.lineEditStitPreMSampleImage, 4, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_8.addWidget(self.pushButton_14, 3, 3, 1, 1)
        self.btnCompositeImg = QtWidgets.QToolButton(self.groupBox_2)
        self.btnCompositeImg.setObjectName("btnCompositeImg")
        self.gridLayout_8.addWidget(self.btnCompositeImg, 5, 2, 1, 1)
        self.lineEditStitchedPostMImage = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditStitchedPostMImage.setObjectName("lineEditStitchedPostMImage")
        self.gridLayout_8.addWidget(self.lineEditStitchedPostMImage, 1, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_8.addWidget(self.pushButton_13, 4, 3, 1, 1)
        self.btnStitchedPostMBfImg = QtWidgets.QToolButton(self.groupBox_2)
        self.btnStitchedPostMBfImg.setObjectName("btnStitchedPostMBfImg")
        self.gridLayout_8.addWidget(self.btnStitchedPostMBfImg, 1, 2, 1, 1)
        self.lineEditStitchedPreMImage = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditStitchedPreMImage.setObjectName("lineEditStitchedPreMImage")
        self.gridLayout_8.addWidget(self.lineEditStitchedPreMImage, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_8)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.gen_settings, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_10.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.helpText_2 = QtWidgets.QTextEdit(self.tab_2)
        self.helpText_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.helpText_2.setObjectName("helpText_2")
        self.gridLayout_4.addWidget(self.helpText_2, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_2.setMaximumSize(QtCore.QSize(1039, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4.addWidget(self.widget_2, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        self.btnSaveSettings = QtWidgets.QPushButton(self.centralWidget)
        self.btnSaveSettings.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btnSaveSettings.setObjectName("btnSaveSettings")
        self.gridLayout.addWidget(self.btnSaveSettings, 2, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1093, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuSd = QtWidgets.QMenu(self.menuBar)
        self.menuSd.setObjectName("menuSd")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionImport_settings = QtWidgets.QAction(MainWindow)
        self.actionImport_settings.setObjectName("actionImport_settings")
        self.menuSd.addAction(self.actionImport_settings)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuSd.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "spaceM 0.1"))
        self.btnImprtSettings.setText(_translate("MainWindow", "Import settings"))
        self.pushButton.setText(_translate("MainWindow", "Run step"))
        self.LogsTextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Logs</p></body></html>"))
        self.btnStartAnalysis.setText(_translate("MainWindow", "Run pipeline"))
        self.label.setText(_translate("MainWindow", "Help:"))
        self.helpText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is an example text that will be substituted with a custom step dependent explanotary information. For general setting, user has to provide all necessary paths to Main folder to where to store the output files, path to Python interpreter(ver&gt;3), and select stitched image with cell Profiler installed path.</p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "General settings"))
        self.label_6.setText(_translate("MainWindow", "Cell Profiler path(Windows only):"))
        self.label_3.setText(_translate("MainWindow", "Main Folder:"))
        self.btnCellProfiler.setText(_translate("MainWindow", "..."))
        self.btnPython.setText(_translate("MainWindow", "..."))
        self.btnMainFolder.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "Python interpreter:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "MALDI data"))
        self.btnUdpFile.setText(_translate("MainWindow", "..."))
        self.pushButton_4.setText(_translate("MainWindow", "?"))
        self.btnImzMLFilename.setText(_translate("MainWindow", "..."))
        self.pushButton_5.setText(_translate("MainWindow", "?"))
        self.label_12.setText(_translate("MainWindow", "MALDI Metadata file:"))
        self.btnMALDImetadata.setText(_translate("MainWindow", "..."))
        self.pushButton_7.setText(_translate("MainWindow", "?"))
        self.label_5.setText(_translate("MainWindow", "imzML filename"))
        self.label_7.setText(_translate("MainWindow", "UDP file:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Metaspace data"))
        self.label_9.setText(_translate("MainWindow", "Login:"))
        self.pushButton_8.setText(_translate("MainWindow", "?"))
        self.label_10.setText(_translate("MainWindow", "Password:"))
        self.pushButton_9.setText(_translate("MainWindow", "?"))
        self.label_13.setText(_translate("MainWindow", "Database:"))
        __sortingEnabled = self.lineEditMSDb.isSortingEnabled()
        self.lineEditMSDb.setSortingEnabled(False)
        item = self.lineEditMSDb.item(0)
        item.setText(_translate("MainWindow", "HMDB-v4"))
        item = self.lineEditMSDb.item(1)
        item.setText(_translate("MainWindow", "Chebi-2018-1"))
        self.lineEditMSDb.setSortingEnabled(__sortingEnabled)
        self.pushButton_10.setText(_translate("MainWindow", "?"))
        self.label_14.setText(_translate("MainWindow", "FDR:"))
        self.comboBoxFdr.setItemText(0, _translate("MainWindow", "10%"))
        self.comboBoxFdr.setItemText(1, _translate("MainWindow", "20%"))
        self.comboBoxFdr.setItemText(2, _translate("MainWindow", "50%"))
        self.pushButton_11.setText(_translate("MainWindow", "?"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Pre/Post MALDI images"))
        self.btnCpPipeFile.setText(_translate("MainWindow", "..."))
        self.pushButton_15.setText(_translate("MainWindow", "?"))
        self.label_19.setText(_translate("MainWindow", "(Optional) Cellprofiler pipeline file:"))
        self.label_17.setText(_translate("MainWindow", "Pre MALDI fluorescent (DAPI) image:"))
        self.pushButton_6.setText(_translate("MainWindow", "?"))
        self.btnStitchedPostMDapiImg.setText(_translate("MainWindow", "..."))
        self.btnStitchedPreMSampleImg.setText(_translate("MainWindow", "..."))
        self.pushButton_3.setText(_translate("MainWindow", "?"))
        self.label_8.setText(_translate("MainWindow", "Stitched Pre MALDI brightfield image:"))
        self.label_18.setText(_translate("MainWindow", "Composite.png file:"))
        self.pushButton_12.setText(_translate("MainWindow", "?"))
        self.btnStitchedPreMDapiImg.setText(_translate("MainWindow", "..."))
        self.label_15.setText(_translate("MainWindow", "Post MALDI fluorescent  (DAPI) image:"))
        self.btnStitchedPreMBfImg.setText(_translate("MainWindow", "..."))
        self.label_16.setText(_translate("MainWindow", "Pre MALDI fluorescent (Sample) image:"))
        self.label_11.setText(_translate("MainWindow", "Stitched Post MALDI brightfield mage:"))
        self.pushButton_2.setText(_translate("MainWindow", "?"))
        self.pushButton_14.setText(_translate("MainWindow", "?"))
        self.btnCompositeImg.setText(_translate("MainWindow", "..."))
        self.pushButton_13.setText(_translate("MainWindow", "?"))
        self.btnStitchedPostMBfImg.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gen_settings), _translate("MainWindow", "General settings"))
        self.helpText_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">These are set of asdditional parameters to be specified for a pipileine</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Help:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Additonal settings"))
        self.btnSaveSettings.setText(_translate("MainWindow", "Save settings"))
        self.menuSd.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionImport_settings.setText(_translate("MainWindow", "Import settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

