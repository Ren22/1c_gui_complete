# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gen_settings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gen_settings(object):
    def setupUi(self, gen_settings):
        gen_settings.setObjectName("gen_settings")
        gen_settings.resize(1072, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gen_settings.sizePolicy().hasHeightForWidth())
        gen_settings.setSizePolicy(sizePolicy)
        self.layoutWidget = QtWidgets.QWidget(gen_settings)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 991, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setMaximumSize(QtCore.QSize(661, 160))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 32, 316, 95))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditMainFolder = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEditMainFolder.setObjectName("lineEditMainFolder")
        self.gridLayout_2.addWidget(self.lineEditMainFolder, 0, 1, 1, 1)
        self.btnCellProfiler = QtWidgets.QToolButton(self.layoutWidget1)
        self.btnCellProfiler.setObjectName("btnCellProfiler")
        self.gridLayout_2.addWidget(self.btnCellProfiler, 2, 2, 1, 1)
        self.btnPython = QtWidgets.QToolButton(self.layoutWidget1)
        self.btnPython.setObjectName("btnPython")
        self.gridLayout_2.addWidget(self.btnPython, 1, 2, 1, 1)
        self.btnMainFolder = QtWidgets.QToolButton(self.layoutWidget1)
        self.btnMainFolder.setObjectName("btnMainFolder")
        self.gridLayout_2.addWidget(self.btnMainFolder, 0, 2, 1, 1)
        self.lineEditCellProfiler = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEditCellProfiler.setObjectName("lineEditCellProfiler")
        self.gridLayout_2.addWidget(self.lineEditCellProfiler, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEditPythonPath = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEditPythonPath.setObjectName("lineEditPythonPath")
        self.gridLayout_2.addWidget(self.lineEditPythonPath, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(12, 32, 471, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnUdpFile = QtWidgets.QToolButton(self.layoutWidget2)
        self.btnUdpFile.setObjectName("btnUdpFile")
        self.gridLayout_4.addWidget(self.btnUdpFile, 0, 3, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 0, 4, 1, 1)
        self.btnImzMLFilename = QtWidgets.QToolButton(self.layoutWidget2)
        self.btnImzMLFilename.setObjectName("btnImzMLFilename")
        self.gridLayout_4.addWidget(self.btnImzMLFilename, 1, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 1, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 2)
        self.lineEditMetadata = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditMetadata.setObjectName("lineEditMetadata")
        self.gridLayout_4.addWidget(self.lineEditMetadata, 2, 2, 1, 1)
        self.btnMALDImetadata = QtWidgets.QToolButton(self.layoutWidget2)
        self.btnMALDImetadata.setObjectName("btnMALDImetadata")
        self.gridLayout_4.addWidget(self.btnMALDImetadata, 2, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 2, 4, 1, 1)
        self.lineEditimzMLName = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditimzMLName.setObjectName("lineEditimzMLName")
        self.gridLayout_4.addWidget(self.lineEditimzMLName, 1, 2, 1, 1)
        self.lineEditUdpFile = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditUdpFile.setObjectName("lineEditUdpFile")
        self.gridLayout_4.addWidget(self.lineEditUdpFile, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 2)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 32, 471, 176))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEditMSLogin = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditMSLogin.setObjectName("lineEditMSLogin")
        self.gridLayout.addWidget(self.lineEditMSLogin, 0, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEditMSPass = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditMSPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditMSPass.setObjectName("lineEditMSPass")
        self.gridLayout.addWidget(self.lineEditMSPass, 1, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_9.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.lineEditMSDb = QtWidgets.QListWidget(self.layoutWidget3)
        self.lineEditMSDb.setObjectName("lineEditMSDb")
        item = QtWidgets.QListWidgetItem()
        self.lineEditMSDb.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lineEditMSDb.addItem(item)
        self.gridLayout.addWidget(self.lineEditMSDb, 2, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_10.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1)
        self.comboBoxFdr = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBoxFdr.setObjectName("comboBoxFdr")
        self.comboBoxFdr.addItem("")
        self.comboBoxFdr.addItem("")
        self.comboBoxFdr.addItem("")
        self.gridLayout.addWidget(self.comboBoxFdr, 3, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_11.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(11, 31, 480, 227))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEditStitchedPreMImage = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditStitchedPreMImage.setObjectName("lineEditStitchedPreMImage")
        self.gridLayout_3.addWidget(self.lineEditStitchedPreMImage, 0, 1, 1, 1)
        self.btnStitchedPreMBfImg = QtWidgets.QToolButton(self.layoutWidget4)
        self.btnStitchedPreMBfImg.setObjectName("btnStitchedPreMBfImg")
        self.gridLayout_3.addWidget(self.btnStitchedPreMBfImg, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEditStitchedPostMImage = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditStitchedPostMImage.setObjectName("lineEditStitchedPostMImage")
        self.gridLayout_3.addWidget(self.lineEditStitchedPostMImage, 1, 1, 1, 1)
        self.btnStitchedPostMBfImg = QtWidgets.QToolButton(self.layoutWidget4)
        self.btnStitchedPostMBfImg.setObjectName("btnStitchedPostMBfImg")
        self.gridLayout_3.addWidget(self.btnStitchedPostMBfImg, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)
        self.lineEditStitPreMDapiImage = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditStitPreMDapiImage.setObjectName("lineEditStitPreMDapiImage")
        self.gridLayout_3.addWidget(self.lineEditStitPreMDapiImage, 2, 1, 1, 1)
        self.btnStitchedPreMDapiImg = QtWidgets.QToolButton(self.layoutWidget4)
        self.btnStitchedPreMDapiImg.setObjectName("btnStitchedPreMDapiImg")
        self.gridLayout_3.addWidget(self.btnStitchedPreMDapiImg, 2, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 2, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)
        self.lineEditStitPostMDapiImage = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditStitPostMDapiImage.setObjectName("lineEditStitPostMDapiImage")
        self.gridLayout_3.addWidget(self.lineEditStitPostMDapiImage, 3, 1, 1, 1)
        self.btnStitchedPostMDapiImg = QtWidgets.QToolButton(self.layoutWidget4)
        self.btnStitchedPostMDapiImg.setObjectName("btnStitchedPostMDapiImg")
        self.gridLayout_3.addWidget(self.btnStitchedPostMDapiImg, 3, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_14.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_3.addWidget(self.pushButton_14, 3, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 4, 0, 1, 1)
        self.lineEditStitPreMSampleImage = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditStitPreMSampleImage.setObjectName("lineEditStitPreMSampleImage")
        self.gridLayout_3.addWidget(self.lineEditStitPreMSampleImage, 4, 1, 1, 1)
        self.btnStitchedPreMSampleImg = QtWidgets.QToolButton(self.layoutWidget4)
        self.btnStitchedPreMSampleImg.setObjectName("btnStitchedPreMSampleImg")
        self.gridLayout_3.addWidget(self.btnStitchedPreMSampleImg, 4, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_13.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_3.addWidget(self.pushButton_13, 4, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineEditCompositeImg = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditCompositeImg.setObjectName("lineEditCompositeImg")
        self.gridLayout_3.addWidget(self.lineEditCompositeImg, 5, 1, 1, 1)
        self.btnCompositeImg = QtWidgets.QToolButton(self.layoutWidget4)
        self.btnCompositeImg.setObjectName("btnCompositeImg")
        self.gridLayout_3.addWidget(self.btnCompositeImg, 5, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 5, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 6, 0, 1, 1)
        self.lineEditCPpipeFile = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditCPpipeFile.setObjectName("lineEditCPpipeFile")
        self.gridLayout_3.addWidget(self.lineEditCPpipeFile, 6, 1, 1, 1)
        self.btnCpPipeFile = QtWidgets.QToolButton(self.layoutWidget4)
        self.btnCpPipeFile.setObjectName("btnCpPipeFile")
        self.gridLayout_3.addWidget(self.btnCpPipeFile, 6, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_12.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_3.addWidget(self.pushButton_12, 6, 3, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.retranslateUi(gen_settings)
        QtCore.QMetaObject.connectSlotsByName(gen_settings)

    def retranslateUi(self, gen_settings):
        _translate = QtCore.QCoreApplication.translate
        gen_settings.setWindowTitle(_translate("gen_settings", "Form"))
        self.groupBox.setTitle(_translate("gen_settings", "General settings"))
        self.label_6.setText(_translate("gen_settings", "Cell Profiler path:"))
        self.label.setText(_translate("gen_settings", "Main Folder:"))
        self.btnCellProfiler.setText(_translate("gen_settings", "..."))
        self.btnPython.setText(_translate("gen_settings", "..."))
        self.btnMainFolder.setText(_translate("gen_settings", "..."))
        self.label_3.setText(_translate("gen_settings", "Python interpreter:"))
        self.groupBox_3.setTitle(_translate("gen_settings", "MALDI data"))
        self.btnUdpFile.setText(_translate("gen_settings", "..."))
        self.pushButton_4.setText(_translate("gen_settings", "?"))
        self.btnImzMLFilename.setText(_translate("gen_settings", "..."))
        self.pushButton_5.setText(_translate("gen_settings", "?"))
        self.label_12.setText(_translate("gen_settings", "MALDI Metadata file:"))
        self.btnMALDImetadata.setText(_translate("gen_settings", "..."))
        self.pushButton_7.setText(_translate("gen_settings", "?"))
        self.label_5.setText(_translate("gen_settings", "imzML filename"))
        self.label_2.setText(_translate("gen_settings", "UDP file:"))
        self.groupBox_4.setTitle(_translate("gen_settings", "Metaspace data"))
        self.label_9.setText(_translate("gen_settings", "Login:"))
        self.pushButton_8.setText(_translate("gen_settings", "?"))
        self.label_10.setText(_translate("gen_settings", "Password:"))
        self.pushButton_9.setText(_translate("gen_settings", "?"))
        self.label_13.setText(_translate("gen_settings", "Database:"))
        __sortingEnabled = self.lineEditMSDb.isSortingEnabled()
        self.lineEditMSDb.setSortingEnabled(False)
        item = self.lineEditMSDb.item(0)
        item.setText(_translate("gen_settings", "HMDB-v4"))
        item = self.lineEditMSDb.item(1)
        item.setText(_translate("gen_settings", "Chebi-2018-1"))
        self.lineEditMSDb.setSortingEnabled(__sortingEnabled)
        self.pushButton_10.setText(_translate("gen_settings", "?"))
        self.label_14.setText(_translate("gen_settings", "FDR:"))
        self.comboBoxFdr.setItemText(0, _translate("gen_settings", "10%"))
        self.comboBoxFdr.setItemText(1, _translate("gen_settings", "20%"))
        self.comboBoxFdr.setItemText(2, _translate("gen_settings", "50%"))
        self.pushButton_11.setText(_translate("gen_settings", "?"))
        self.groupBox_2.setTitle(_translate("gen_settings", "Pre/Post MALDI images"))
        self.label_7.setText(_translate("gen_settings", "Stitched Pre MALDI brightfield image:"))
        self.btnStitchedPreMBfImg.setText(_translate("gen_settings", "..."))
        self.pushButton.setText(_translate("gen_settings", "?"))
        self.label_4.setText(_translate("gen_settings", "Stitched Post MALDI brightfield mage:"))
        self.btnStitchedPostMBfImg.setText(_translate("gen_settings", "..."))
        self.pushButton_2.setText(_translate("gen_settings", "?"))
        self.label_17.setText(_translate("gen_settings", "Pre MALDI fluorescent (DAPI) image:"))
        self.btnStitchedPreMDapiImg.setText(_translate("gen_settings", "..."))
        self.pushButton_6.setText(_translate("gen_settings", "?"))
        self.label_11.setText(_translate("gen_settings", "Post MALDI fluorescent  (DAPI) image:"))
        self.btnStitchedPostMDapiImg.setText(_translate("gen_settings", "..."))
        self.pushButton_14.setText(_translate("gen_settings", "?"))
        self.label_16.setText(_translate("gen_settings", "Pre MALDI fluorescent (Sample) image:"))
        self.btnStitchedPreMSampleImg.setText(_translate("gen_settings", "..."))
        self.pushButton_13.setText(_translate("gen_settings", "?"))
        self.label_8.setText(_translate("gen_settings", "Composite.png file:"))
        self.btnCompositeImg.setText(_translate("gen_settings", "..."))
        self.pushButton_3.setText(_translate("gen_settings", "?"))
        self.label_15.setText(_translate("gen_settings", "(Optional) Cellprofiler pipeline file:"))
        self.btnCpPipeFile.setText(_translate("gen_settings", "..."))
        self.pushButton_12.setText(_translate("gen_settings", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gen_settings = QtWidgets.QWidget()
    ui = Ui_gen_settings()
    ui.setupUi(gen_settings)
    gen_settings.show()
    sys.exit(app.exec_())

