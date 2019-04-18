class GlobalVars:
    def __init__(self):
        self.inpPath = ''
        self.pythonPath = ''
        self.cellprofilerPath = ''

        self.stitchedImgPreMPath = ''
        self.stitchedImgPostMPath = ''
        # self.preMaldiDapi = ''
        # self.preMaldiSample = ''
        # self.compositeImgPath = ''

        self.udpFile = ''
        self.microscopyMetadata = ''

        '''Tab Ablation mark finder'''
        self.tab_amf_matrixType = ''
        self.tab_amf_fftIterations = 20
        self.tab_amf_gblurSigma = 10
        self.tab_amf_maxDist = 15
        self.tab_amf_ifftImage = ''
        self.tab_amf_postMaldiDapi = ''
        # self.tab_amf_showRes = False

        '''Tab grabbing data from metaspace'''
        self.tab_gms_MSLogin = ''
        self.tab_gms_MSPass = ''
        self.tab_gms_msDSName = ''
        self.tab_gms_database = []
        self.tab_gms_fdr = 0.1

        '''Tab running Cellprofiler'''
        self.cpPipeLine = ''

        '''Tab generating csv with mole features'''
        self.tab_genCsv_CDThresh = 0.88
        self.tab_genCsv_csvFilePath = ''


global_vars = GlobalVars()