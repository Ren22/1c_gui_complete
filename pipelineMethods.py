import os, json, gc
import scipy.misc
import spaceM
import utils


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
    predata = spaceM.WriteILIinput.preCSVdatagen(
        MF + 'Analysis/gridFit/xye_clean2.npy',
        radius=10,
        nbin=nbin,
        PlainFirst=True)
    spaceM.WriteILIinput.writeCSV(
        path=MF + 'Analysis/gridFit/marks_check/ablation_marks_checkDETECTIONS.csv',
        data=predata)

    predata = spaceM.WriteILIinput.preCSVdatagen(
        MF + 'Analysis/gridFit/xye_grid.npy',
        radius=10,
        nbin=nbin,
        PlainFirst=True)
    spaceM.WriteILIinput.writeCSV(
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


def registration(MF, tf_obj, do_transform=True, do_ili=True, ili_fdr=0.2,
    ds_name = None, db_name = None, email = None, password = None):
    if not os.path.exists(MF + 'Analysis/Fiducials/optimized_params.npy'):
        spaceM.Registration.ImageRegistration.fiducialsAlignment(MF + 'Analysis/')

    if do_transform:
        spaceM.Registration.ImageRegistration.TransformMarks(MF + 'Analysis/')

    if do_ili:
        if not os.path.exists(MF + 'Analysis/ili/'):
            os.makedirs(MF + 'Analysis/ili/')

    spaceM.WriteILIinput.annotationSM2CSV(
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


def cell_outlines_gen(MF, cp_window):
    spaceM.scAnalysis.Segmentation.cellOutlines(MF + 'Analysis/CellProfilerAnalysis/Composite_cropped.tiff',
                             cp_window,
                             MF + 'Analysis/CellProfilerAnalysis/Labelled_cells.tiff',
                             MF + 'Analysis/CellProfilerAnalysis/Contour_cells_adjusted.png')


def stitch_microscopy(MF,
                     merge_filenames,
                     tf,
                     merge_colors=[],
                     preMALDI=True,
                     postMALDI=True):

    """Function to stitch tile microscopy images into a single one. The function first applies a transformation (tf) on
        each tile images prior to stitching. It also merges defined fields of stitched images together into an RGB .png
        file.
    Args:
        MF (str): path to the Main Folder.
        merge_colors (list): list of string of color names: 'red', 'green', 'blue', 'gray', 'cyan', 'magenta', 'yellow'.
        merge_filenames (list): list of string of image files names to merge. Their sequence in the list should match their
            respective color in the 'colors' argument. After stitching they should start with 'img_t1_z1_c ... '.
        tf (fun): image transformation to apply to the tile images prior to stitching.
        preMALDI (bool): whether or not stithcing preMALDI dataset.
        postMALDI (bool): whether or not stithcing postMALDI dataset.

    Data are stored in MF + /Analysis/StitchedMicroscopy/
    """

    if not os.path.exists(MF + 'Analysis/'):
        os.makedirs(MF + 'Analysis/')
        os.mkdir(MF + 'Analysis/StitchedMicroscopy/')

    if preMALDI:

        if not os.path.exists(MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/'):
            os.makedirs(MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/')

        tif_files = spaceM.ImageFileManipulation.manipulations.PixFliplr(
            tf,
            MF + 'Input/Microscopy/preMALDI/',
            MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/')

        spaceM.ImageFileManipulation.FIJIcalls.TileConfFormat(path= MF + 'Input/Microscopy/preMALDI/',
                                                              dir_fliplr=MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/',
                                                              tif_files= tif_files)
        gc.collect()
        spaceM.ImageFileManipulation.FIJIcalls.callFIJIstitch(MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/')
        print('Pre-MALDI Stitching finished')

    if postMALDI:

        if not os.path.exists(MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/'):
            os.makedirs(MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/')

        tif_files = spaceM.ImageFileManipulation.manipulations.PixFliplr(
            tf,
            MF + 'Input/Microscopy/postMALDI/',
            MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/')

        spaceM.ImageFileManipulation.FIJIcalls.TileConfFormat(path=MF + 'Input/Microscopy/postMALDI/',
                                                              dir_fliplr=MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/',
                                                              tif_files=tif_files)
        gc.collect()
        spaceM.ImageFileManipulation.FIJIcalls.callFIJIstitch(MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/')
        print('Post-MALDI Stitching finished')

    if merge_colors != []:
        spaceM.ImageFileManipulation.FIJIcalls.callFIJImergeChannels(
            base_path=MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/',
            colors=merge_colors,
            filenames=merge_filenames,
            save_filename='Composite.png')
