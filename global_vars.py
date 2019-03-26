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

        self.MSLogin = ''
        self.MSPass = ''
        self.database = 'ChEBI-2018-01'
        self.fdr = 0.2

        '''Tab Ablation mark finder'''
        self.tab_amf_fftIterations = 20
        self.tab_amf_gblurSigma = 10

        '''Tab grabbing data from metaspace'''
        self.tab_gms_MSLogin = ''
        self.tab_gms_MSPass = ''
        # self.inp_path =  '/home/renat/EMBL/Sharaz_images/rhodamin'
        # self.python_path =  '/home/renat/miniconda3/bin/python'
        # self.cellprofilerPath = ''
        #
        # self.stitchedImgPreMPath = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/pre/bf'
        # self.stitchedImgPostMPath = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/post/bf'
        # self.preMaldiDapi = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/pre/dapi'
        # self.postMaldiDapi = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/post/dapi'
        # self.preMaldiSample = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/pre/rhodamine'
        # self.compositeImgPath = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/Composite.png'
        # self.cpPipeLine = ''
        #
        # self.udpFile = '/home/renat/EMBL/Sharaz_images/rhodamin/191118_RhodaminetTop_p50_s50_DHB_NEG.RAW/191118_Top_Rhodamine_p50_s50_DHB_P.RAW.UDP'
        # self.imzMLName = '191118_Top_Rhodamine_p50_s50_DHB_P.RAW'
        # self.maldiMetadata = '/home/renat/EMBL/Sharaz_images/rhodamin/Post Maldi/Top Square/out.txt'
        #
        # self.MSLogin = ''
        # self.MSPass = ''
        # self.database = 'ChEBI-2018-01'
        # self.fdr = 0.2

        # self.inp_path = '/home/renat/EMBL/Sharaz_images/rhodamin2'
        # self.python_path = '/home/renat/miniconda3/bin/python'
        # self.cellprofilerPath = ''
        #
        # self.stitchedImgPreMPath = '/home/renat/EMBL/Sharaz_images/rhodamin2/Analysis/StitchedMicroscopy/preMALDI_FLR/img_t1_z1_c1'
        # self.stitchedImgPostMPath = '/home/renat/EMBL/Sharaz_images/rhodamin2/Analysis/StitchedMicroscopy/postMALDI_FLR/img_t1_z1_c1'
        # self.preMaldiDapi = '/home/renat/EMBL/Sharaz_images/rhodamin2/Analysis/StitchedMicroscopy/preMALDI_FLR/img_t1_z1_c2'
        # self.postMaldiDapi = '/home/renat/EMBL/Sharaz_images/rhodamin2/Analysis/StitchedMicroscopy/postMALDI_FLR/img_t1_z1_c2'
        # self.preMaldiSample = '/home/renat/EMBL/Sharaz_images/rhodamin2/Analysis/StitchedMicroscopy/preMALDI_FLR/img_t1_z1_c3'
        # self.compositeImgPath = '/home/renat/EMBL/Sharaz_images/rhodamin2/Analysis/StitchedMicroscopy/Composite.png'
        # self.cpPipeLine = ''
        #
        # self.udpFile = '/home/renat/EMBL/Sharaz_images/rhodamin2/06.02.19 RhodamineWellA_topsquare_Pos_S50P50_190207164901.RAW/06.02.19 RhodamineWellA_topsquare_Pos_S50P50_190207164901.UDP'
        # self.imzMLName = '06.02.19 RhodamineWellA_topsquare_Pos_S50P50'
        # self.maldiMetadata = '/home/renat/EMBL/Sharaz_images/rhodamin2/Input/Microscopy/postMALDI/out.txt'
        #
        # self.MSLogin = ''
        # self.MSPass = ''
        # self.database = 'ChEBI-2018-01'
        # self.fdr = 0.5

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

    '''Tab grabbing data from metaspace'''
    def set_MS_login(self, val):
        self.tab_gms_MSLogin = val

    def set_MS_password(self, val):
        self.tab_gms_MSPass = val


global_vars = GlobalVars()