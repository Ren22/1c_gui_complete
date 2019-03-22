from PyQt5.QtCore import Qt, pyqtSignal, QObject
from pipelineController import *


class RegImageWorker(QObject):

    progressBarSig = pyqtSignal(int)
    pipeStatusToLogger = pyqtSignal(str)
    changeTabSig = pyqtSignal()
    incrementStepSig = pyqtSignal()
    reg_pre_post = RegisterPrePostMaldi()

    def __init__(self):
        super(RegImageWorker, self).__init__()

    def work_1(self):
        self.reg_pre_post.step1()
        self.progressBarSig.emit(55)
        self.incrementStepSig.emit()
        self.changeTabSig.emit()
