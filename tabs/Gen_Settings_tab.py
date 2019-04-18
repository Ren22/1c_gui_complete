from PyQt5.QtWidgets import *
from global_vars.global_vars import global_vars


class GenSettingsTab():
    def __init__(self, ext_obj):
        ext_obj.btnMainFolder.clicked.connect(lambda: self.define_main_folder(ext_obj))
        ext_obj.btnPython.clicked.connect(lambda: self.define_python(ext_obj))
        ext_obj.btnCellProfiler.clicked.connect(lambda: self.define_cellprofiler(ext_obj))
    
        ext_obj.btnStitchedPreMBfImg.clicked.connect(lambda: self.define_stitched_img_prem_bf(ext_obj))
        ext_obj.btnStitchedPostMBfImg.clicked.connect(lambda: self.define_stitched_img_postm_bf(ext_obj))

        ext_obj.btnUdpFile.clicked.connect(lambda: self.define_udp_file(ext_obj))
        ext_obj.btnMicroscopyMetadata.clicked.connect(lambda: self.define_micriscopy_metadata(ext_obj))
    
        ext_obj.lineEditMainFolder.textChanged[str].connect(lambda: self.set_main_folder(ext_obj))
        ext_obj.lineEditPythonPath.textChanged[str].connect(lambda: self.set_python(ext_obj))
        ext_obj.lineEditCellProfiler.textChanged[str].connect(lambda: self.set_cellprofiler(ext_obj))
    
        ext_obj.lineEditStitchedPreMImage.textChanged[str].connect(lambda: self.set_stitchedPreMImage(ext_obj))
        ext_obj.lineEditStitchedPostMImage.textChanged[str].connect(lambda: self.set_stitchedPostMImage(ext_obj))

        ext_obj.lineEditUdpFile.textChanged[str].connect(lambda: self.set_udpFile(ext_obj))
        ext_obj.lineEditMetadata.textChanged[str].connect(lambda: self.set_metadata(ext_obj))

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
        global_vars.inpPath = path
        ext_obj.lineEditMainFolder.setText(path)

    def define_python(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.pythonPath = path
        ext_obj.lineEditPythonPath.setText(path)

    def define_cellprofiler(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.cellprofilerPath = path
        ext_obj.lineEditCellProfiler.setText(path)



    def define_stitched_img_prem_bf(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.stitchedImgPreMPath = path
        ext_obj.lineEditStitchedPreMImage.setText(path)

    def define_stitched_img_postm_bf(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.stitchedImgPostMPath = path
        ext_obj.lineEditStitchedPostMImage.setText(path)


    def define_udp_file(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.udpFile = path
        ext_obj.lineEditUdpFile.setText(path)

    def define_msDsName(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.msDSName = path
        ext_obj.lineEditMSDsName.setText(path)

    def define_micriscopy_metadata(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.microscopyMetadata = path
        ext_obj.lineEditMetadata.setText(path)


    '''Setters for paths'''

    @staticmethod
    def set_main_folder(ext_obj):
        global_vars.inpPath = ext_obj.lineEditMainFolder.text()

    @staticmethod
    def set_python(ext_obj):
        global_vars.pythonPath = ext_obj.lineEditPythonPath.text()

    @staticmethod
    def set_cellprofiler(ext_obj):
        global_vars.cellprofilerPath = ext_obj.lineEditCellProfiler.text()

    @staticmethod
    def set_stitchedPreMImage(ext_obj):
        global_vars.stitchedImgPreMPath = ext_obj.lineEditStitchedPreMImage.text()

    @staticmethod
    def set_stitchedPostMImage(ext_obj):
        global_vars.stitchedImgPostMPath = ext_obj.lineEditStitchedPostMImage.text()

    @staticmethod
    def set_udpFile(ext_obj):
        global_vars.udpFile = ext_obj.lineEditUdpFile.text()

    @staticmethod
    def set_metadata(ext_obj):
        global_vars.microscopyMetadata = ext_obj.lineEditMetadata.text()


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
