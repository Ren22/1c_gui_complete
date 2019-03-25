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
        self.gen_csv_worker.step2()
        self.progressBarSig.emit(100)
