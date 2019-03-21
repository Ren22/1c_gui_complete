from PyQt5.QtCore import Qt, pyqtSignal, QObject
from pipelineController import *


class FullPipeWorker(QObject):

    progressBarSig = pyqtSignal(int)
    pipeStatusToLogger = pyqtSignal(str)
    changeTabSig = pyqtSignal(int)
    waitForNextStep = pyqtSignal()
    find_am = FindAMinPM()
    filter_fiducials = FindFilterFiducials()

    def __init__(self):
        super(FullPipeWorker, self).__init__()

    def work_1(self):
        self.find_am.step1()
        self.progressBarSig.emit(10)
        self.pipeStatusToLogger.emit('CropPMimage finished')
        self.pipeStatusToLogger.emit('Ablation mark finder started')
        self.changeTabSig.emit(1)

    def work_2(self):
        self.find_am = FindAMinPM()
        self.find_am.step2()
        self.progressBarSig.emit(20)
        self.pipeStatusToLogger.emit('Cropping of AM finished')
        self.pipeStatusToLogger.emit('Ablation mark filtering started')
        self.changeTabSig.emit(2)

    def work_3(self):
        self.pipeStatusToLogger.emit("Searching for fiducials started")
        self.filter_fiducials.step1()
        self.progressBarSig.emit(30)
        self.pipeStatusToLogger.emit("Searching for fiducials finished")
        self.pipeStatusToLogger.emit('Fiducials filtering on PRE maldi image started')
        self.filter_fiducials.step2()
        self.progressBarSig.emit(40)
        self.pipeStatusToLogger.emit('Fiducials filtering on PRE maldi image finished')

        reg_pre_post = RegisterPrePostMaldi()
        self.pipeStatusToLogger.emit('Registration of Pre and Post maldi fidicuals')
        reg_pre_post.step1()
        self.pipeStatusToLogger.emit('Registration of Pre and Post maldi fidicuals and metaspace based annotation finished')
        self.progressBarSig.emit(55)

        ms_data = GrabMsData()
        self.pipeStatusToLogger.emit('Grabbing annotation from Metaspace2020 started')
        ms_data.step1()
        self.pipeStatusToLogger.emit('Grabbing annotation from Metaspace2020 finished')
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