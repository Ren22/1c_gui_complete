from PyQt5.QtCore import Qt, pyqtSignal, QObject
from pipelineController import *


class GrabMSDataWorker(QObject):

    progressBarSig = pyqtSignal(int)
    pipeStatusToLogger = pyqtSignal(str)
    changeTabSig = pyqtSignal()
    incrementStepSig = pyqtSignal()
    grab_ms_data = GrabMsData()

    def __init__(self):
        super(GrabMSDataWorker, self).__init__()

    def work_1(self):
        self.grab_ms_data.step1()
        self.progressBarSig.emit(65)
        self.incrementStepSig.emit()
        self.changeTabSig.emit()
