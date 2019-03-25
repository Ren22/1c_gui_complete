import sys, json
from mainwindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
import logging
from gen_settings.gensettings import GenSettings as gs
from tabs.Am_finder_tab import AmFinderTab as amfTab
from pipelineController import *
from workers.Full_pipe_worker import FullPipeWorker
from workers.Am_worker import AMWorker
from workers.Fudicials_filter_worker import FidFilterWorker
from workers.Reg_image_worker import RegImageWorker
from workers.Grab_ms_data_worker import GrabMSDataWorker
from workers.Cell_profiler_worker import CPWorker
from workers.Gen_csv_worker import GenCSVWorker

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
        amfTab(self)
        self.connect_callbacks()
        self.set_btns_static_state()
        self.setup_workers()

    def setup_workers(self):
        self.setup_full_thread()
        self.setup_am_thread()
        self.setup_fid_filter_thread()
        self.setup_reg_image_thread()
        self.setup_grab_ms_data_thread()
        self.setup_cellprof_thread()
        self.setup_cellprof_postproc_thread()
        self.setup_gen_csv_thread()

    def setup_full_thread(self):
        self.thread_full = QThread()
        self.worker = FullPipeWorker()
        self.worker.moveToThread(self.thread_full)
        self.thread_full.started.connect(self.worker.work_full)
        self.worker.progressBarSig.connect(self.update_pb)
        self.worker.pipeStatusToLogger.connect(self.update_logger)
        # self.worker.changeTabSig.connect(self.update_tab)

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

    def setup_fid_filter_thread(self):
        self.thread_2 = QThread()
        self.worker_2 = FidFilterWorker()
        self.worker_2.moveToThread(self.thread_2)
        self.thread_2.started.connect(self.worker_2.work_1)
        self.worker_2.progressBarSig.connect(self.update_pb)
        self.worker_2.pipeStatusToLogger.connect(self.update_logger)
        self.worker_2.incrementStepSig.connect(self.increment_step)
        self.worker_2.changeTabSig.connect(self.update_tab)

        self.thread_3 = QThread()
        self.worker_3 = FidFilterWorker()
        self.worker_3.moveToThread(self.thread_3)
        self.thread_3.started.connect(self.worker_3.work_2)
        self.worker_3.progressBarSig.connect(self.update_pb)
        self.worker_3.pipeStatusToLogger.connect(self.update_logger)
        self.worker_3.incrementStepSig.connect(self.increment_step)
        self.worker_3.changeTabSig.connect(self.update_tab)

    def setup_reg_image_thread(self):
        self.thread_4 = QThread()
        self.worker_4 = RegImageWorker()
        self.worker_4.moveToThread(self.thread_4)
        self.thread_4.started.connect(self.worker_4.work_1)
        self.worker_4.progressBarSig.connect(self.update_pb)
        self.worker_4.pipeStatusToLogger.connect(self.update_logger)
        self.worker_4.incrementStepSig.connect(self.increment_step)
        self.worker_4.changeTabSig.connect(self.update_tab)

    def setup_grab_ms_data_thread(self):
        self.thread_5 = QThread()
        self.worker_5 = GrabMSDataWorker()
        self.worker_5.moveToThread(self.thread_5)
        self.thread_5.started.connect(self.worker_5.work_1)
        self.worker_5.progressBarSig.connect(self.update_pb)
        self.worker_5.pipeStatusToLogger.connect(self.update_logger)
        self.worker_5.incrementStepSig.connect(self.increment_step)
        self.worker_5.changeTabSig.connect(self.update_tab)

    def setup_cellprof_thread(self):
        self.thread_6 = QThread()
        self.worker_6 = CPWorker()
        self.worker_6.moveToThread(self.thread_6)
        self.thread_6.started.connect(self.worker_6.work_1)
        self.worker_6.progressBarSig.connect(self.update_pb)
        self.worker_6.pipeStatusToLogger.connect(self.update_logger)
        self.worker_6.incrementStepSig.connect(self.increment_step)
        self.worker_6.changeTabSig.connect(self.update_tab)
        
    def setup_cellprof_postproc_thread(self):
        self.thread_7 = QThread()
        self.worker_7 = CPWorker()
        self.worker_7.moveToThread(self.thread_7)
        self.thread_7.started.connect(self.worker_7.work_2)
        self.worker_7.progressBarSig.connect(self.update_pb)
        self.worker_7.pipeStatusToLogger.connect(self.update_logger)
        self.worker_7.incrementStepSig.connect(self.increment_step)
        self.worker_7.changeTabSig.connect(self.update_tab)
        
    def setup_gen_csv_thread(self):
        self.thread_8 = QThread()
        self.worker_8 = GenCSVWorker()
        self.worker_8.moveToThread(self.thread_8)
        self.thread_8.started.connect(self.worker_8.work_1)
        self.worker_8.progressBarSig.connect(self.update_pb)
        self.worker_8.pipeStatusToLogger.connect(self.update_logger)
        self.worker_8.incrementStepSig.connect(self.increment_step)
        self.worker_8.changeTabSig.connect(self.update_tab)

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
        self.btnStartAnalysis.clicked.connect(self.run_full_pipe)

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
        if self.validate_inputs():
            if self.step == 0:
                self.set_btns_running_state()
                self.thread_0.start()
            elif self.step == 1:
                self.set_btns_running_state()
                self.thread_1.start()
            elif self.step == 2:
                self.set_btns_running_state()
                self.thread_2.start()
            elif self.step == 3:
                self.set_btns_running_state()
                self.thread_3.start()
            elif self.step == 4:
                self.set_btns_running_state()
                self.thread_4.start()
            elif self.step == 5:
                self.set_btns_running_state()
                self.thread_5.start()
            elif self.step == 6:
                self.set_btns_running_state()
                self.thread_6.start()
            elif self.step == 7:
                self.set_btns_running_state()
                self.thread_7.start()
            elif self.step == 8:
                self.set_btns_running_state()
                self.thread_8.start()

    def run_full_pipe(self):
        if self.validate_inputs():
            self.set_btns_running_state()
            self.thread_full.start()
            self.set_btns_static_state()

    def validate_inputs(self):
        self.inpPath = gs.get_main_folder(self)
        self.pythonPath = gs.get_python(self)
        self.cellprofilerPath = gs.get_cellprofiler(self)

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

        '''Tab 1'''
        #     TODO: DEV only - bypassing all checks
        #     self.run_new_Thread.start()
        #     self.run_new_Thread.progressBarSig.connect(self.update_pb)
        #     self.run_new_Thread.pipeStatusToLogger.connect(self.update_logger)

        if (self.inpPath and self.pythonPath and self.stitchedPreMImage and \
            self.stitchedPostMImage and self.stitPreMDapiImage and self.stitPostMDapiImage  \
            and self.compositeImg and self.udpFile and self.imzMLName \
                and self.metadata) == '':
            QMessageBox.warning(self, "Warning", "Please check that all inputs are correctly entered and are not empty")
        else:
            return True

    def update_tab(self):
        if self.step == 1:
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'amf_tab'))
            self.set_btns_static_state()
            self.thread_0.terminate()
        elif self.step == 2:
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'fids_tab'))
            self.set_btns_static_state()
            self.thread_1.terminate()
        elif self.step == 3:
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'reg_tab'))
            self.set_btns_static_state()
            self.thread_2.terminate()
        elif self.step == 4:
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'grab_ms_data_tab'))
            self.set_btns_static_state()
            self.thread_3.terminate()
        elif self.step == 5:
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'cell_segm_tab'))
            self.set_btns_static_state()
            self.thread_4.terminate()
        elif self.step == 6:
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'cell_segm_tab'))
            self.set_btns_static_state()
            self.thread_5.terminate()
        elif self.step == 7:
            self.set_btns_static_state()
            self.thread_6.terminate()
        elif self.step == 8:
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'csv_gen_tab'))
            self.set_btns_static_state()
            self.thread_7.terminate()

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