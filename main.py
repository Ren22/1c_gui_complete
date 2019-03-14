import sys, json
from mainwindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, QRegExp, QThread
from pipelineController import *
import logging
from gen_settings.gen_settings import Gen_Settings as GS
from gen_settings.gen_settings_ui import Ui_gen_settings

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


class CallBacks(GS):
    def import_settings(self):
        print('here')
        if os.path.exists('./configs/settings.json'):
            with open('./configs/settings.json') as f:
                settings = json.load(f)
                # print(settings['inp_path'])
                self.lineEditMainFolder.setText(settings['inp_path'])
                self.lineEditMainFolder.repaint()
                # GS.set_main_folder(settings['inp_path'])


class SpaceMApp(QMainWindow, Ui_MainWindow, Ui_gen_settings):
    def __init__(self, parent=None):
        super(SpaceMApp, self).__init__(parent)
        self.setupUi(self)
        self.connect_callbacks()
        self.run_new_Thread = NewThread()
        self.inp_path = ''
        self.python_path = ''
        self.cellprofiler_path = ''

        self.stitchedPreMImage = ''
        self.stitchedPostMImage = ''
        self.stitPreMDapiImage = ''
        self.stitPostMDapiImage = ''
        self.stitPreMSampleImage = ''
        self.compositeImg = ''
        self.CPpipeFile = ''
        self.udpFile = ''
        self.imzMLName = ''
        self.metadata = ''

        self.MSLogin = ''
        self.MSPass = ''

    def connect_callbacks(self):
        cb = CallBacks()
        self.btnStartAnalysis.clicked.connect(self.run_pipe)
        self.btnImprtSettings.clicked.connect(cb.import_settings)

    def run_pipe(self):
        self.inp_path = self.widget1.get_main_folder()
        self.python_path = self.widget1.get_python()
        self.cellprofiler_path = self.widget1.get_cellprofiler()

        self.stitchedPreMImage = self.widget1.get_stitchedPreMImage()
        self.stitchedPostMImage = self.widget1.get_stitchedPostMImage()
        self.stitPreMDapiImage = self.widget1.get_stitPreMDapiImage()
        self.stitPostMDapiImage = self.widget1.get_stitPostMDapiImage()
        self.stitPreMSampleImage = self.widget1.get_stitPreMSampleImage()
        self.compositeImg = self.widget1.get_compositeImg()
        self.CPpipeFile = self.widget1.get_CPpipeFile()
        self.udpFile = self.widget1.get_udpFile()
        self.imzMLName = self.widget1.get_imzMLName()
        self.metadata = self.widget1.get_metadata()

        self.MSLogin = self.widget1.get_MSLogin()
        self.MSPass = self.widget1.get_MSPass()

        if self.inp_path and self.python_path and self.stitchedPreMImage and \
            self.stitchedPostMImage and self.stitPreMDapiImage and self.stitPostMDapiImage and self.stitPreMSampleImage \
            and self.compositeImg and self.udpFile and self.imzMLName \
                and self.metadata and self.MSLogin and self.MSPass:
            self.run_new_Thread.start()
            self.run_new_Thread.progressBarSig.connect(self.update_pb)
            self.run_new_Thread.pipeStatusToLogger.connect(self.update_logger)
        else:
            print(self.inp_path, self.python_path, self.cellprofiler_path, self.stitchedPreMImage, \
            self.stitchedPostMImage , self.stitPreMDapiImage , self.stitPostMDapiImage , self.stitPreMSampleImage, \
            self.compositeImg, self.udpFile, self.imzMLName, \
            self.metadata, self.MSLogin, self.MSPass)
            QMessageBox.warning(self, "Warning", "Please check that all inputs are correctly entered and are not empty")


    # #     TODO: DEV only - bypassing all checks
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