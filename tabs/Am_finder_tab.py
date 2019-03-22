from PyQt5.QtWidgets import *
from global_vars import global_vars


class AmFinderTab():
    def __init__(self, ext_obj):
        ext_obj.tab1_sbFftIters.valueChanged.connect(self.tab1_sbFftItersCallback)
        ext_obj.tab1_sbFftGblurSigma.valueChanged.connect(self.tab1_sbFftGblurSigmaCallback)

    '''Callbacks'''
    @staticmethod
    def tab1_sbFftItersCallback(val):
        global_vars.tab1_fftIterations = val

    @staticmethod
    def tab1_sbFftGblurSigmaCallback(val):
        global_vars.tab1_gblurSigma = val