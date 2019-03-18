import sys, json
from mainwindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, QRegExp, QThread
from pipelineController import *
import logging
from gen_settings.gensettings import GenSettings as gs

if not os.path.exists('./logs'):
    os.makedirs('./logs')
if not os.path.exists('./configs/spaceM.log'):
    with open('./configs/spaceM.log', 'w') as log_file:
        log_file.write('')
logging.basicConfig(filename='./logs/spaceM.log',
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
        find_am = FindAMinPM()
        find_am.step1()
        self.progressBarSig.emit(10)
        self.pipeStatusToLogger.emit('CropPMimage finished')
        self.pipeStatusToLogger.emit('Ablation mark finder started')
        find_am.step2()

        self.progressBarSig.emit(20)
        self.pipeStatusToLogger.emit('Cropping of AM finished')
        self.pipeStatusToLogger.emit('Ablation mark filtering started')

        filter_fiducials = FindFilterFiducials()
        self.pipeStatusToLogger.emit("Searching for fiducials started")
        filter_fiducials.step1()
        self.progressBarSig.emit(30)
        self.pipeStatusToLogger.emit("Searching for fiducials finished")
        self.pipeStatusToLogger.emit('Fiducials filtering on PRE maldi image started')
        filter_fiducials.step2()
        self.progressBarSig.emit(40)
        self.pipeStatusToLogger.emit('Fiducials filtering on PRE maldi image finished')

        reg_pre_post = RegisterPrePostMaldi()
        self.pipeStatusToLogger.emit('Registration of Pre and Post maldi fidicuals and metaspace based annotation started')
        reg_pre_post.step1()
        self.pipeStatusToLogger.emit('Registration of Pre and Post maldi fidicuals and metaspace based annotation finished')
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


class SpaceMApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SpaceMApp, self).__init__(parent)
        self.setupUi(self)
        gs(self)
        self.connect_callbacks()
        self.run_new_Thread = NewThread()

    def connect_callbacks(self):
        self.btnStartAnalysis.clicked.connect(self.run_pipe)
        self.btnImprtSettings.clicked.connect(self.import_settings)

    def import_settings(self):
        if os.path.exists('./configs/settings.json'):
            with open('./configs/settings.json') as f:
                settings = json.load(f)
                self.lineEditMainFolder.setText(settings['inp_path'])
                self.lineEditPythonPath.setText(settings['python_path'])
                self.lineEditCellProfiler.setText(settings['cellprofilerPath'])

                self.lineEditStitchedPreMImage.setText(settings['stitchedImgPreMPath'])
                self.lineEditStitchedPostMImage.setText(settings['stitchedImgPostMPath'])
                self.lineEditStitPreMDapiImage.setText(settings['preMaldiDapi'])
                self.lineEditStitPostMDapiImage.setText(settings['postMaldiDapi'])
                self.lineEditStitPreMSampleImage.setText(settings['preMaldiSample'])
                self.lineEditCompositeImg.setText(settings['compositeImgPath'])
                self.lineEditCPpipeFile.setText(settings['cpPipeLine'])

                self.lineEditUdpFile.setText(settings['udpFile'])
                self.lineEditimzMLName.setText(settings['imzMLName'])
                self.lineEditMetadata.setText(settings['maldiMetadata'])

                self.lineEditMSLogin.setText(settings['MSLogin'])
                self.lineEditMSPass.setText(settings['MSPass'])
        else:
            QMessageBox.warning(self, "Warning", "No settings file found!")
            Exception('Settings file was not found or does not exist')

    def run_pipe(self):
        self.inp_path = gs.get_main_folder(self)
        self.python_path = gs.get_python(self)
        self.cellprofiler_path = gs.get_cellprofiler(self)

        self.stitchedPreMImage = gs.get_stitchedPreMImage(self)
        self.stitchedPostMImage = gs.get_stitchedPostMImage(self)
        self.stitPreMDapiImage = gs.get_stitPreMDapiImage(self)
        self.stitPostMDapiImage = gs.get_stitPostMDapiImage(self)
        self.stitPreMSampleImage = gs.get_stitPreMSampleImage(self)
        self.compositeImg = gs.get_compositeImg(self)
        self.CPpipeFile = gs.get_CPpipeFile(self)
        self.udpFile = gs.get_udpFile(self)
        self.imzMLName = gs.get_imzMLName(self)
        self.metadata = gs.get_metadata(self)

        self.MSLogin = gs.get_MSLogin(self)
        self.MSPass = gs.get_MSPass(self)

        if self.inp_path and self.python_path and self.stitchedPreMImage and \
            self.stitchedPostMImage and self.stitPreMDapiImage and self.stitPostMDapiImage and self.stitPreMSampleImage \
            and self.compositeImg and self.udpFile and self.imzMLName \
                and self.metadata :
            self.run_new_Thread.start()
            self.run_new_Thread.progressBarSig.connect(self.update_pb)
            self.run_new_Thread.pipeStatusToLogger.connect(self.update_logger)
        else:
            print(self.inp_path, self.python_path, self.cellprofiler_path, self.stitchedPreMImage, \
            self.stitchedPostMImage , self.stitPreMDapiImage , self.stitPostMDapiImage , self.stitPreMSampleImage, \
            self.compositeImg, self.udpFile, self.imzMLName, \
            self.metadata)
            QMessageBox.warning(self, "Warning", "Please check that all inputs are correctly entered and are not empty")

    #     TODO: DEV only - bypassing all checks
    #     self.run_new_Thread.start()
    #     self.run_new_Thread.progressBarSig.connect(self.update_pb)
    #     self.run_new_Thread.pipeStatusToLogger.connect(self.update_logger)

    def update_pb(self, val):
        self.progressBar.setValue(val)

    def update_logger(self, val):
        logging.info(val)
        with open('./logs/spaceM.log', 'r') as f:
            self.LogsTextBrowser.setText(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = SpaceMApp()
    form.show()
    app.exec()