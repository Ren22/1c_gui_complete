class GlobalVars:
    def __init__(self):

        self.inpPath =  ''
        self.pythonPath =  ''
        self.cellprofilerPath = ''

        self.stitchedImgPreMPath = ''
        self.stitchedImgPostMPath = ''
        self.preMaldiDapi = ''
        self.postMaldiDapi = ''
        self.preMaldiSample = ''
        self.compositeImgPath = ''
        self.cpPipeLine = ''

        self.udpFile = ''
        self.imzMLName = ''
        self.maldiMetadata = ''

        self.database = 'ChEBI-2018-01'
        self.fdr = 0.1

        '''Tab Ablation mark finder'''
        self.tab_amf_fftIterations = 20
        self.tab_amf_gblurSigma = 10
        self.tab_amf_showRes = False
        # self.tab

        '''Tab grabbing data from metaspace'''
        self.tab_gms_MSLogin = ''
        self.tab_gms_MSPass = ''

    def set_inp_path(self, new_path):
        self.inpPath = new_path

    def set_python_path(self, new_path):
        self.pythonPath = new_path

    def set_cellprofiler_path(self, new_path):
        self.cellprofilerPath = new_path

    def set_pre_stitched_image_bf_path(self, new_path):
        self.stitchedImgPreMPath = new_path

    def set_post_stitched_image_bf_path(self, new_path):
        self.stitchedImgPostMPath = new_path

    def set_pre_stitched_image_dapi_path(self, new_path):
        self.preMaldiDapi = new_path

    def set_post_stitched_image_dapi_path(self, new_path):
        self.postMaldiDapi = new_path

    def set_prem_stitched_image_sample_path(self, new_path):
        self.preMaldiSample = new_path

    def set_composite_path(self, new_path):
        self.compositeImgPath = new_path

    def set_cp_pipe_path(self, new_path):
        self.cpPipeLine = new_path

    def set_udpfile_path(self, new_path):
        self.udpFile = new_path

    def set_imzMLName(self, new_path):
        self.imzMLName = new_path

    def set_maldiMetadata_path(self, new_path):
        self.maldiMetadata = new_path

    '''Tab Ablation mark finder'''
    def set_fftIterations(self, val):
        self.tab_amf_fftIterations = val

    def set_gblurSigma(self, val):
        self.tab_amf_gblurSigma = val

    def set_showRes(self, val):
        self.tab_amf_showRes = val

    '''Tab grabbing data from metaspace'''
    def set_MS_login(self, val):
        self.tab_gms_MSLogin = val

    def set_MS_password(self, val):
        self.tab_gms_MSPass = val

global_vars = GlobalVars()