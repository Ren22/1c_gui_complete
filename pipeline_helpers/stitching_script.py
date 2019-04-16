import os, codecs, re, gc
import tifffile as tiff
import numpy as np
from subprocess import call
from shutil import copyfile
from pathlib import Path, PureWindowsPath
from sys import platform

def def_platform_path(path):
    if platform == "win32":
        path = str(PureWindowsPath(path))
    else:
        path = Path(path)
    return path

def getMetadataPath(folderToSearch):
    if len(os.listdir(folderToSearch)) > 0:
        for row in os.listdir(folderToSearch):
            if row.endswith('.txt'):
                with codecs.open(folderToSearch + row, 'r', 'utf-16') as txt_file:
                    data = txt_file.readlines()
                    if len(re.findall('Image Fields', data[0])) > 0:
                        return Path(folderToSearch + row)
    else:
        return 0
    raise Exception('Metadata file was not found at {}'.format(folderToSearch))


def getPixSize(MF, metadata_path):
    """Reads the pixel size in um from the Nikon Ti E microscope (NIS elements software).

    Returns:
        pix_size (float): pixel size in um.

    """
    for row in os.listdir(Path(MF + 'Input/Microscopy/preMALDI/')):
        if row.endswith('.txt'):
            os.path.basename(row)
            with codecs.open(Path(MF + 'Input/Microscopy/preMALDI/' + row), 'r', 'utf-16') as txt_file:
                data = txt_file.readlines()
                if len(re.findall('Image Fields', data[0])) > 0:
                    metadata_path = Path(MF + 'Input/Microscopy/preMALDI/' + row)
    pix_size = 0.73
    txt_file = codecs.open(metadata_path, 'r', 'utf-16')
    for row in txt_file:
        if row.startswith('Calibration'):
            pix_size = float(row.strip().split()[2].replace(',', '.'))
    return pix_size


def TileConfFormat(path, dir_fliplr, tif_files, pix_size, metadata_path, start_index):
    """Extract the microscope motor stage coordinates at each frame from the metadata text file from the Nikon
    Ti-E microscope (NIS elements software) and reformat into readable format for the Priebisch software algorithm
    from FIJI.

    Args:
        path (str): path of the directory containing the microscope metadata file (named 'out.txt' by default).
        dir_fliplr (str): path of the directory containing the transformed tiled frames to stitch.
        tif_files (array): names of each tiled frames to stitch.

    """
    txt_file = codecs.open(metadata_path, 'r', 'utf-16')
    data = []
    out_file = open(dir_fliplr + 'TileConfiguration.txt', 'w')
    out_file.write('# Define the number of dimensions we are working on\ndim = 2\n\n# Define the image coordinates\n')
    i = start_index
    n_zfill = 1
    if np.shape(tif_files)[0] >= 10:
        n_zfill = 2
    if np.shape(tif_files)[0] >= 100:
        n_zfill = 3
    if np.shape(tif_files)[0] >= 1000:
        n_zfill = 4

    base = re.findall('^(.*)\d{' + str(n_zfill) + '}.tif$', tif_files[0])[0]
    checkpoint = 0
    tif_files_count = len(tif_files)
    for row in txt_file:
        if row.startswith('Point Name'):
            checkpoint = 1
        if row.startswith('#') and checkpoint == 1:
            if i <= tif_files_count:
                data.append(row.strip().split('\t'))
                data[-1][0] = str(i).zfill(n_zfill)
                data[-1][1] = float(data[-1][1].replace(',', '.')) / pix_size
                data[-1][2] = float(data[-1][2].replace(',', '.')) / pix_size
                out_file.write(base + '{}.tif; ; ({}, {})\n'.format(data[-1][0],data[-1][1],data[-1][2]))
                i = i+1
        elif row.startswith('Spectral Loop'):
            break
    out_file.close()


def callFIJImergeChannels(base_path,
                          colors,
                          filenames,
                          fiji_path,
                          save_filename = 'Composite.png'):

    """Creates a FIJI macro and call FIJI executable to merge different channels stored in independent files into an RGB
    image (.png).

    Args:
        base_path (str): path of the directory containing the images to merge.
        colors (list): list of string of color names: 'red', 'green', 'blue', 'gray', 'cyan', 'magenta', 'yellow'.
        filename (str): list of string of image files names to merge. Their sequence in the list should match their
            respective color in the 'colors' argument.
        save_filename (str): name of the merged image containing all chanels. Saved as an RGB image

    """

    color_codex = {'red': 'c1',
                   'green': 'c2',
                   'blue': 'c3',
                   'gray': 'c4',
                   'cyan': 'c5',
                   'magenta': 'c6',
                   'yellow': 'c7'}

    string1 = ''

    ## FIXME: Fragile part , len(filenames) can be 0
    for i in range(len(filenames)):
        string1 = string1 + 'open("{}")\n'.format(
            base_path + filenames[i]
        )

    string2 = ''
    for i in range(len(colors)):
        string2 = string2 + '{}={} '.format(
            color_codex[colors[i]],
            filenames[i])
    string2 = string2 + 'create'

    script_file_p = Path(base_path + 'mergeRedGray_script.txt')
    base = os.path.splitext(script_file_p)[0]

    if os.path.exists(Path(base_path + 'mergeRedGray_script.ijm')):
        os.remove(Path(base_path + 'mergeRedGray_script.ijm'))

    out_file2 = open(script_file_p , 'w')
    out_file2.write(string1 + 'run("Merge Channels...", "{}")\
    \nsaveAs("PNG", "{}");\
    \nrun("Quit");'\
                    .format(string2,
                            base_path + save_filename))
    out_file2.close()

    if os.path.exists(Path(base + ".ijm")):
        os.remove(Path(base + ".ijm"))
    os.rename(script_file_p, base + ".ijm")
    call([fiji_path, '-macro', base + ".ijm"])#, stdout = PIPE)


