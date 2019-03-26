from PyQt5.QtWidgets import *
from global_vars import global_vars


class AmFinderTab():
    def __init__(self, ext_obj):
        ext_obj.tab_amf_sbFftIters.valueChanged.connect(self.tab_amf_sbFftIters)
        ext_obj.tab_amf_sbFftGblurSigma.valueChanged.connect(self.tab_amf_sbFftGblurSigma)

    '''Callbacks'''
    @staticmethod
    def tab_amf_sbFftIters(val):
        global_vars.tab_amf_fftIterations = val

    @staticmethod
    def tab_amf_sbFftGblurSigma(val):
        global_vars.tab_amf_gblurSigma = val