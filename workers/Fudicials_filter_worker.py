from PyQt5.QtCore import Qt, pyqtSignal, QObject
from pipelineController import *


class FidFilterWorker(QObject):

    progressBarSig = pyqtSignal(int)
    pipeStatusToLogger = pyqtSignal(str)
    changeTabSig = pyqtSignal()
    incrementStepSig = pyqtSignal()
    filter_fiducials = FindFilterFiducials()

    def __init__(self):
        super(FidFilterWorker, self).__init__()

    def work_1(self):
        self.filter_fiducials.step1()
        self.filter_fiducials.step2()
        self.progressBarSig.emit(40)
        self.incrementStepSig.emit()
        self.changeTabSig.emit()
