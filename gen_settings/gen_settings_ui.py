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
        gen_settings.resize(937, 722)
        self.widget = QtWidgets.QWidget(gen_settings)
        self.widget.setGeometry(QtCore.QRect(20, 14, 721, 250))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEditMainFolder = QtWidgets.QLineEdit(self.widget)
        self.lineEditMainFolder.setObjectName("lineEditMainFolder")
        self.gridLayout.addWidget(self.lineEditMainFolder, 1, 1, 1, 1)
        self.btnMainFolder = QtWidgets.QToolButton(self.widget)
        self.btnMainFolder.setObjectName("btnMainFolder")
        self.gridLayout.addWidget(self.btnMainFolder, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditPythonPath = QtWidgets.QLineEdit(self.widget)
        self.lineEditPythonPath.setObjectName("lineEditPythonPath")
        self.gridLayout.addWidget(self.lineEditPythonPath, 2, 1, 1, 1)
        self.btnPython = QtWidgets.QToolButton(self.widget)
        self.btnPython.setObjectName("btnPython")
        self.gridLayout.addWidget(self.btnPython, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEditStitchedPreImage = QtWidgets.QLineEdit(self.widget)
        self.lineEditStitchedPreImage.setObjectName("lineEditStitchedPreImage")
        self.gridLayout.addWidget(self.lineEditStitchedPreImage, 3, 1, 1, 1)
        self.btnStitchedPreImg = QtWidgets.QToolButton(self.widget)
        self.btnStitchedPreImg.setObjectName("btnStitchedPreImg")
        self.gridLayout.addWidget(self.btnStitchedPreImg, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEditStitchedPostImage = QtWidgets.QLineEdit(self.widget)
        self.lineEditStitchedPostImage.setObjectName("lineEditStitchedPostImage")
        self.gridLayout.addWidget(self.lineEditStitchedPostImage, 4, 1, 1, 1)
        self.btnStitchedPostImg = QtWidgets.QToolButton(self.widget)
        self.btnStitchedPostImg.setObjectName("btnStitchedPostImg")
        self.gridLayout.addWidget(self.btnStitchedPostImg, 4, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineEditCompositeImg = QtWidgets.QLineEdit(self.widget)
        self.lineEditCompositeImg.setObjectName("lineEditCompositeImg")
        self.gridLayout.addWidget(self.lineEditCompositeImg, 5, 1, 1, 1)
        self.btnCompositeImg = QtWidgets.QToolButton(self.widget)
        self.btnCompositeImg.setObjectName("btnCompositeImg")
        self.gridLayout.addWidget(self.btnCompositeImg, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEditFiji = QtWidgets.QLineEdit(self.widget)
        self.lineEditFiji.setObjectName("lineEditFiji")
        self.gridLayout.addWidget(self.lineEditFiji, 6, 1, 1, 1)
        self.btnFiji = QtWidgets.QToolButton(self.widget)
        self.btnFiji.setObjectName("btnFiji")
        self.gridLayout.addWidget(self.btnFiji, 6, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.lineEditCellProfiler = QtWidgets.QLineEdit(self.widget)
        self.lineEditCellProfiler.setObjectName("lineEditCellProfiler")
        self.gridLayout.addWidget(self.lineEditCellProfiler, 7, 1, 1, 1)
        self.btnCellProfiler = QtWidgets.QToolButton(self.widget)
        self.btnCellProfiler.setObjectName("btnCellProfiler")
        self.gridLayout.addWidget(self.btnCellProfiler, 7, 2, 1, 1)

        self.retranslateUi(gen_settings)
        QtCore.QMetaObject.connectSlotsByName(gen_settings)

    def retranslateUi(self, gen_settings):
        _translate = QtCore.QCoreApplication.translate
        gen_settings.setWindowTitle(_translate("gen_settings", "Form"))
        self.label_2.setText(_translate("gen_settings", "Inputs"))
        self.label.setText(_translate("gen_settings", "Select Main Folder:"))
        self.btnMainFolder.setText(_translate("gen_settings", "..."))
        self.label_3.setText(_translate("gen_settings", "Select Python:"))
        self.btnPython.setText(_translate("gen_settings", "..."))
        self.label_7.setText(_translate("gen_settings", "Choose your stitched Pre maldi image:"))
        self.btnStitchedPreImg.setText(_translate("gen_settings", "..."))
        self.label_4.setText(_translate("gen_settings", "Choose your stitched Post maldi mage:"))
        self.btnStitchedPostImg.setText(_translate("gen_settings", "..."))
        self.label_8.setText(_translate("gen_settings", "Choose your composite.png file:"))
        self.btnCompositeImg.setText(_translate("gen_settings", "..."))
        self.label_5.setText(_translate("gen_settings", "FiJi path:"))
        self.btnFiji.setText(_translate("gen_settings", "..."))
        self.label_6.setText(_translate("gen_settings", "Cell Profiler path:"))
        self.btnCellProfiler.setText(_translate("gen_settings", "..."))

