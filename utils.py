import matplotlib.pyplot as plt
import numpy as np
import tifffile as tiff
import scipy
import os, json
from PIL import Image
from errors import check_paths

CONFIGS = './configs/transforms.json'


def prepare_settings():
    if not os.path.exists('./configs'):
        os.makedirs('./configs')
    if not os.path.exists('./configs/transforms.json'):
        configs = {'transforms': [],
                   'MALDI_img_transformed': False}
        with open('./configs/transforms.json', 'w') as json_file:
            json.dump(configs, json_file)
    else:
        # TODO: add an option of running the existing pipeline configs
        with open('./configs/transforms.json') as f:
            configs = json.load(f)
    return configs


def cropFluo_img(im_p, bf_img_p, output_p, coords_p, name):
    bf_img = Image.open(bf_img_p)
    im = Image.open(im_p)
    coords = np.load(coords_p).item()
    im_crop = im.crop((int(coords['topLeft'][0]), int(coords['topLeft'][1]),
                       int(coords['topLeft'][0]) + bf_img.size[0],
                       int(coords['topLeft'][1]) + bf_img.size[1]))
    im_crop.save(output_p + name + '.tif')





def crop2coords(coords_p, img_p, save_p, window):
    # TODO: MAKE THE FILE SAVED IN A CORRECT FORMAT DEPENDING ON SAVE_P
    X, Y = np.load(coords_p)
    X = [int(x) for x in X]
    Y = [int(y) for y in Y]
    if os.path.splitext(img_p)[1] == 'tif' or os.path.splitext(img_p)[1] == 'tiff'\
            or os.path.splitext(img_p)[1] == '':
        img = tiff.imread(img_p)
        if os.path.splitext(img_p)[1] == '':
            tiff.imsave(save_p + '.tiff', img[np.min(X)-window:np.max(X)+window, np.min(Y)-window:np.max(Y)+window])
    else:
        img = plt.imread(img_p)
        scipy.misc.imsave(save_p, img[np.min(X)-window:np.max(X)+window, np.min(Y)-window:np.max(Y)+window])


def ion2fluoTF(ion_img):
    """Image transformation to apply on ion image for registration.
    Args:
        ion_img (ndarray): the ion image to transform (2D).
    Returns:
        out (array): the transformed ion image.
    """
    with open(CONFIGS) as configs_json:
        configs = json.load(configs_json)
    transforms = configs['transforms']
    was_processed = configs['MALDI_img_transformed']
    if was_processed is True and len(transforms)>0:
        for i in transforms:
            if i == "flipud":
                ion_img = np.flipud(ion_img)
            elif i == "fliplr":
                ion_img = np.fliplr(ion_img)
            elif i == "transp":
                ion_img = np.transpose(ion_img)
            elif i == 3:
                ion_img = np.rot90(ion_img, 3)
            elif i == 2:
                ion_img = np.rot90(ion_img, 2)
            elif i == 1:
                ion_img = np.rot90(ion_img, 1)
    return ion_img


def prepare_images(MF, window=0):
    if not os.path.exists(MF + 'Analysis/CellProfilerAnalysis/'):
        os.makedirs(MF + 'Analysis/CellProfilerAnalysis/')

    if not os.path.exists(MF + 'Analysis/CellProfilerAnalysis/'):
        os.makedirs(MF + 'Analysis/CellProfilerAnalysis/')
    if not os.path.exists(MF + 'Analysis/cropped_preM_channels'):
        os.makedirs(MF + 'Analysis/cropped_preM_channels')
    for file in os.listdir(MF + '/Analysis/StitchedMicroscopy/preMALDI_FLR'):
        if file.startswith('img_'):
            crop2coords(
                MF + 'Analysis/Fiducials/transformedMarks.npy',
                MF + '/Analysis/StitchedMicroscopy/preMALDI_FLR/' + file,
                MF + 'Analysis/cropped_preM_channels/' +
                os.path.splitext(file)[0] + '_cropped',
                window=window)


def prepared_cropped_img_amfinder(MF, bf_img_p, image_type):
    for file in os.listdir(MF + '/Analysis/StitchedMicroscopy/{}MALDI_FLR'.format(image_type)):
        if file.startswith('img_'):
            try:
                cropFluo_img(MF + '/Analysis/StitchedMicroscopy/{}MALDI_FLR/'.format(image_type) + file,
                                   bf_img_p,
                                   output_p=MF + '/Analysis/cropped_{}M_channels/'.format(image_type, image_type),
                                   coords_p=MF + 'Analysis/gridFit/AM_cropped_coords.npy',
                                   name=os.path.splitext(file)[0] + '_cropped')
            except (FileNotFoundError, IOError):
                raise Exception(
                    'Fluorescent image cannot be cropped, please make sure that it is in the directory and has a correct name')