import os, gc
import utils
import spaceM

def ablation_mark_filter(MF, postMaldiImgPath, postMFluoOutputPath, postMFluoPath,
                         UDPpath, maldiMetadataPath, bf_img_p, marks_check=True, window=0):
    """Filters ablation marks. First by re-running the ablation mark detection on the cropped stitched images where the
    ablation marks are. Then by fitting a theoretical grid on the detections and taking only the closest detection to
    each grid node. This filters out double detections and re-orders the remaining ones into a uniform index which matches
    later on the index of the ion image. The detections after filtering can be visualized in 'ili (https://ili.embl.de/).

    Args:
        MF (str): path to the Main Folder.
        marks_check (bool): whether or not show the results.

    Data are stored in MF + /Analysis/gridFit/
    Visualization are stored in MF + /Analysis/gridFit/marks_check/
    """
    if postMFluoPath:
        try:
            utils.cropFluo_img(postMFluoPath,
                               bf_img_p,
                               output_p=postMFluoOutputPath,
                               coords_p=MF + 'Analysis/gridFit/AM_cropped_coords.npy')
        except (FileNotFoundError, IOError):
            raise Exception(
                'DAPI image cannot be cropped, please make sure that it is in the directory and has a correct name')

    spaceM.Registration.AblationMarkFinder.GridFit(MF, postMaldiImgPath, UDPpath=UDPpath, maldiMetadataPath=maldiMetadataPath)

    if marks_check:
        if not os.path.exists(MF + 'Analysis/gridFit/marks_check/'):
            os.makedirs(MF + 'Analysis/gridFit/marks_check/')

        mark_check_p = MF + 'Analysis/gridFit/marks_check/marks_check_window{}.tiff'.format(window)

        utils.crop2coords(
            MF + 'Analysis/gridFit/xye_clean2.npy',
            postMaldiImgPath,
            mark_check_p,
            window=window)
        # nbin = spaceM.ImageFileManipulation.FIJIcalls.imbin4ili(
        #     MF + 'Analysis/gridFit/marks_check/PHASE_crop_bin1x1.png',
        #     maxsize=50e6)

    nbin = 1
    predata = spaceM.Registration.WriteILIinput.preCSVdatagen(
        MF + 'Analysis/gridFit/xye_clean2.npy',
        radius=10,
        nbin=nbin,
        PlainFirst=True)
    spaceM.Registration.WriteILIinput.writeCSV(
        path=MF + 'Analysis/gridFit/marks_check/ablation_marks_checkDETECTIONS.csv',
        data=predata)

    predata = spaceM.Registration.WriteILIinput.preCSVdatagen(
        MF + 'Analysis/gridFit/xye_grid.npy',
        radius=10,
        nbin=nbin,
        PlainFirst=True)
    spaceM.Registration.WriteILIinput.writeCSV(
        path=MF + 'Analysis/gridFit/marks_check/ablation_marks_checkTHEORETICAL.csv',
        data=predata)

    if not os.path.exists(MF + 'Analysis/gridFit/marksMask.npy'):
        # Provide maxDist=17 for the rho 2 exp
        # spaceM.Registration.AblationMarkFinder.regionGrowingAblationMarks(MF, window=window, maxDist=17)
        spaceM.Registration.AblationMarkFinder.regionGrowingAblationMarks(MF, window=window)
        spaceM.Registration.AblationMarkFinder.AM_filter(MF, window=window)


def fiducials_finder(MF, preMaldiImg, postMaldiImg):
    """Find the fiducials coordinates on the stitched images.
    Args:
        MF (str): path to the Main Folder.

    Data are stored in MF + /Analysis/Fiducials/
    """

    if not os.path.exists(MF + 'Analysis/Fiducials/'):
        os.makedirs(MF + 'Analysis/Fiducials/')

    spaceM.Registration.ImageRegistration.penMarksFeatures(MF, stitchedImg=preMaldiImg, prefix='pre')
    spaceM.Registration.ImageRegistration.penMarksFeatures(MF, stitchedImg=postMaldiImg, prefix='post')


