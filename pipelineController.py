import os
import pipelineMethods, utils
from subprocess import run, call
from global_vars import global_vars
from pipeline_helpers import abl_mark_handler, ili_analog

SETTINGS = utils.prepare_settings()


class Analysis():
    def __init__(self):
        self.get_paths()

    def get_paths(self):
        ''' GUI general settings'''
        self.MF = global_vars.inpPath + '/'
        self.PYTHON_PATH = global_vars.pythonPath
        self.CP = global_vars.cellprofilerPath

        self.STITCHED_PRE = global_vars.stitchedImgPreMPath
        self.STITCHED_POST = global_vars.stitchedImgPostMPath
        self.PREM_DAPI = global_vars.preMaldiDapi
        self.POSTM_DAPI = global_vars.postMaldiDapi
        self.PREM_FLUO = global_vars.preMaldiSample
        self.COMPOSITE_PNG = global_vars.compositeImgPath
        self.CP_PIPELINE = global_vars.cpPipeLine

        self.UDP_FILE = global_vars.udpFile
        self.IMZML_FILENAME = global_vars.imzMLName
        self.MALDI_METADATA = global_vars.maldiMetadata

        self.MS_LOGIN = global_vars.MSLogin
        self.MS_PASS = global_vars.MSPass
        self.DATABASE = global_vars.database
        self.FDR = global_vars.fdr

        self.MFA = self.MF + 'Analysis/'
        self.AM_CURATOR = abl_mark_handler.__file__
        self.SPOT_FINDER = self.MFA + 'SpotFinder/'
        self.GRIDFIT = self.MFA + 'gridFit/'
        self.ILI = ili_analog.__file__

        ''' GUI AM tab1'''
        self.TAB1_ITERATIONS = global_vars.tab_amf_fftIterations
        self.TAB1_GBLUR_SIGMA = global_vars.tab_amf_gblurSigma


class FindAMinPM():
    def __init__(self):
        self.vars = Analysis()

    def step1(self):
        self.vars.get_paths()
        print('cropPMimage started')
        if not os.path.exists(self.vars.GRIDFIT):
            os.makedirs(self.vars.GRIDFIT)
        run(["{}".format(self.vars.PYTHON_PATH), "{}".format(self.vars.AM_CURATOR), "{}".format(self.vars.STITCHED_POST),
             "{}AM_cropped.tif".format(self.vars.GRIDFIT)])
        print('cropPMimage finished')

    def step2(self):
        self.vars.get_paths()
        if not os.path.exists(self.vars.GRIDFIT):
            os.makedirs(self.vars.GRIDFIT)
        print('Ablation mark finding and filtering started')
        pipelineMethods.ablation_mark_filter(
            MF=self.vars.MF,
            postMaldiImgPath=self.vars.STITCHED_POST,
            postMFluoOutputPath=self.vars.GRIDFIT,
            postMFluoPath=self.vars.POSTM_DAPI,
            UDPpath=self.vars.UDP_FILE,
            maldiMetadataPath=self.vars.MALDI_METADATA,
            bf_img_p="{}AM_cropped.tif".format(self.vars.GRIDFIT),
            iterations=self.vars.TAB1_ITERATIONS,
            gblur_sigma=self.vars.TAB1_GBLUR_SIGMA,
            window=0)
        print('Ablation mark finding and filtering finished')


class FindFilterFiducials():
    def __init__(self):
        self.vars = Analysis()

    def step1(self):
        self.vars.get_paths()
        print("Searching for fiducials started")
        pipelineMethods.fiducials_finder(self.vars.MF, self.vars.STITCHED_PRE, self.vars.STITCHED_POST)
        print("Searching for fiducials finished")

    def step2(self):
        self.vars.get_paths()
        print('Fiducials filtering on PRE maldi image started')
        run(["{}".format(self.vars.PYTHON_PATH), "{}".format(self.vars.AM_CURATOR),
             "{}".format(self.vars.MFA + 'Fiducials/preXYpenmarks.npy'),
             "{}".format(self.vars.MFA + 'Fiducials/preXYpenmarks.npy')])
        print('Fiducials filtering on PRE maldi image finished')
        print('Fiducials filtering on POST maldi image started')
        run(["{}".format(self.vars.PYTHON_PATH), "{}".format(self.vars.AM_CURATOR),
             "{}".format(self.vars.MFA + 'Fiducials/postXYpenmarks.npy'),
             "{}".format(self.vars.MFA + 'Fiducials/postXYpenmarks.npy')])
        print('Fiducials filtering on POST maldi image finished')


