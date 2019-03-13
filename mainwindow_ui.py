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
        MainWindow.resize(1107, 893)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1061, 801))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.gen_settings = QtWidgets.QWidget()
        self.gen_settings.setObjectName("gen_settings")
        self.layoutWidget = QtWidgets.QWidget(self.gen_settings)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 1041, 601))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.helpText = QtWidgets.QTextEdit(self.layoutWidget)
        self.helpText.setMaximumSize(QtCore.QSize(16777215, 100))
        self.helpText.setObjectName("helpText")
        self.gridLayout_3.addWidget(self.helpText, 1, 0, 1, 1)
        self.widget1 = Gen_Settings(self.layoutWidget)
        self.widget1.setMaximumSize(QtCore.QSize(1039, 16777215))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3.addWidget(self.widget1, 2, 0, 1, 1)
        self.tabWidget.addTab(self.gen_settings, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1041, 601))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.helpText_2 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.helpText_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.helpText_2.setObjectName("helpText_2")
        self.gridLayout_4.addWidget(self.helpText_2, 1, 0, 1, 1)
        self.widget_2 = Add_settings(self.layoutWidget_2)
        self.widget_2.setMaximumSize(QtCore.QSize(1039, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4.addWidget(self.widget_2, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.layoutWidget_2.raise_()
        self.label_2.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 2)
        self.LogsTextBrowser = QtWidgets.QTextBrowser(self.widget)
        self.LogsTextBrowser.setMaximumSize(QtCore.QSize(16777215, 120))
        self.LogsTextBrowser.setObjectName("LogsTextBrowser")
        self.gridLayout.addWidget(self.LogsTextBrowser, 1, 1, 4, 1)
        self.btnImprtSettings = QtWidgets.QPushButton(self.widget)
        self.btnImprtSettings.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btnImprtSettings.setObjectName("btnImprtSettings")
        self.gridLayout.addWidget(self.btnImprtSettings, 1, 0, 1, 1)
        self.btnStartAnalysis = QtWidgets.QPushButton(self.widget)
        self.btnStartAnalysis.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btnStartAnalysis.setObjectName("btnStartAnalysis")
        self.gridLayout.addWidget(self.btnStartAnalysis, 4, 0, 1, 1)
        self.btnSaveSettings = QtWidgets.QPushButton(self.widget)
        self.btnSaveSettings.setMaximumSize(QtCore.QSize(300, 16777215))
        self.btnSaveSettings.setObjectName("btnSaveSettings")
        self.gridLayout.addWidget(self.btnSaveSettings, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1107, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "spaceM 0.1"))
        self.label.setText(_translate("MainWindow", "Help:"))
        self.helpText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is an example text that will be substituted with a custom step dependent explanotary information. For general setting, user has to provide all necessary paths to Main folder to where to store the output files, path to Python interpreter(ver&gt;3), and select stitched image with cell Profiler installed path.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gen_settings), _translate("MainWindow", "General settings"))
        self.helpText_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">These are set of asdditional parameters to be specified for a pipileine</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Help:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Additonal settings"))
        self.LogsTextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Logs</p></body></html>"))
        self.btnImprtSettings.setText(_translate("MainWindow", "Import settings"))
        self.btnStartAnalysis.setText(_translate("MainWindow", "Run pipeline"))
        self.btnSaveSettings.setText(_translate("MainWindow", "Save settings"))
        self.pushButton.setText(_translate("MainWindow", "Run step"))

from add_settings.add_settings import Add_settings
from gen_settings.gen_settings import Gen_Settings

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

