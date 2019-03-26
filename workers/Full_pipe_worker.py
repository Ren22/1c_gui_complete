from PyQt5.QtCore import Qt, pyqtSignal, QObject
from pipelineController import *


class FullPipeWorker(QObject):

    progressBarSig = pyqtSignal(int)
    pipeStatusToLogger = pyqtSignal(str)
    changeTabSig = pyqtSignal(int)
    finishPipeSig = pyqtSignal()


    def __init__(self):
        super(FullPipeWorker, self).__init__()

    def work_full(self):
        find_am = FindAMinPM()
        self.progressBarSig.emit(0)
        find_am.step1()
        self.progressBarSig.emit(10)
        find_am.step2()
        self.progressBarSig.emit(20)

        filter_fiducials = FindFilterFiducials()
        filter_fiducials.step1()
        self.progressBarSig.emit(30)
        filter_fiducials.step2()
        self.progressBarSig.emit(40)

        reg_pre_post = RegisterPrePostMaldi()
        reg_pre_post.step1()
        self.progressBarSig.emit(55)

        ms_data = GrabMsData()
        ms_data.step1()
        self.progressBarSig.emit(65)

        cell_seg = CellSegment()
        cell_seg.step0()
        cell_seg.step1()
        cell_seg.step2()
        cell_seg.step3()
        cell_seg.step4()
        self.progressBarSig.emit(80)

        gen_csv_features = GenerateCSV()
        gen_csv_features.step1()
        gen_csv_features.step2()
        self.progressBarSig.emit(100)

        self.finishPipeSig.emit()