class RegisterPrePostMaldi():
    def __init__(self):
        self.vars = Analysis()

    def step1(self):
        self.vars.get_paths()
        # For this step access to internet and Metaspace is needed
        # The metaspace package is used to pull ion images
        # Check if the package is not updated -> update it
        print("Registration of Pre and Post maldi fidicuals, alignment, and metaspace based annotation started")
        pipelineMethods.registration(self.vars.MF)
        print("Registration of Pre and Post maldi fidicuals, alignment, and metaspace based annotation finished")


class GrabMsData():
    def __init__(self):
        self.vars = Analysis()

    def step1(self):
        self.vars.get_paths()
        pipelineMethods.grab_ms_data(
            self.vars.MF,
            ili_fdr=self.vars.FDR,
            ds_name=self.vars.IMZML_FILENAME,
            db_name=self.vars.DATABASE,
            email=self.vars.MS_LOGIN,
            password=self.vars.MS_PASS)


class CellSegment():
    def __init__(self):
        self.vars = Analysis()

    def step0(self):
        self.vars.get_paths()
        print("Images are cropped and are being prepared for cellprofiler")
        # TODO : these window 100 vals are very cryptic and not easy to understand
        utils.prepare_images(self.vars.MF, self.vars.PREM_DAPI, self.vars.PREM_FLUO, self.vars.COMPOSITE_PNG, window=100)
        print("Images preparation is done")

    def step1(self):
        self.vars.get_paths()
        print("Cell profiler for cell segmentation started")
        pipelineMethods.cell_segmentation(self.vars.MF, self.vars.CP_PIPELINE)
        print("Cell profiler segmentation finished")

    def step2(self):
        self.vars.get_paths()
        print("Generation of cell distribution image started")
        pipelineMethods.cell_distrib(self.vars.MF, window=100)
        print("Generation of cell distribution image finished")

    def step3(self):
        self.vars.get_paths()
        print("Generation of cell outlines image started")
        pipelineMethods.cell_outlines_gen(self.vars.MF, cp_window=100)
        print("Generation of cell outlines image finished")

    def step4(self):
        self.vars.get_paths()
        print("Calling ablation marks analyzer(ili)")
        csv = self.vars.MFA + 'ili/sm_annotation_detections.csv'
        img = self.vars.MFA + 'CellProfilerAnalysis/Composite_cropped.tiff'
        celldist = self.vars.MFA + 'CellProfilerAnalysis/cellDistribution_MALDI.npy'
        configs = './configs/transforms.json'
        execut_string = '{} {} -csv {} -img {} -celldist {} -configs {}'.format(self.vars.PYTHON_PATH,
                                                                                self.vars.ILI,
                                                                                csv,
                                                                                img,
                                                                                celldist,
                                                                                configs)
        call(execut_string, shell=True)
        print("Ablation marks analyzer finished")

class GenerateCSV():
    def __init__(self):
        self.vars = Analysis()

    def step1(self):
        self.vars.get_paths()
        pipelineMethods.spatio_molecular_matrix(self.vars.MF,
                              tf_obj=utils.ion2fluoTF,
                              udp_path=self.vars.UDP_FILE,
                              ms_login=self.vars.MS_LOGIN,
                              ms_password=self.vars.MS_PASS,
                              ds_name=self.vars.IMZML_FILENAME,
                              fdr_level=self.vars.FDR)

    def step2(self):
        self.vars.get_paths()
        pipelineMethods.map_intensities_on_cells(self.vars.MF, tf_obj=utils.ion2fluoTF)
