from gen_settings_ui import Ui_gen_settings
from PyQt5.QtWidgets import *
from global_vars import GlobalVars, global_vars


class Gen_Settings(QWidget, Ui_gen_settings):
    def __init__(self, parent=None):
        super(Gen_Settings, self).__init__(parent)
        self.setupUi(self)
        self.btnMainFolder.clicked.connect(self.define_main_folder)
        self.btnPython.clicked.connect(self.define_python_path)
        self.btnStitchedPreImg.clicked.connect(self.stitched_img_prem_path)
        self.btnStitchedPostImg.clicked.connect(self.stitched_img_postm_path)
        self.btnCompositeImg.clicked.connect(self.define_composite_img_path)
        self.btnFiji.clicked.connect(self.define_fiji_path)
        self.btnCellProfiler.clicked.connect(self.define_cellprofiler_path)

        self.lineEditMainFolder.textChanged[str].connect(self.define_main_folder1)
        self.lineEditPythonPath.textChanged[str].connect(self.define_python_path1)
        self.lineEditStitchedPreImage.textChanged[str].connect(self.stitched_img_prem_path1)
        self.lineEditStitchedPostImage.textChanged[str].connect(self.stitched_img_postm_path1)
        self.lineEditCompositeImg.textChanged[str].connect(self.define_composite_img_path1)
        self.lineEditFiji.textChanged[str].connect(self.define_fiji_path1)
        self.lineEditCellProfiler.textChanged[str].connect(self.define_cellprofiler_path1)

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

    def define_python_path(self):
        path = self.file_path_finder()
        global_vars.set_python_path(path)
        self.lineEditPythonPath.setText(path)

    def stitched_img_prem_path(self):
        path = self.file_path_finder()
        global_vars.set_pre_stitched_image_path(path)
        self.lineEditStitchedPreImage.setText(path)

    def stitched_img_postm_path(self):
        path = self.file_path_finder()
        global_vars.set_post_stitched_image_path(path)
        self.lineEditStitchedPostImage.setText(path)

    def define_composite_img_path(self):
        path = self.file_path_finder()
        global_vars.set_composite_path(path)
        self.lineEditStitchedPostImage.setText(path)

    def define_fiji_path(self):
        path = self.file_path_finder()
        global_vars.set_fiji_path(path)
        self.lineEditFiji.setText(path)

    def define_cellprofiler_path(self):
        path = self.file_path_finder()
        global_vars.set_cellprofiler_path(path)
        self.lineEditCellProfiler.setText(path)

    '''Setters for paths'''

    def define_main_folder1(self, path):
        global_vars.set_inp_path(path)

    def define_python_path1(self, path):
        global_vars.set_python_path(path)

    def stitched_img_prem_path1(self, path):
        global_vars.set_pre_stitched_image_path(path)

    def stitched_img_postm_path1(self, path):
        global_vars.set_post_stitched_image_path(path)

    def define_composite_img_path1(self, path):
        global_vars.set_composite_path(path)

    def define_fiji_path1(self, path):
        global_vars.set_fiji_path(path)

    def define_cellprofiler_path1(self, path):
        global_vars.set_cellprofiler_path(path)

    '''Getters'''

    def get_main_folder(self):
        return self.lineEditMainFolder.text()

    def get_python_path(self):
        return self.lineEditPythonPath.text()

    def get_stitched_img_prem_path(self):
        return self.lineEditStitchedPreImage.text()

    def get_stitched_img_postm_path(self):
        return self.lineEditStitchedPostImage.text()

    def get_composite_img_path(self):
        return self.lineEditCompositeImg.text()

    def get_fiji_path(self):
        return self.lineEditFiji.text()

    def get_cellprofiler_path(self):
        return self.lineEditCellProfiler.text()