def callFIJIstitch(dir_fliplr, fiji_path):
    """Calls FIJI stitching algorithm on the transformed tiled frames using the reformatted metadata text file.
    The function creates a FIJI macro which is then ran by FIJI application.

    Args:
        dir_fliplr (str): path of the directory containing the tiled frames to stitch and the metadata text file.

    """
    script_file_p = dir_fliplr + 'stitch_script.txt'
    dir_fliplr = PureWindowsPath(dir_fliplr).as_posix()
    out_file2 = open(script_file_p , 'w')
    out_file2.write('run("Grid/Collection stitching", \
    "type=[Positions from file] order=[Defined by TileConfiguration] directory={} \
    layout_file=TileConfiguration.txt fusion_method=[Linear Blending] regression_threshold=0.30 \
    max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 \
    compute_overlap computation_parameters=[Save computation time (but use more RAM)] \
    image_output=[Write to disk] output_directory={}"); \
                    \nrun("Quit");'
                    .format(dir_fliplr,
                            dir_fliplr))
    out_file2.close()
    base = os.path.splitext(script_file_p)[0]
    if os.path.exists(base + ".ijm"):
        os.remove(base + ".ijm")
    os.rename(script_file_p, base + ".ijm")
    try:
        call([fiji_path, '-macro', base + ".ijm"])
    except PermissionError:
        raise Exception('Please provide ImageJ executable, most probably directory path was provided')


def callFIJIstitch_noCompute(dir_in, dir_out, fiji_path):
    copyfile(src=Path(dir_out + 'TileConfiguration'
                                '.registered.txt'), dst=Path(dir_in + 'TileConfiguration.registered.txt'))
    copyfile(src=Path(dir_out + 'img_t1_z1_c1'), dst=Path(dir_out + 'img_t1_z1_c0'))

    script_file_p = dir_in + 'stitch_script_2.txt'
    dir_in = PureWindowsPath(dir_in).as_posix()
    dir_out = PureWindowsPath(dir_out).as_posix()
    out_file2 = open(script_file_p, 'w')
    out_file2.write('run("Grid/Collection stitching", "type=[Positions from file] order=[Defined by TileConfiguration] ' \
                    'directory={} layout_file=TileConfiguration.registered.txt ' \
                    'fusion_method=[Linear Blending] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 ' \
                    'computation_parameters=[Save computation time (but use more RAM)] image_output=[Write to disk] ' \
                    'output_directory={}");'
                    '\nrun("Quit");'
                    .format(dir_in,
                            dir_out))
    out_file2.close()
    base = os.path.splitext(script_file_p)[0]
    if os.path.exists(base + ".ijm"):
        os.remove(base + ".ijm")
    os.rename(script_file_p, base + ".ijm")
    call([fiji_path, '-macro', base + ".ijm"])


def readTileConfReg(dir_fliplr):
    """Extract registered tile image coordinates from the textfile generated by Priebisch stitching algorithm
    in FIJI.

    Args:
        dir_fliplr(str): path of the directory containing the registered coordinates.

    Returns:
        dataXscaled (array): registred tile images X coordinates.
        dataYscaled (array): registred tile images Y coordinates.

    """
    txt_file = codecs.open(dir_fliplr + 'TileConfiguration.registered.txt', 'r')
    dataX = []
    dataY = []
    for row in txt_file:
        # print(row)
        if row.endswith(')\n'):
            # print(row)
            dataY = np.append(dataY, float(row.split()[2].replace('(', '').replace(',', '')))
            dataX = np.append(dataX, float(row.split()[3].replace(')', '')))
    dataXscaled = dataX - np.min(dataX)
    dataYscaled = dataY - np.min(dataY)

    return dataXscaled, dataYscaled