def registration(MF, do_transform=True, do_ili=True):
    if not os.path.exists(MF + 'Analysis/Fiducials/optimized_params.npy'):
        spaceM.Registration.ImageRegistration.fiducialsAlignment(MF + 'Analysis/')

    if do_transform:
        spaceM.Registration.ImageRegistration.TransformMarks(MF + 'Analysis/')

    if do_ili:
        if not os.path.exists(MF + 'Analysis/ili/'):
            os.makedirs(MF + 'Analysis/ili/')


def grab_ms_data(MF, ili_fdr=0.2, ds_name=None, db_name=None, email=None, password=None):
    spaceM.Registration.WriteILIinput.annotationSM2CSV(
        MFA=MF + 'Analysis/',
        fdr=ili_fdr,
        nbin=1,
        radius=20,
        ds_name=ds_name,
        db_name=db_name,
        email=email,
        password=password)


def cell_segmentation(MF, pipeline_file):

    if not os.path.exists(MF + 'Analysis/CellProfilerAnalysis/'):
        os.makedirs(MF + 'Analysis/CellProfilerAnalysis/')

    headless = True if len(pipeline_file) > 0 else False
    spaceM.scAnalysis.Segmentation.callCP(MF + 'Analysis/', pipeline_file, headless = headless)


def cell_distrib(MF, window):
    spaceM.scAnalysis.Segmentation.cellDistribution_MALDI(MF, window)


def cell_outlines_gen(MF, cp_window):
    spaceM.scAnalysis.Segmentation.cellOutlines(MF + 'Analysis/CellProfilerAnalysis/Composite_cropped.tiff',
                                                       cp_window,
                                                       MF + 'Analysis/CellProfilerAnalysis/Labelled_cells.tiff',
                                                       MF + 'Analysis/CellProfilerAnalysis/Contour_cells_adjusted.png')


def spatio_molecular_matrix(MF,
                          tf_obj,
                          CDs=[0.75],
                          fetch_ann='online',
                          filter='correlation',
                          tol_fact=-0.2,
                          udp_path=None,
                          ms_login=None,
                          ms_password=None,
                          ds_name=None,
                          fdr_level=0.5):

    if not os.path.exists(MF + 'Analysis/scAnalysis/'):
        os.makedirs(MF + 'Analysis/scAnalysis/')

    spaceM.scAnalysis.scAnalysis_refactored.defMOLfeatures(
        MF,
        tf_obj=tf_obj,
        CDs=CDs,
        norm_method='weighted_mean_sampling_area_MarkCell_overlap_ratio_sampling_area',
        fetch_ann=fetch_ann, tol_fact=tol_fact, filter=filter,
        fluo_path=MF + 'Analysis/CellProfilerAnalysis/rhodamine_cropped.tiff',
        fluo_nucl_path=MF + 'Analysis/CellProfilerAnalysis/dapi_cropped.tiff',
        ili_csv_file_path=MF + 'Analysis/ili/sm_annotation_detections.csv',
        udp_path=udp_path,
        ms_login=ms_login,
        ms_password=ms_password,
        ds_name=ds_name,
        fdr_level=fdr_level)

    spaceM.scAnalysis.scAnalysis_refactored.mergeMORPHnMOL(
        MF,
        CDs=CDs,
        fetch_ann=fetch_ann,
        tol_fact=tol_fact,
        filter=filter)


def map_intensities_on_cells(MF, tf_obj):
    spaceM.scAnalysis.scAnalysis_refactored.mapAnn2microCells(
        MF,
        ds_index=None,
        csv_p=MF + 'Analysis/scAnalysis/MORPHnMOL.csv',
        labelled_cells_path=MF + 'Analysis/CellProfilerAnalysis/Labelled_cells.tiff',
        tf_obj=tf_obj,
        cp_window=0)