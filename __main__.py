import sys
from mainwindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, QRegExp, QThread
from pipelinecontroller import *
from global_vars import GlobalVars, global_vars
import logging

logging.basicConfig(filename='./spaceM.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.info("Running spaceM v0.1")


class NewThread(QThread):
    progressBarSig = pyqtSignal(int)
    pipeStatusToLogger = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        # find_am = FindAMinPM()
        # find_am.step1()
        # self.progressBarSig.emit(10)
        # self.pipeStatusToLogger.emit('CropPMimage finished')
        # self.pipeStatusToLogger.emit('Ablation mark finder started')
        # find_am.step2()
        #
        # self.progressBarSig.emit(20)
        # self.pipeStatusToLogger.emit('Cropping of AM finished')
        # self.pipeStatusToLogger.emit('Ablation mark filtering started')
        #
        # filter_fiducials = FindFilterFiducials()
        # self.pipeStatusToLogger.emit("Searching for fiducials started")
        # filter_fiducials.step1()
        # self.progressBarSig.emit(30)
        # self.pipeStatusToLogger.emit("Searching for fiducials finished")
        # self.pipeStatusToLogger.emit('Fiducials filtering on PRE maldi image started')
        # filter_fiducials.step2()
        # self.progressBarSig.emit(40)
        # self.pipeStatusToLogger.emit('Fiducials filtering on PRE maldi image finished')
        # reg_pre_post = RegisterPrePostMaldi()
        # self.pipeStatusToLogger.emit('Registration of Pre and Post maldi fidicuals and metaspace based annotation started')
        # reg_pre_post.step1()
        # self.pipeStatusToLogger.emit('Registration of Pre and Post maldi fidicuals and metaspace based annotation finished')
        # self.progressBarSig.emit(65)

        # cell_seg = CellSegment()
        # cell_seg.step3()

        gen_csv_features = GenerateCSV()
        gen_csv_features.step1()

class SpaceMApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SpaceMApp, self).__init__(parent)
        self.setupUi(self)
        self.btnStartAnalysis.clicked.connect(self.run_pipe)
        self.run_new_Thread = NewThread()
        self.inp_path = ''
        self.python_path = ''
        self.stitchedImgPreMPath = ''
        self.stitchedImgPostMPath = ''
        self.composite_img_path = ''
        self.fiji_path = ''
        self.cellprofiler_path = ''

    def run_pipe(self):
        self.inp_path = self.widget.get_main_folder()
        self.python_path = self.widget.lineEditPythonPath.text()
        self.stitchedImgPreMPath = self.widget.get_stitched_img_prem_path()
        self.stitchedImgPostMPath = self.widget.get_stitched_img_postm_path()
        self.composite_img_path = self.widget.get_composite_img_path()
        self.fiji_path = self.widget.get_fiji_path()
        self.cellprofiler_path = self.widget.get_cellprofiler_path()
        #
        # if self.inp_path and self.python_path and self.stitchedImgPreMPath and self.stitchedImgPostMPath \
        #         and self.composite_img_path and self.fiji_path:
        self.run_new_Thread.start()
        self.run_new_Thread.progressBarSig.connect(self.update_pb)
        self.run_new_Thread.pipeStatusToLogger.connect(self.update_logger)
        # else:
        #     QMessageBox.warning(self, "Warning", "Please check that all inputs are correctly entered and not empty")

    def update_pb(self, val):
        self.progressBar.setValue(val)

    def update_logger(self, val):
        logging.info(val)
        with open('./spaceM.log', 'r') as f:
            self.LogsTextBrowser.setText(f.read())

    def run(self):
        if global_vars.inp_path and global_vars.python_path and global_vars.stitchedImgPath:
            cell_seg = CellSegment()
            cell_seg.step1()
            self.progressBar.setValue(68)
            cell_seg.step2()
            self.progressBar.setValue(75)
            cell_seg.step3()
            self.progressBar.setValue(80)

            gen_csv = GenerateCSV()
            gen_csv.step1()
            self.progressBar.setValue(100)

def main():
    app = QApplication(sys.argv)
    form = SpaceMApp()
    form.show()
    app.exec()


if __name__ == '__main__':
    main()