def PixFliplr(tf, file_path, MFAspm, transform):
    """Transform images before stitching. This transformation depends on the microscope, the software and the camera used.

    Args:
        tf (fun): transformation function (np.fliplr/np.flupud/.T) toi apply to the tile images prior to stitching.
        file_path (str): path of directory containing the tiled images to transform.
        MFAspm (str): path of directory where the transformed images will be saved.

    Returns:
        tif_files (array): array containing the names of the transformed images.

    """
    # if not os.path.exists(dir_fliplr):
    #     os.makedirs(dir_fliplr)
    tif_files = []
    for item in os.listdir(file_path):
        if item.endswith('.tif'):
            a = tiff.imread(file_path + item)
            if np.shape(a.shape)[0] == 2:
                b0 = np.zeros((np.max(a.shape), np.max(a.shape)),
                             dtype=np.uint16)
                b0[:, :] = tf(a[:, :], transform)
            else:
                if not os.path.exists(Path(MFAspm + 'other_channels/')):
                    os.mkdir(Path(MFAspm + 'other_channels/'))
                b0 = tf(a[0, :, :], transform)
                n_chan = a.shape[0] - 1
                b = np.zeros((n_chan, a.shape[1], a.shape[2]), dtype=np.uint16)
                for i in range(n_chan):
                    b[i, :, :] = tf(a[i + 1, :, :])
                tiff.imsave(MFAspm + 'other_channels/' + item, b)
            tiff.imsave(MFAspm + item, b0)
            tif_files.append(item)
    return tif_files


def stitchMicroscopy(MF,
                     tf,
                     fiji_path,
                     merge_filenames=[],
                     merge_colors=[],
                     preMALDI=True,
                     postMALDI=False,
                     transform=None,
                     start_index=0):

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

    if not os.path.exists(Path(MF + 'Analysis/')):
        os.makedirs(Path(MF + 'Analysis/'))
        os.mkdir(Path(MF + 'Analysis/StitchedMicroscopy/'))

    if preMALDI:

        if not os.path.exists(Path(MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/')):
            os.makedirs(Path(MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/'))

        tif_files = PixFliplr(
            tf,
            MF + 'Input/Microscopy/preMALDI/',
            MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/',
            transform)

        if len(tif_files) > 0:

            metadata_path = getMetadataPath(MF + 'Input/Microscopy/preMALDI/')
            pix_size = getPixSize(MF, metadata_path)
            TileConfFormat(path=MF + 'Input/Microscopy/preMALDI/',
                           dir_fliplr=MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/',
                           tif_files= tif_files,
                           pix_size=pix_size,
                           metadata_path=metadata_path,
                           start_index=start_index)
            gc.collect()
            callFIJIstitch(MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/', fiji_path)
            callFIJIstitch_noCompute(
                MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/' + 'other_channels/',
                MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/',
                fiji_path)

        print('Pre-MALDI Stitching finished')

    if postMALDI:

        if not os.path.exists(Path(MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/')):
            os.makedirs(Path(MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/'))

        tif_files = PixFliplr(
            tf,
            MF + 'Input/Microscopy/postMALDI/',
            MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/',
            transform)

        if len(tif_files) > 0:

            metadata_path = getMetadataPath(MF + 'Input/Microscopy/postMALDI/')
            pix_size = getPixSize(MF, metadata_path)
            TileConfFormat(path=MF + 'Input/Microscopy/postMALDI/',
                           dir_fliplr=MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/',
                           tif_files=tif_files,
                           pix_size=pix_size,
                           metadata_path=metadata_path,
                           start_index=start_index)
            gc.collect()
            callFIJIstitch(MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/', fiji_path)
            callFIJIstitch_noCompute(
                MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/' + 'other_channels/',
                MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/',
                fiji_path)

        print('Post-MALDI Stitching finished')
    # TODO: Remove mergin as it's not part of automated pipeline anymore
    # if merge_colors != []:
    #     callFIJImergeChannels(
    #         base_path=Path(MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/'),
    #         colors=merge_colors,
    #         filenames=merge_filenames,
    #         save_filename='Composite.png')


def tf(img, transform=None):
    transforms = {
        'left_right': np.fliplr(img),
        'upside_down': np.flipud(img),
        'left_right_upside_down': np.fliplr(np.flipud(img))
    }
    if transform:
        return transforms[transform]
    else:
        return img
    # return np.flipud(img)
    # return np.fliplr(np.flipud(img))


if __name__ == '__main__':
    fiji_path = '/home/renat/EMBL/software/Fiji.app/ImageJ-linux64'
    MF = '/home/renat/EMBL/Sharaz_images/1_1mM_Tet_UNW_DMEM/'
    # Possible transformations to the tiled images
    # transform = 'left_right'
    # transform = 'upside_down'
    # transform = 'left_right_upside_down'
    # transform = '' # will produce no transformation
    transform = ''
    st_index = 1 # Starting index of tiles
    stitchMicroscopy(MF, tf, fiji_path, transform, start_index=st_index)
