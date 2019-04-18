from PyQt5.QtCore import Qt, pyqtSignal, QObject
from pipelineController import *


class GenCSVWorker(QObject):

    progressBarSig = pyqtSignal(int)
    pipeStatusToLogger = pyqtSignal(str)
    changeTabSig = pyqtSignal()
    incrementStepSig = pyqtSignal()
    gen_csv_worker = GenerateCSV()

    def __init__(self):
        super(GenCSVWorker, self).__init__()

    def work_1(self):
        self.gen_csv_worker.step1()
        self.progressBarSig.emit(95)
        # TODO: the fucntionality of step 2 is to create images with cells intensities
        # it should be implemented so that each molecule can have it
        # self.gen_csv_worker.step2()
        self.incrementStepSig.emit()
        self.progressBarSig.emit(100)
