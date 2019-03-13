import os, codecs, re, gc
import tifffile as tiff
import numpy as np
from subprocess import call

fiji_path = '/home/renat/EMBL/software/Fiji.app/ImageJ-linux64'
MF = '/home/renat/EMBL/vero/test2/'
metadata_path = '/home/renat/EMBL/vero/test2/Input/Microscopy/preMALDI/Well2.txt'


def getPixSize(metadata_path):
    """Reads the pixel size in um from the Nikon Ti E microscope (NIS elements software).

    Returns:
        pix_size (float): pixel size in um.

    """
    pix_size = 0.73
    txt_file = codecs.open(metadata_path, 'r', 'utf-16')
    for row in txt_file:
        if row.startswith('Calibration'):
            pix_size = float(row.strip().split()[2].replace(',', '.'))
    return pix_size


def TileConfFormat(path, dir_fliplr, tif_files, pix_size):
    """Extract the microscope motor stage coordinates at each frame from the metadata text file from the Nikon
    Ti-E microscope (NIS elements software) and reformat into readable format for the Priebisch software algorithm
    from FIJI.

    Args:
        path (str): path of the directory containing the microscope metadata file (named 'out.txt' by default).
        dir_fliplr (str): path of the directory containing the transformed tiled frames to stitch.
        tif_files (array): names of each tiled frames to stitch.

    """
    if os.path.basename(metadata_path) in os.listdir(path):
        txt_file = codecs.open(path + os.path.basename(metadata_path), 'r', 'utf-16')
        data = []
        out_file = open(dir_fliplr + 'TileConfiguration.txt', 'w')
        out_file.write('# Define the number of dimensions we are working on\ndim = 2\n\n# Define the image coordinates\n')
        i = 0
        n_zfill = 1
        if np.shape(tif_files)[0] >= 10:
            n_zfill = 2
        if np.shape(tif_files)[0] >= 100:
            n_zfill = 3
        if np.shape(tif_files)[0] >= 1000:
            n_zfill = 4

        base = re.findall('^(.*)\d{' + str(n_zfill) + '}.tif$', tif_files[0])[0]
        checkpoint = 0
        for row in txt_file:
            if row.startswith('Point Name'):
                checkpoint = 1
            if row.startswith('#') and checkpoint == 1:

                if i <= np.shape(tif_files)[0]-1:
                    # print(row.strip().split('\t'))
                    data.append(row.strip().split('\t'))
                    data[i][0] = str(i).zfill(n_zfill)
                    data[i][1] = float(data[i][1].replace(',', '.')) / pix_size
                    data[i][2] = float(data[i][2].replace(',', '.')) / pix_size
                    out_file.write(base + '{}.tif; ; ({}, {})\n'.format(data[i][0],data[i][1],data[i][2]))
                    # re.findall('^(.*)(\d{3})$', 'seq000_XY120')
                    # print i
                    i = i+1
            elif row.startswith('Spectral Loop'):
                break
        out_file.close()


def callFIJImergeChannels(base_path,
                          colors,
                          filenames,
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

    script_file_p = base_path + 'mergeRedGray_script.txt'
    base = os.path.splitext(script_file_p)[0]

    if os.path.exists(base_path + 'mergeRedGray_script.ijm'):
        os.remove(base_path + 'mergeRedGray_script.ijm')

    out_file2 = open(script_file_p , 'w')
    out_file2.write(string1 + 'run("Merge Channels...", "{}")\
    \nsaveAs("PNG", "{}");\
    \nrun("Quit");'\
                    .format(string2,
                            base_path + save_filename))
    out_file2.close()

    if os.path.exists(base + ".ijm"):
        os.remove(base + ".ijm")
    os.rename(script_file_p, base + ".ijm")
    call([fiji_path, '-macro', base + ".ijm"])#, stdout = PIPE)


def callFIJIstitch(dir_fliplr):
    """Calls FIJI stitching algorithm on the transformed tiled frames using the reformatted metadata text file.
    The function creates a FIJI macro which is then ran by FIJI application.

    Args:
        dir_fliplr (str): path of the directory containing the tiled frames to stitch and the metadata text file.

    """
    script_file_p = dir_fliplr + 'stitch_script.txt'
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
    call([fiji_path, '-macro', base + ".ijm"])#, stdout = PIPE)
    # os.remove('C:\\Users\Luca\AppData\Local\Temp\org.scijava.jython.shaded.jline_2_5_3.dll')


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


def PixFliplr(tf, file_path, MFAspm):
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
    ind = 1
    for item in os.listdir(file_path):
        if item.endswith('.tif'):
            a = tiff.imread(file_path + item)
            # a = (a/float(np.max(a)))*16385.0
            if np.shape(a.shape)[0] == 2:
                n_chan=1
                b = np.zeros((np.max(a.shape), np.max(a.shape)),
                             dtype=np.uint16)  # lazy hack --> restricts to squared images
                # b.shape = 1, 1, 1, a.shape[0], a.shape[1], 1
                b[:, :] = tf(a[:, :])
            else:
                n_chan = a.shape[0]
                b = np.zeros((n_chan, a.shape[1], a.shape[2]), dtype=np.uint16) # lazy hack --> restricts to squared images
                # b.shape =  n_chan, a.shape[1], a.shape[2], 1, 1 # dimensions in XYCZT order
                for i in range(n_chan):
                    b[i, :, :] = tf(a[i, :, :])

            tiff.imsave(MFAspm + item,  b)
            # plt.imsave(arr=b, fname=MFAspm + item)
            # fi.write_multipage(b, MFAspm + item)
            # io.imsave(MFAspm + item, b)
            tif_files.append(item)
            # print('Processed Image # {}'.format(ind))
            ind  = ind+1
    return tif_files


def stitchMicroscopy(MF,
                     tf,
                     merge_filenames=[],
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

        tif_files = PixFliplr(
            tf,
            MF + 'Input/Microscopy/preMALDI/',
            MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/')

        pix_size = getPixSize(metadata_path=metadata_path)

        TileConfFormat(path= MF + 'Input/Microscopy/preMALDI/',
                                                              dir_fliplr=MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/',
                                                              tif_files= tif_files, pix_size=pix_size)
        gc.collect()
        callFIJIstitch(MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/')
        print('Pre-MALDI Stitching finished')

    if postMALDI:

        if not os.path.exists(MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/'):
            os.makedirs(MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/')

        tif_files = PixFliplr(
            tf,
            MF + 'Input/Microscopy/postMALDI/',
            MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/')

        pix_size = getPixSize(metadata_path=metadata_path)

        TileConfFormat(path=MF + 'Input/Microscopy/postMALDI/',
                                                              dir_fliplr=MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/',
                                                              tif_files=tif_files, pix_size=pix_size)
        gc.collect()
        callFIJIstitch(MF + 'Analysis/StitchedMicroscopy/postMALDI_FLR/')
        print('Post-MALDI Stitching finished')

    if merge_colors != []:
        callFIJImergeChannels(
            base_path=MF + 'Analysis/StitchedMicroscopy/preMALDI_FLR/',
            colors=merge_colors,
            filenames=merge_filenames,
            save_filename='Composite.png')


def tf(img):
    # return img
    return np.fliplr(np.flipud(img))


if __name__ == '__main__':
    stitchMicroscopy(MF, tf=tf, )
