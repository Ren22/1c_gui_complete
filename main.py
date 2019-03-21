import sys, json
from mainwindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
import logging
from gen_settings.gensettings import GenSettings as gs
from pipelineController import *
from workers.Am_worker import AMWorker
from workers.Full_pipe_worker import FullPipeWorker

if not os.path.exists('./logs'):
    os.makedirs('./logs')
if not os.path.exists('./configs/spaceM.log'):
    with open('./configs/spaceM.log', 'w') as log_file:
        log_file.write('')
logging.basicConfig(
        filename='./logs/spaceM.log',
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)

logging.info("Running spaceM v0.1")

class SpaceMApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SpaceMApp, self).__init__(parent)
        self.step = 0
        self.setupUi(self)
        self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'gen_settings'))
        gs(self)
        self.connect_callbacks()
        self.set_btns_static_state()
        self.setup_workers()

    def setup_workers(self):
        self.setup_am_thread()
        # self.setup_thread()

    # def setup_thread(self):
    #     self.thread = QThread()
    #     self.worker = MyWorker()
    #     self.worker.moveToThread(self.thread)
    #     self.thread.started.connect(self.worker.work_1)
    #     self.worker.progressBarSig.connect(self.update_pb)
    #     self.worker.pipeStatusToLogger.connect(self.update_logger)
    #     self.worker.changeTabSig.connect(self.update_tab)

    def setup_am_thread(self):
        self.thread_0 = QThread()
        self.worker_0 = AMWorker()
        self.worker_0.moveToThread(self.thread_0)
        self.thread_0.started.connect(self.worker_0.work_1)
        self.worker_0.progressBarSig.connect(self.update_pb)
        self.worker_0.pipeStatusToLogger.connect(self.update_logger)
        self.worker_0.incrementStepSig.connect(self.increment_step)
        self.worker_0.changeTabSig.connect(self.update_tab)

        self.thread_1 = QThread()
        self.worker_1 = AMWorker()
        self.worker_1.moveToThread(self.thread_1)
        self.thread_1.started.connect(self.worker_1.work_2)
        self.worker_1.progressBarSig.connect(self.update_pb)
        self.worker_1.pipeStatusToLogger.connect(self.update_logger)
        self.worker_1.incrementStepSig.connect(self.increment_step)
        self.worker_1.changeTabSig.connect(self.update_tab)

    def set_btns_static_state(self):
        self.btnImprtSettings.setEnabled(True)
        self.btnSaveSettings.setEnabled(True)
        if self.step == 0:
            self.btnRepeatStep.setEnabled(False)
        else:
            self.btnRepeatStep.setEnabled(True)
        self.btnRunNextStep.setEnabled(True)
        self.btnStartAnalysis.setEnabled(True)

    def set_btns_running_state(self):
        self.btnImprtSettings.setEnabled(False)
        self.btnSaveSettings.setEnabled(False)
        self.btnRepeatStep.setEnabled(False)
        self.btnRunNextStep.setEnabled(False)
        self.btnStartAnalysis.setEnabled(False)

    def connect_callbacks(self):
        self.btnImprtSettings.clicked.connect(self.import_settings)
        self.btnRunNextStep.clicked.connect(self.run_prev_or_next_step)
        self.btnRepeatStep.clicked.connect(self.repeat_step)
        self.btnStartAnalysis.clicked.connect(self.run_pipe)

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

    def increment_step(self):
        self.step += 1

    def decrement_step(self):
        self.step -= 1

    def repeat_step(self):
        self.decrement_step()
        self.run_prev_or_next_step()

    def run_prev_or_next_step(self):
        if self.step == 0:
            self.set_btns_running_state()
            self.thread_0.start()
        elif self.step == 1:
            self.set_btns_running_state()
            self.thread_1.start()

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
            self.stitchedPostMImage and self.stitPreMDapiImage and self.stitPostMDapiImage  \
            and self.compositeImg and self.udpFile and self.imzMLName \
                and self.metadata:
            self.thread.start()

        else:
            print(self.inp_path, self.python_path, self.cellprofiler_path, self.stitchedPreMImage, \
            self.stitchedPostMImage , self.stitPreMDapiImage , self.stitPostMDapiImage, \
            self.compositeImg, self.udpFile, self.imzMLName, \
            self.metadata)
            QMessageBox.warning(self, "Warning", "Please check that all inputs are correctly entered and are not empty")

    #     TODO: DEV only - bypassing all checks
    #     self.run_new_Thread.start()
    #     self.run_new_Thread.progressBarSig.connect(self.update_pb)
    #     self.run_new_Thread.pipeStatusToLogger.connect(self.update_logger)

    def update_tab(self):
        if self.step == 1:
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'amf_tab'))
            self.set_btns_static_state()
            self.thread_0.terminate()
        elif self.step == 2:
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'fids_tab'))
            self.set_btns_static_state()
            self.thread_1.terminate()

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