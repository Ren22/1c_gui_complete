import sys, json
from mainwindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
import logging
from global_vars.global_vars import GlobalVars as gv
from tabs.Am_finder_tab import AmFinderTab as amfTab
from tabs.Gen_Settings_tab import GenSettingsTab as gsTab
from tabs.Grab_ms_data_tab import GrabMSDataTab as gmsTab
from tabs.GenCsv_tab import GenCsvTab as genCsvTab
from pipelineController import *
from workers.Full_pipe_worker import FullPipeWorker
from workers.Am_finder_worker import AMWorker
from workers.Fudicials_filter_worker import FidFilterWorker
from workers.Reg_image_worker import RegImageWorker
from workers.Grab_ms_data_worker import GrabMSDataWorker
from workers.Cell_profiler_worker import CPWorker
from workers.Gen_csv_worker import GenCSVWorker
from sys import platform


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
        self.step = 7
        self.setupUi(self)
        self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'global_vars'))
        self.setup_tabs()
        self.setup_workers()
        self.connect_callbacks()
        self.set_btns_static_state()

    def setup_workers(self):
        self.setup_full_thread()
        self.setup_am_thread()
        self.setup_fid_filter_thread()
        self.setup_reg_image_thread()
        self.setup_grab_ms_data_thread()
        self.setup_cellprof_thread()
        self.setup_cellprof_postproc_thread()
        self.setup_gen_csv_thread()

    def setup_tabs(self):
        gv()
        gsTab(self)
        amfTab(self)
        gmsTab(self)
        genCsvTab(self)

    def setup_full_thread(self):
        self.thread_full = QThread()
        self.worker = FullPipeWorker()
        self.worker.moveToThread(self.thread_full)
        self.thread_full.started.connect(self.worker.work_full)
        self.worker.finishPipeSig.connect(self.fullpipe_finished)
        self.worker.progressBarSig.connect(self.update_pb)
        self.worker.pipeStatusToLogger.connect(self.update_logger)

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

    def setup_reg_image_thread(self):
        self.thread_3 = QThread()
        self.worker_3 = RegImageWorker()
        self.worker_3.moveToThread(self.thread_3)
        self.thread_3.started.connect(self.worker_3.work_1)
        self.worker_3.progressBarSig.connect(self.update_pb)
        self.worker_3.pipeStatusToLogger.connect(self.update_logger)
        self.worker_3.incrementStepSig.connect(self.increment_step)
        self.worker_3.changeTabSig.connect(self.update_tab)

    def setup_grab_ms_data_thread(self):
        self.thread_4 = QThread()
        self.worker_4 = GrabMSDataWorker()
        self.worker_4.moveToThread(self.thread_4)
        self.thread_4.started.connect(self.worker_4.work_1)
        self.worker_4.progressBarSig.connect(self.update_pb)
        self.worker_4.pipeStatusToLogger.connect(self.update_logger)
        self.worker_4.incrementStepSig.connect(self.increment_step)
        self.worker_4.changeTabSig.connect(self.update_tab)

    def setup_cellprof_thread(self):
        self.thread_5 = QThread()
        self.worker_5 = CPWorker()
        self.worker_5.moveToThread(self.thread_5)
        self.thread_5.started.connect(self.worker_5.work_1)
        self.worker_5.progressBarSig.connect(self.update_pb)
        self.worker_5.pipeStatusToLogger.connect(self.update_logger)
        self.worker_5.incrementStepSig.connect(self.increment_step)
        self.worker_5.changeTabSig.connect(self.update_tab)
        
    def setup_cellprof_postproc_thread(self):
        self.thread_6 = QThread()
        self.worker_6 = CPWorker()
        self.worker_6.moveToThread(self.thread_6)
        self.thread_6.started.connect(self.worker_6.work_2)
        self.worker_6.progressBarSig.connect(self.update_pb)
        self.worker_6.pipeStatusToLogger.connect(self.update_logger)
        self.worker_6.incrementStepSig.connect(self.increment_step)
        self.worker_6.changeTabSig.connect(self.update_tab)
        
    def setup_gen_csv_thread(self):
        self.thread_7 = QThread()
        self.worker_7 = GenCSVWorker()
        self.worker_7.moveToThread(self.thread_7)
        self.thread_7.started.connect(self.worker_7.work_1)
        self.worker_7.progressBarSig.connect(self.update_pb)
        self.worker_7.pipeStatusToLogger.connect(self.update_logger)
        self.worker_7.incrementStepSig.connect(self.increment_step)
        self.worker_7.changeTabSig.connect(self.update_tab)

    def set_btns_static_state(self):
        self.btnImprtSettings.setEnabled(True)
        self.btnSaveSettings.setEnabled(True)
        if self.step == 8:
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
        self.btnStartAnalysis.clicked.connect(self.run_full_pipe_check)

    def import_settings(self):
        if os.path.exists('./configs/settings.json'):
            with open('./configs/settings.json') as f:
                settings = json.load(f)
                self.lineEditMainFolder.setText(settings['inp_path'])
                self.lineEditPythonPath.setText(settings['python_path'])
                self.lineEditCellProfiler.setText(settings['cellprofilerPath'])

                self.lineEditStitchedPreMImage.setText(settings['stitchedImgPreMPath'])
                self.lineEditStitchedPostMImage.setText(settings['stitchedImgPostMPath'])

                self.lineEditUdpFile.setText(settings['udpFile'])
                self.lineEditMetadata.setText(settings['maldiMetadata'])

                self.tab_amf_FluoCh.setText(settings['postMaldiDapi'])
                self.tab_amf_ifftImgPath.setText(settings['manProcessedImgPath'])

                self.tab_gms_lineEditMSDs.setText(settings['MSDsName'])

                self.lineEditCPpipeFile.setText(settings['cpPipeLine'])

                self.tab_csvGen_lineEditCells.setText(settings['csvCellsPath'])
        else:
            QMessageBox.warning(self, "Warning", "No settings file found!")
            Exception('Settings file was not found or does not exist')

    def increment_step(self):
        self.step += 1
        print(self.step)

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

    def validate_inputs(self):
        if self.step == 0:
            check_line = global_vars.inpPath and global_vars.pythonPath and global_vars.stitchedImgPreMPath \
            and global_vars.stitchedImgPostMPath and global_vars.udpFile and global_vars.maldiMetadata
            if platform == "win32":
                check_line = check_line and global_vars.cellprofilerPath
            if check_line == '':
                QMessageBox.warning(self, "Warning", "Please check that all inputs are correctly entered and are "
                                                     "not empty for general settings")
            else:
                return True
        elif self.step == 1:
            if global_vars.tab_amf_postMaldiDapi == '' and self.tab_amf_cbMatrix.currentText() == 'DHB' or \
                self.tab_amf_manFftRb.isChecked() and global_vars.tab_amf_ifftImage == '':
                QMessageBox.warning(self, "Warning", "Please check that all inputs are correctly entered and are "
                                                     "not empty for general settings")
            else:
                return True
        elif self.step == 4:
            prev_checks = global_vars.inpPath and global_vars.pythonPath and global_vars.stitchedImgPreMPath \
            and global_vars.stitchedImgPostMPath and global_vars.udpFile and global_vars.maldiMetadata and \
            (global_vars.tab_amf_postMaldiDapi == '' and self.tab_amf_cbMatrix.currentText() == 'DHB' or \
                self.tab_amf_manFftRb.isChecked() and global_vars.tab_amf_ifftImage == '')
            if global_vars.tab_gms_msDSName == '':
                QMessageBox.warning(self, "Warning", "Please make sure that your provided the name of the "
                                                     "dataset")
            elif prev_checks == '':
                QMessageBox.warning(self, "Warning", "Please make sure that all the paths from the previous steps "
                                                     "are provided")
            else:
                return True
        elif self.step == 7:
            prev_checks = global_vars.inpPath and global_vars.pythonPath and global_vars.stitchedImgPreMPath \
                          and global_vars.stitchedImgPostMPath and global_vars.udpFile and global_vars.maldiMetadata and \
                          (global_vars.tab_amf_postMaldiDapi == '' and self.tab_amf_cbMatrix.currentText() == 'DHB' or \
                           self.tab_amf_manFftRb.isChecked() and global_vars.tab_amf_ifftImage == '') and \
                          global_vars.tab_gms_msDSName
            if global_vars.tab_genCsv_csvFilePath == '':
                QMessageBox.warning(self, "Warning", "Please make sure that your provided the csv file with features path")
            elif prev_checks == '':
                QMessageBox.warning(self, "Warning", "Please make sure that all the paths from the previous steps "
                                                     "are provided")
            else:
                return True

    '''Running threads of workers/Full pipeline'''
    def run_full_pipe(self):
        if self.validate_inputs():
            self.set_btns_running_state()
            self.thread_full.start()

    def run_full_pipe_check(self):
        if self.step != 0 and self.step != 8:
            btnRunPipeReply = QMessageBox.question(self, "Warning", "You are in the middle of running pipeline step by step wise, "
                                                    "running the full pipeline will start it from the first step again. "
                                                    "Are you sure you want to proceed?")
            if btnRunPipeReply == QMessageBox.Yes:
                self.run_full_pipe()
            else:
                print('Running the full pipeline was aborted.')
        else:
            self.run_full_pipe()

    def fullpipe_finished(self):
        self.thread_full.terminate()
        self.set_btns_static_state()

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
            self.tabWidget.setCurrentWidget(self.tabWidget.findChild(QWidget, 'csv_gen_tab'))
            self.set_btns_static_state()
            self.thread_6.terminate()
        elif self.step == 8:
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