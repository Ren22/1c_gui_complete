from PyQt5.QtCore import Qt, pyqtSignal, QObject
from pipelineController import *


class AMWorker(QObject):

    progressBarSig = pyqtSignal(int)
    pipeStatusToLogger = pyqtSignal(str)
    changeTabSig = pyqtSignal()
    incrementStepSig = pyqtSignal()
    find_am = FindAMinPM()

    def __init__(self):
        super(AMWorker, self).__init__()

    def work_1(self):
        self.find_am.step1()
        self.progressBarSig.emit(10)
        self.incrementStepSig.emit()
        self.changeTabSig.emit()

    def work_2(self):
        self.find_am.step2()
        self.progressBarSig.emit(20)
        self.incrementStepSig.emit()
        self.changeTabSig.emit()

