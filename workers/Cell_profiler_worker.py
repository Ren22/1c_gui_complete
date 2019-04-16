from PyQt5.QtCore import Qt, pyqtSignal, QObject
from pipelineController import *

class CPWorker(QObject):

    progressBarSig = pyqtSignal(int)
    pipeStatusToLogger = pyqtSignal(str)
    changeTabSig = pyqtSignal()
    incrementStepSig = pyqtSignal()
    cp_worker = CellSegment()

    def __init__(self):
        super(CPWorker, self).__init__()

    def work_1(self):
        self.cp_worker.step0()
        self.cp_worker.step1()
        self.progressBarSig.emit(70)
        self.incrementStepSig.emit()
        self.changeTabSig.emit()

    def work_2(self):
        self.cp_worker.step2()
        self.cp_worker.step3()
        self.cp_worker.step4()
        self.progressBarSig.emit(80)
        self.incrementStepSig.emit()
        self.changeTabSig.emit()
