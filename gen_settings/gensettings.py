from PyQt5.QtWidgets import *
from global_vars import global_vars


class GenSettings():
    def __init__(self, ext_obj):
        ext_obj.btnMainFolder.clicked.connect(lambda: self.define_main_folder(ext_obj))
        ext_obj.btnPython.clicked.connect(lambda: self.define_python(ext_obj))
        ext_obj.btnCellProfiler.clicked.connect(lambda: self.define_cellprofiler(ext_obj))
    
        ext_obj.btnStitchedPreMBfImg.clicked.connect(lambda: self.define_stitched_img_prem_bf(ext_obj))
        ext_obj.btnStitchedPostMBfImg.clicked.connect(lambda: self.define_stitched_img_postm_bf(ext_obj))
        ext_obj.btnStitchedPreMDapiImg.clicked.connect(lambda: self.define_stitched_img_prem_dapi(ext_obj))
        ext_obj.btnStitchedPostMDapiImg.clicked.connect(lambda: self.define_stitched_img_postm_dapi(ext_obj))
        ext_obj.btnStitchedPreMSampleImg.clicked.connect(lambda: self.define_stitched_img_prem_sample(ext_obj))
        ext_obj.btnCompositeImg.clicked.connect(lambda: self.define_composite_img(ext_obj))
        ext_obj.btnCpPipeFile.clicked.connect(lambda: self.define_cp_pipeline(ext_obj))
    
        ext_obj.btnUdpFile.clicked.connect(lambda: self.define_udp_file(ext_obj))
        ext_obj.btnImzMLFilename.clicked.connect(lambda: self.define_Imzml_file(ext_obj))
        ext_obj.btnMALDImetadata.clicked.connect(lambda: self.define_maldi_metadata(ext_obj))
    
        ext_obj.lineEditMainFolder.textChanged[str].connect(lambda: self.set_main_folder(ext_obj))
        ext_obj.lineEditPythonPath.textChanged[str].connect(lambda: self.set_python(ext_obj))
        ext_obj.lineEditCellProfiler.textChanged[str].connect(lambda: self.set_cellprofiler(ext_obj))
    
        ext_obj.lineEditStitchedPreMImage.textChanged[str].connect(lambda: self.set_stitchedPreMImage(ext_obj))
        ext_obj.lineEditStitchedPostMImage.textChanged[str].connect(lambda: self.set_stitchedPostMImage(ext_obj))
        ext_obj.lineEditStitPreMDapiImage.textChanged[str].connect(lambda: self.set_stitPreMDapiImage(ext_obj))
        ext_obj.lineEditStitPostMDapiImage.textChanged[str].connect(lambda: self.set_stitPostMDapiImage(ext_obj))
        ext_obj.lineEditStitPreMSampleImage.textChanged[str].connect(lambda: self.set_stitPreMSampleImage(ext_obj))
        ext_obj.lineEditCompositeImg.textChanged[str].connect(lambda: self.set_compositeImg(ext_obj))
        ext_obj.lineEditCPpipeFile.textChanged[str].connect(lambda: self.set_CPpipeFile(ext_obj))
    
        ext_obj.lineEditUdpFile.textChanged[str].connect(lambda: self.set_udpFile(ext_obj))
        ext_obj.lineEditimzMLName.textChanged[str].connect(lambda: self.set_imzMLName(ext_obj))
        ext_obj.lineEditMetadata.textChanged[str].connect(lambda: self.set_metadata(ext_obj))
    
        ext_obj.lineEditMSLogin.textChanged[str].connect(lambda: self.set_MSLogin(ext_obj))
        ext_obj.lineEditMSPass.textChanged[str].connect(lambda: self.set_MSPass(ext_obj))

    @staticmethod
    def dir_path_finder(ext_obj):
        input_dir = ''
        try:
            input_dir = QFileDialog.getExistingDirectory(ext_obj, 'Select a folder:')
        except Exception as e:
            print('Directory cannot be opened')
            print(e, e.args)
        return input_dir

    @staticmethod
    def file_path_finder(ext_obj):
        input_dir = ''
        try:
            input_dir, _ = QFileDialog.getOpenFileName(ext_obj, 'Select a file:')
        except Exception as e:
            print('File cannot be opened')
            print(e, e.args)
        return input_dir

    def define_main_folder(self, ext_obj):
        path = self.dir_path_finder(ext_obj)
        global_vars.set_inp_path(path)
        ext_obj.lineEditMainFolder.setText(path)

    def define_python(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_python_path(path)
        ext_obj.lineEditPythonPath.setText(path)

    def define_cellprofiler(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_cellprofiler_path(path)
        ext_obj.lineEditCellProfiler.setText(path)

    def define_stitched_img_prem_bf(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_pre_stitched_image_bf_path(path)
        ext_obj.lineEditStitchedPreMImage.setText(path)

    def define_stitched_img_postm_bf(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_post_stitched_image_bf_path(path)
        ext_obj.lineEditStitchedPostMImage.setText(path)

    def define_stitched_img_prem_dapi(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_pre_stitched_image_dapi_path(path)
        ext_obj.lineEditStitPreMDapiImage.setText(path)

    def define_stitched_img_postm_dapi(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_post_stitched_image_dapi_path(path)
        ext_obj.lineEditStitPostMDapiImage.setText(path)

    def define_stitched_img_prem_sample(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_prem_stitched_image_sample_path(path)
        ext_obj.lineEditStitPreMSampleImage.setText(path)

    def define_composite_img(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_composite_path(path)
        ext_obj.lineEditCompositeImg.setText(path)

    def define_cp_pipeline(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_cp_pipe_path(path)
        ext_obj.lineEditCPpipeFile.setText(path)

    def define_udp_file(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_udpfile_path(path)
        ext_obj.lineEditUdpFile.setText(path)

    def define_Imzml_file(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_imzMLName(path)
        ext_obj.lineEditimzMLName.setText(path)

    def define_maldi_metadata(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.set_maldiMetadata_path(path)
        ext_obj.lineEditMetadata.setText(path)

    '''Setters for paths'''
    @staticmethod
    def set_main_folder(ext_obj):
        global_vars.set_inp_path(ext_obj.lineEditMainFolder.text())

    @staticmethod
    def set_python(ext_obj):
        global_vars.set_python_path(ext_obj.lineEditPythonPath.text())

    @staticmethod
    def set_cellprofiler(ext_obj):
        global_vars.set_cellprofiler_path(ext_obj.lineEditCellProfiler.text())

    @staticmethod
    def set_stitchedPreMImage(ext_obj):
        global_vars.set_pre_stitched_image_bf_path(ext_obj.lineEditStitchedPreMImage.text())

    @staticmethod
    def set_stitchedPostMImage(ext_obj):
        global_vars.set_post_stitched_image_bf_path(ext_obj.lineEditStitchedPostMImage.text())

    @staticmethod
    def set_stitPreMDapiImage(ext_obj):
        global_vars.set_pre_stitched_image_dapi_path(ext_obj.lineEditStitPreMDapiImage.text())

    @staticmethod
    def set_stitPostMDapiImage(ext_obj):
        global_vars.set_post_stitched_image_dapi_path(ext_obj.lineEditStitPostMDapiImage.text())

    @staticmethod
    def set_stitPreMSampleImage(ext_obj):
        global_vars.set_prem_stitched_image_sample_path(ext_obj.lineEditStitPreMSampleImage.text())

    @staticmethod
    def set_compositeImg(ext_obj):
        global_vars.set_composite_path(ext_obj.lineEditCompositeImg.text())

    @staticmethod
    def set_CPpipeFile(ext_obj):
        global_vars.set_cp_pipe_path(ext_obj.lineEditCPpipeFile.text())

    @staticmethod
    def set_udpFile(ext_obj):
        global_vars.set_udpfile_path(ext_obj.lineEditUdpFile.text())

    @staticmethod
    def set_imzMLName(ext_obj):
        global_vars.set_imzMLName(ext_obj.lineEditimzMLName.text())

    @staticmethod
    def set_metadata(ext_obj):
        global_vars.set_maldiMetadata_path(ext_obj.lineEditMetadata.text())

    @staticmethod
    def set_MSLogin(ext_obj):
        global_vars.set_MS_login(ext_obj.lineEditMSLogin.text())

    @staticmethod
    def set_MSPass(ext_obj):
        global_vars.set_MS_pass(ext_obj.lineEditMSPass.text())

    '''Getters'''
    @staticmethod
    def get_main_folder(ext_obj):
        return ext_obj.lineEditMainFolder.text()
    
    @staticmethod
    def get_python(ext_obj):
        return ext_obj.lineEditPythonPath.text()

    @staticmethod 
    def get_cellprofiler(ext_obj):
        return ext_obj.lineEditCellProfiler.text()

    @staticmethod 
    def get_stitchedPreMImage(ext_obj):
        return ext_obj.lineEditStitchedPreMImage.text()

    @staticmethod 
    def get_stitchedPostMImage(ext_obj):
        return ext_obj.lineEditStitchedPostMImage.text()

    @staticmethod 
    def get_stitPreMDapiImage(ext_obj):
        return ext_obj.lineEditStitPreMDapiImage.text()

    @staticmethod 
    def get_stitPostMDapiImage(ext_obj):
        return ext_obj.lineEditStitPostMDapiImage.text()

    @staticmethod 
    def get_stitPreMSampleImage(ext_obj):
        return ext_obj.lineEditStitPreMSampleImage.text()

    @staticmethod 
    def get_compositeImg(ext_obj):
        return ext_obj.lineEditCompositeImg.text()

    @staticmethod 
    def get_CPpipeFile(ext_obj):
        return ext_obj.lineEditCPpipeFile.text()

    @staticmethod 
    def get_udpFile(ext_obj):
        return ext_obj.lineEditUdpFile.text()

    @staticmethod 
    def get_imzMLName(ext_obj):
        return ext_obj.lineEditimzMLName.text()

    @staticmethod 
    def get_metadata(ext_obj):
        return ext_obj.lineEditMetadata.text()

    @staticmethod 
    def get_MSLogin(ext_obj):
        return ext_obj.lineEditMSLogin.text()

    @staticmethod 
    def get_MSPass(ext_obj):
        return ext_obj.lineEditMSPass.text()
