from PyQt5.QtWidgets import *
from global_vars.global_vars import global_vars


class GenCsvTab():
    def __init__(self, ext_obj):
        ext_obj.tab_csvGen_corrValThr.valueChanged.connect(self.set_CDThr)
        ext_obj.tab_csvGen_lineEditCells.textChanged[str].connect(lambda: self.set_cells_csv(ext_obj))
        ext_obj.tab_csvGen_btnCells.clicked.connect(lambda: self.define_cells_csv(ext_obj))

    '''callbacks'''
    @staticmethod
    def set_cells_csv(ext_obj):
        global_vars.tab_genCsv_csvFilePath = ext_obj.tab_csvGen_lineEditCells.text()

    def define_cells_csv(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.tab_genCsv_csvFilePath = path
        ext_obj.tab_csvGen_lineEditCells.setText(path)

    def set_CDThr(self, val):
        global_vars.tab_genCsv_CDThresh = val

    '''Common'''
    @staticmethod
    def file_path_finder(ext_obj):
        input_dir = ''
        try:
            input_dir, _ = QFileDialog.getOpenFileName(ext_obj, 'Select a file:')
        except Exception as e:
            print('File cannot be opened')
            print(e, e.args)
        return input_dir