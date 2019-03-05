import os
import pipelineMethods, utils
from subprocess import run, call
from spaceM.unneeded_files.Pipeline import spatioMolecularMatrix, mapIntensitiesOnCells
from spaceM.scAnalysis.Segmentation import cellDistribution_MALDI as cellDistrib
from global_vars import global_vars

SETTINGS = utils.prepare_settings()

class Analysis():
    def __init__(self):
        super(Analysis, self).__init__()
        ''' GUI paths'''
        self.MF = global_vars.inp_path + '/'
        self.PYTHON_PATH = global_vars.python_path
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
        self.AM_CURATOR = './pipeline_helpers/MaldiHelper.py'
        self.SPOT_FINDER = self.MFA + 'SpotFinder/'
        self.GRIDFIT = self.MFA + 'gridFit/'
        self.ILI = './pipeline_helpers/ili.py'


class FindAMinPM(Analysis):
    def __init__(self):
        super(FindAMinPM, self).__init__()

    def step1(self):
        print('cropPMimage started')
        if not os.path.exists(self.GRIDFIT):
            os.makedirs(self.GRIDFIT)
        run(["{}".format(self.PYTHON_PATH), "{}".format(self.AM_CURATOR), "{}".format(self.STITCHED_POST),
             "{}AM_cropped.tif".format(self.GRIDFIT)])
        print('cropPMimage finished')

    def step2(self):
        if not os.path.exists(self.GRIDFIT):
            os.makedirs(self.GRIDFIT)
        print('Ablation mark finding and filtering started')
        pipelineMethods.ablation_mark_filter(self.MF, self.STITCHED_POST, self.GRIDFIT,
                                             self.POSTM_DAPI, self.UDP_FILE,
                                             self.MALDI_METADATA, "{}AM_cropped.tif".format(self.GRIDFIT), window=0)
        print('Ablation mark finding and filtering finished')


class FindFilterFiducials(Analysis):
    def __init__(self):
        super(FindFilterFiducials, self).__init__()

    def step1(self):
        print("Searching for fiducials started")
        pipelineMethods.fiducials_finder(self.MF, self.STITCHED_PRE, self.STITCHED_POST)
        print("Searching for fiducials finished")

    def step2(self):
        print('Fiducials filtering on PRE maldi image started')
        run(["{}".format(self.PYTHON_PATH), "{}".format(self.AM_CURATOR),
             "{}".format(self.MFA + 'Fiducials/preXYpenmarks.npy'),
             "{}".format(self.MFA + 'Fiducials/preXYpenmarks.npy')])
        print('Fiducials filtering on PRE maldi image finished')
        print('Fiducials filtering on POST maldi image started')
        run(["{}".format(self.PYTHON_PATH), "{}".format(self.AM_CURATOR),
             "{}".format(self.MFA + 'Fiducials/postXYpenmarks.npy'),
             "{}".format(self.MFA + 'Fiducials/postXYpenmarks.npy')])
        print('Fiducials filtering on POST maldi image finished')


class RegisterPrePostMaldi(Analysis):
    def step1(self):
        # For this step access to internet and Metaspace is needed
        # The metaspace package is used to pull ion images
        # Check if the package is not updated -> update it
        print("Registration of Pre and Post maldi fidicuals, alignment, and metaspace based annotation started")
        pipelineMethods.registration(self.MF,
                                     tf_obj=utils.ion2fluoTF,
                                     ili_fdr=self.FDR,
                                     ds_name=self.IMZML_FILENAME,
                                     db_name=self.DATABASE,
                                     email=self.MS_LOGIN,
                                     password=self.MS_PASS)
        print("Registration of Pre and Post maldi fidicuals, alignment, and metaspace based annotation finished")


class CellSegment(Analysis):
    def __init__(self):
        super(CellSegment, self).__init__()

    def step0(self):
        print("Images are cropped and are being prepared for cellprofiler")
        # TODO : these window 100 vals are very cryptic and not easy to understand
        utils.prepare_images(self.MF, self.PREM_DAPI, self.PREM_FLUO, self.COMPOSITE_PNG, window=100)
        print("Images preparation is done")

    def step1(self):
        print("Cell profiler for cell segmentation started")
        pipelineMethods.cell_segmentation(self.MF, self.CP_PIPELINE)
        print("Cell segmentation finished")

    def step2(self):
        print("Generation of cell distribution image started")
        cellDistrib(self.MF, window=100)
        print("Generation of cell distribution image finished")

    def step3(self):
        print("Generation of cell outlines image started")
        pipelineMethods.cell_outlines_gen(self.MF, cp_window=100)
        print("Generation of cell outlines image finished")

    def step4(self):
        print("Calling ablation marks analyzer(ili)")
        csv = self.MFA + 'ili/sm_annotation_detections.csv'
        img = self.MFA + 'CellProfilerAnalysis/Composite_cropped.tiff'
        celldist = self.MFA + 'CellProfilerAnalysis/cellDistribution_MALDI.npy'
        configs = './configs/configs.json'
        execut_string = '{} {} -csv {} -img {} -celldist {} -configs {}'.format(self.PYTHON_PATH,
                                                                                self.ILI,
                                                                                csv,
                                                                                img,
                                                                                celldist,
                                                                                configs)
        call(execut_string, shell=True)
        print("Ablation marks analyzer finished")


class GenerateCSV(Analysis):
    def step1(self):
        spatioMolecularMatrix(self.MF,
                              tf_obj=utils.ion2fluoTF,
                              udp_path=self.UDP_FILE,
                              ms_login=self.MS_LOGIN,
                              ms_password=self.MS_PASS,
                              ds_name=self.IMZML_FILENAME,
                              fdr_level=self.FDR)

    def step2(self):
        mapIntensitiesOnCells(self.MF, tf_obj=utils.ion2fluoTF)
