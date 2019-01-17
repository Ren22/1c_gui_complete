import os, logging
from subprocess import run, call, Popen
from spaceM.Pipeline import ablationMarksFilter as AMFilter
from spaceM.Pipeline import fiducialsFinder as FFinder
from spaceM.Pipeline import registration
from spaceM.Pipeline import spatioMolecularMatrix
from spaceM.Pipeline import cellSegmentation
from spaceM.scAnalysis.Segmentation import cellDistribution_MALDI as cellDistrib
from spaceM.CellProfilerProjectFiles.CP_upstream import default_processing
from global_vars import GlobalVars, global_vars

MERGE_COLOURS = []
MERGE_FILENAMES = []


def prepare_paths():
    all_paths = {
        'MF': global_vars.inp_path,
        'PYTHON_PATH': global_vars.python_path,
        'STITCHED_PREM': global_vars.stitchedImgPreMPath,
        'STITCHED_POST': global_vars.stitchedImgPostMPath,
        'MFA': global_vars.inp_path + 'Analysis/',
        'AM_CURATOR': './MaldiHelper.py',
        'CROPPED_PM_OUT_PATH': global_vars.inp_path + 'Analysis/' + 'SpotFinder/',
        'SPOT_FINDER': global_vars.inp_path + 'Analysis/' + 'SpotFinder/',
        'ILI': './ili.py'
    }
    return all_paths


def ion2fluoTF(ion_img):
    """Image transformation to apply on ion image for registration.
    Args:
        ion_img (ndarray): the ion image to transform (2D).
    Returns:
        out (array): the transformed ion image.
    """
    return ion_img.T  # --> TF1 HepaJune dataset batches FASTER


class Analysis():
    def __init__(self):
        super(Analysis, self).__init__()
        self.MF = global_vars.inp_path + '/'
        self.MFA = self.MF + 'Analysis/'
        self.PYTHON_PATH = global_vars.python_path
        self.STITCHED_PRE = global_vars.stitchedImgPreMPath
        self.STITCHED_POST = global_vars.stitchedImgPostMPath
        self.STITCHED_PRE_GF = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/pre/bf'
        self.STITCHED_POST_GF = '/home/renat/EMBL/Sharaz_images/rhodamin/stitched/post/bf'
        self.COMPOSITE_PNG = global_vars.compositeImgPath
        self.AM_CURATOR = './MaldiHelper.py'
        self.CROPPED_PM_OUT_PATH = self.MFA + 'gridFit/'
        self.SPOT_FINDER = self.MFA + 'SpotFinder/'
        self.GRIDFIT = self.MFA + 'gridFit/'
        self.ILI = '/home/renat/EMBL/spaceM_Luca/linux/1c_gui_complete/ili.py'
        self.CP = global_vars.cellprofilerPath


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
        AMFilter(self.MF, self.STITCHED_POST, self.GRIDFIT)
        print('Ablation mark finding and filtering finished')


class FindFilterFiducials(Analysis):
    def __init__(self):
        super(FindFilterFiducials, self).__init__()

    def step1(self):
        print("Searching for fiducials started")
        FFinder(self.MF, self.STITCHED_PRE_GF, self.STITCHED_POST_GF)
        print("Searching for fiducials finished")

    def step2(self):
        print('Fiducials filtering on PRE maldi image started')
        run(["{}".format(self.PYTHON_PATH), "{}".format(self.AM_CURATOR), "{}".format(self.MFA + 'Fiducials/preXYpenmarks.npy'),
             "{}".format(self.MFA + 'Fiducials/preXYpenmarks.npy')])
        print('Fiducials filtering on PRE maldi image finished')
        print('Fiducials filtering on POST maldi image started')
        run(["{}".format(self.PYTHON_PATH), "{}".format(self.AM_CURATOR), "{}".format(self.MFA + 'Fiducials/postXYpenmarks.npy'),
             "{}".format(self.MFA + 'Fiducials/postXYpenmarks.npy')])
        print('Fiducials filtering on POST maldi image finished')


class RegisterPrePostMaldi(Analysis):
    ILI_FDR = 0.5

    def step1(self):
        ## For this step access to internet and Metaspace is needed
        ## The metaspace package is used to pull ion images
        ## Check if the package is not updated -> update it
        print("Registration of Pre and Post maldi fidicuals, alignment, and metaspace based annotation started")
        registration(self.MF, tf_obj=ion2fluoTF, compositeImg=self.COMPOSITE_PNG, ili_fdr=self.ILI_FDR)
        print("Registration of Pre and Post maldi fidicuals, alignment, and metaspace based annotation finished")


class CellSegment(Analysis):
    def step0(self):
        print("Started image preparation for Cell Profiler")
        default_processing(self.MF)
        print("Finished image preparation for Cell Profiler")

    def step1(self):
        print("Cell segmentation started")
        cellSegmentation(self.MF)
        print("Cell segmentation finished")

    def step2(self):
        print("Generation of cell distribution image started")
        cellDistrib(self.MF)
        print("Generation of cell distribution image finished")

    def step3(self):
        print("Calling ablation marks analyzer(ili)")
        csv = self.MFA + 'ili/sm_annotation_detections.csv'
        img = self.MFA + 'ili/FLUO_crop_bin1x1.png'
        celldist = '' #self.MFA + 'CellProfilerAnalysis/cellDistribution_MALDI.npy'
        execut_string = '{} {} -csv {} -img {} -celldist {}'.format(self.PYTHON_PATH, self.ILI, csv, img, celldist)

        # call(execut_string)
        run(["{}".format(self.PYTHON_PATH), "{}".format(self.ILI)])
        print("Ablation marks analyzer finished")


class GenerateCSV(Analysis):
    def step1(self):
        spatioMolecularMatrix(self.MF, tf_obj=ion2fluoTF)

