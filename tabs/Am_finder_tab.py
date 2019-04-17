from PyQt5.QtWidgets import *
from global_vars.global_vars import global_vars

class AmFinderTab():
    def __init__(self, ext_obj):
        ext_obj = ext_obj
        global_vars.tab_amf_matrixType = ext_obj.tab_amf_cbMatrix.currentText()
        ext_obj.tab_amf_gbFluoCh.setHidden(True)
        ext_obj.tab_amf_cbMatrix.currentTextChanged.connect(lambda: self.provide_marix_type(ext_obj))

        ext_obj.tab_amf_btnFluoCh.clicked.connect(lambda: self.provide_fluo_channel(ext_obj))
        ext_obj.tab_amf_FluoCh.textChanged[str].connect(lambda: self.set_fluo_channel(ext_obj))

        ext_obj.tab_amf_sbFftIters.valueChanged.connect(self.tab_amf_sbFftIters)
        ext_obj.tab_amf_sbFftGblurSigma.valueChanged.connect(self.tab_amf_sbFftGblurSigma)

        ext_obj.tab_amf_ifftImgPath.textChanged[str].connect(lambda: self.set_ifft_image(ext_obj))
        ext_obj.tab_amf_btniFFTimg.clicked.connect(lambda: self.provide_ifft_image(ext_obj))
        ext_obj.tab_amf_autoFftRb.clicked.connect(lambda: self.auto_fft(ext_obj))
        ext_obj.tab_amf_manFftRb.clicked.connect(lambda: self.man_fft(ext_obj))

        ext_obj.tab_amf_markSize.valueChanged.connect(self.tab_amf_set_am_size)

    '''Type of matrix section'''
    def provide_fluo_channel(self, ext_obj):
        path = self.file_path_finder(ext_obj)
        global_vars.tab_amf_postMaldiDapi = path
        ext_obj.tab_amf_FluoCh.setText(path)

    def set_fluo_channel(self, ext_obj):
        global_vars.tab_amf_postMaldiDapi = ext_obj.tab_amf_FluoCh.text()

    def get_fluo_channel(self):
        return ext_obj.tab_amf_FluoCh.text()

    def provide_marix_type(self, ext_obj):
        selMatrixType = ext_obj.tab_amf_cbMatrix.currentText()
        global_vars.tab_amf_matrixType = selMatrixType
        if selMatrixType == 'DHB':
            ext_obj.tab_amf_gbFluoCh.setHidden(False)
            if ext_obj.tab_amf_manFftRb.isChecked():
                ext_obj.tab_amf_gbFluoCh.setHidden(True)
        elif selMatrixType == 'DAN':
            ext_obj.tab_amf_gbFluoCh.setHidden(True)

    '''FFt section'''
    def provide_ifft_image(self, ext_obj):
        ext_obj.tab_amf_manFftRb.setChecked(True)
        if ext_obj.tab_amf_autoFftRb.isChecked():
            ext_obj.tab_amf_autoFftRb.isChecked(False)
        if ext_obj.tab_amf_cbMatrix.currentText() == 'DHB':
            ext_obj.tab_amf_gbFluoCh.setHidden(True)
        path = self.file_path_finder(ext_obj)
        global_vars.pythonPath = path
        ext_obj.tab_amf_ifftImgPath.setText(path)


    def set_ifft_image(self, ext_obj):
        ext_obj.tab_amf_manFftRb.setChecked(True)
        if ext_obj.tab_amf_autoFftRb.isChecked():
            ext_obj.tab_amf_autoFftRb.isChecked(False)
        if ext_obj.tab_amf_cbMatrix.currentText() == 'DHB':
            ext_obj.tab_amf_gbFluoCh.setHidden(True)
        global_vars.tab_amf_ifftImage = ext_obj.tab_amf_ifftImgPath.text()


    def get_ifft_image(self, ext_obj):
        return ext_obj.tab_amf_ifftImgPath.text()

    @staticmethod
    def auto_fft(ext_obj):
        if ext_obj.tab_amf_cbMatrix.currentText() == 'DHB':
            ext_obj.tab_amf_gbFluoCh.setHidden(False)

    @staticmethod
    def man_fft(ext_obj):
        if ext_obj.tab_amf_cbMatrix.currentText() == 'DHB':
            ext_obj.tab_amf_gbFluoCh.setHidden(True)

    @staticmethod
    def tab_amf_sbFftIters(val):
        global_vars.tab_amf_fftIterations = val

    @staticmethod
    def tab_amf_sbFftGblurSigma(val):
        global_vars.tab_amf_gblurSigma = val

    '''Region growing options'''
    @staticmethod
    def tab_amf_set_am_size(val):
        global_vars.tab_amf_maxDist = val

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
