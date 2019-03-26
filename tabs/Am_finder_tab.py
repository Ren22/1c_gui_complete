from PyQt5.QtWidgets import *
from global_vars import global_vars
from PyQt5.QtCore import Qt


class AmFinderTab():
    def __init__(self, ext_obj):
        ext_obj.tab_amf_sbFftIters.valueChanged.connect(self.tab_amf_sbFftIters)
        ext_obj.tab_amf_sbFftGblurSigma.valueChanged.connect(self.tab_amf_sbFftGblurSigma)
        ext_obj.tab_amf_checkBoxDispRes.stateChanged.connect(self.tab_amf_cbDispRes)

    '''Callbacks'''
    @staticmethod
    def tab_amf_sbFftIters(val):
        global_vars.tab_amf_fftIterations = val

    @staticmethod
    def tab_amf_sbFftGblurSigma(val):
        global_vars.tab_amf_gblurSigma = val

    @staticmethod
    def tab_amf_cbDispRes(state):
        if state == Qt.Checked:
            global_vars.tab_amf_showRes = True
        else:
            global_vars.tab_amf_showRes = False

