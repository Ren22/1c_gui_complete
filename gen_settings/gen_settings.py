from .gen_settings_ui import Ui_gen_settings
from PyQt5.QtWidgets import *
from global_vars import global_vars


class Gen_Settings(QWidget, Ui_gen_settings):
    def __init__(self, parent=None):
        super(Gen_Settings, self).__init__(parent)
        self.setupUi(self)
        self.btnMainFolder.clicked.connect(self.define_main_folder)
        self.btnPython.clicked.connect(self.define_python)
        self.btnCellProfiler.clicked.connect(self.define_cellprofiler)

        self.btnStitchedPreMBfImg.clicked.connect(self.define_stitched_img_prem_bf)
        self.btnStitchedPostMBfImg.clicked.connect(self.define_stitched_img_postm_bf)
        self.btnStitchedPreMDapiImg.clicked.connect(self.define_stitched_img_prem_dapi)
        self.btnStitchedPostMDapiImg.clicked.connect(self.define_stitched_img_postm_dapi)
        self.btnStitchedPreMSampleImg.clicked.connect(self.define_stitched_img_prem_sample)
        self.btnCompositeImg.clicked.connect(self.define_composite_img)
        self.btnCpPipeFile.clicked.connect(self.define_cp_pipeline)

        self.btnUdpFile.clicked.connect(self.define_udp_file)
        self.btnImzMLFilename.clicked.connect(self.define_Imzml_file)
        self.btnMALDImetadata.clicked.connect(self.define_maldi_metadata)

        self.lineEditMainFolder.textChanged[str].connect(self.set_main_folder)
        self.lineEditPythonPath.textChanged[str].connect(self.set_python)
        self.lineEditCellProfiler.textChanged[str].connect(self.set_cellprofiler)

        self.lineEditStitchedPreMImage.textChanged[str].connect(self.set_stitchedPreMImage)
        self.lineEditStitchedPostMImage.textChanged[str].connect(self.set_stitchedPostMImage)
        self.lineEditStitPreMDapiImage.textChanged[str].connect(self.set_stitPreMDapiImage)
        self.lineEditStitPostMDapiImage.textChanged[str].connect(self.set_stitPostMDapiImage)
        self.lineEditStitPreMSampleImage.textChanged[str].connect(self.set_stitPreMSampleImage)
        self.lineEditCompositeImg.textChanged[str].connect(self.set_compositeImg)
        self.lineEditCPpipeFile.textChanged[str].connect(self.set_CPpipeFile)

        self.lineEditUdpFile.textChanged[str].connect(self.set_udpFile)
        self.lineEditimzMLName.textChanged[str].connect(self.set_imzMLName)
        self.lineEditMetadata.textChanged[str].connect(self.set_metadata)

        self.lineEditMSLogin.textChanged[str].connect(self.set_MSLogin)
        self.lineEditMSPass.textChanged[str].connect(self.set_MSPass)

        # self.lineEditMSDb
        # self.comboBoxFdr

    def dir_path_finder(self):
        input_dir = ''
        try:
            input_dir = QFileDialog.getExistingDirectory(self, 'Select a folder:')
        except Exception as e:
            print('Directory cannot be opened')
            print(e, e.args)
        return input_dir

    def file_path_finder(self):
        input_dir = ''
        try:
            input_dir, _ = QFileDialog.getOpenFileName(self, 'Select a file:')
        except Exception as e:
            print('File cannot be opened')
            print(e, e.args)
        return input_dir

    def define_main_folder(self):
        path = self.dir_path_finder()
        global_vars.set_inp_path(path)
        self.lineEditMainFolder.setText(path)

    def define_python(self):
        path = self.file_path_finder()
        global_vars.set_python_path(path)
        self.lineEditPythonPath.setText(path)

    def define_cellprofiler(self):
        path = self.file_path_finder()
        global_vars.set_cellprofiler_path(path)
        self.lineEditCellProfiler.setText(path)

    def define_stitched_img_prem_bf(self):
        path = self.file_path_finder()
        global_vars.set_pre_stitched_image_bf_path(path)
        self.lineEditStitchedPreMImage.setText(path)

    def define_stitched_img_postm_bf(self):
        path = self.file_path_finder()
        global_vars.set_post_stitched_image_bf_path(path)
        self.lineEditStitchedPostMImage.setText(path)

    def define_stitched_img_prem_dapi(self):
        path = self.file_path_finder()
        global_vars.set_pre_stitched_image_dapi_path(path)
        self.lineEditStitPreMDapiImage.setText(path)

    def define_stitched_img_postm_dapi(self):
        path = self.file_path_finder()
        global_vars.set_post_stitched_image_dapi_path(path)
        self.lineEditStitPostMDapiImage.setText(path)

    def define_stitched_img_prem_sample(self):
        path = self.file_path_finder()
        global_vars.set_prem_stitched_image_sample_path(path)
        self.lineEditStitPreMSampleImage.setText(path)

    def define_composite_img(self):
        path = self.file_path_finder()
        global_vars.set_composite_path(path)
        self.lineEditCompositeImg.setText(path)

    def define_cp_pipeline(self):
        path = self.file_path_finder()
        global_vars.set_cp_pipe_path(path)
        self.lineEditCPpipeFile.setText(path)

    def define_udp_file(self):
        path = self.file_path_finder()
        global_vars.set_udpfile_path(path)
        self.lineEditUdpFile.setText(path)

    def define_Imzml_file(self):
        path = self.file_path_finder()
        global_vars.set_imzMLName(path)
        self.lineEditimzMLName.setText(path)

    def define_maldi_metadata(self):
        path = self.file_path_finder()
        global_vars.set_maldiMetadata_path(path)
        self.lineEditMetadata.setText(path)

    '''Setters for paths'''
    def set_main_folder(self, path):
        self.lineEditMainFolder.setText(path)
        global_vars.set_inp_path(path)

    def set_python(self, path):
        global_vars.set_python_path(path)

    def set_cellprofiler(self, path):
        global_vars.set_cellprofiler_path(path)

    def set_stitchedPreMImage(self, path):
        global_vars.set_pre_stitched_image_bf_path(path)

    def set_stitchedPostMImage(self, path):
        global_vars.set_post_stitched_image_bf_path(path)

    def set_stitPreMDapiImage(self, path):
        global_vars.set_pre_stitched_image_dapi_path(path)

    def set_stitPostMDapiImage(self, path):
        global_vars.set_post_stitched_image_dapi_path(path)

    def set_stitPreMSampleImage(self, path):
        global_vars.set_prem_stitched_image_sample_path(path)

    def set_compositeImg(self, path):
        global_vars.set_composite_path(path)

    def set_CPpipeFile(self, path):
        global_vars.set_cp_pipe_path(path)

    def set_udpFile(self, path):
        global_vars.set_udpfile_path(path)

    def set_imzMLName(self, path):
        global_vars.set_imzMLName(path)

    def set_metadata(self, path):
        global_vars.set_maldiMetadata_path(path)

    def set_MSLogin(self, login):
        global_vars.set_MS_login(login)

    def set_MSPass(self, password):
        global_vars.set_MS_pass(password)

    '''Getters'''
    def get_main_folder(self):
        return self.lineEditMainFolder.text()

    def get_python(self):
        return self.lineEditPythonPath.text()

    def get_cellprofiler(self):
        return self.lineEditCellProfiler.text()

    def get_stitchedPreMImage(self):
        return self.lineEditStitchedPreMImage.text()

    def get_stitchedPostMImage(self):
        return self.lineEditStitchedPostMImage.text()

    def get_stitPreMDapiImage(self):
        return self.lineEditStitPreMDapiImage.text()

    def get_stitPostMDapiImage(self):
        return self.lineEditStitPostMDapiImage.text()

    def get_stitPreMSampleImage(self):
        return self.lineEditStitPreMSampleImage.text()

    def get_compositeImg(self):
        return self.lineEditCompositeImg.text()

    def get_CPpipeFile(self):
        return self.lineEditCPpipeFile.text()

    def get_udpFile(self):
        return self.lineEditUdpFile.text()

    def get_imzMLName(self):
        return self.lineEditimzMLName.text()

    def get_metadata(self):
        return self.lineEditMetadata.text()

    def get_MSLogin(self):
        return self.lineEditMSLogin.text()

    def get_MSPass(self):
        return self.lineEditMSPass.text()
