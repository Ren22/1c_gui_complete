import matplotlib.pyplot as plt
import numpy as np
import tifffile as tiff
import scipy
import os, json
from PIL import Image

CONFIGS = './configs/configs.json'


def prepare_settings():
    if not os.path.exists('./configs'):
        os.makedirs('./configs')
    if not os.path.exists('./configs/configs.json'):
        configs = {'transforms': [],
                   'MALDI_img_transformed': False}
        with open('./configs/configs.json', 'w') as json_file:
            json.dump(configs, json_file)
    else:
        # TODO: add an option of running the existing pipeline configs
        with open('./configs/configs.json') as f:
            configs = json.load(f)
    return configs


def cropFluo_img(im_p, bf_img_p, output_p, coords_p):
    # im = plt.imread(im_p)
    bf_img = Image.open(bf_img_p)
    im = Image.open(im_p)
    coords = np.load(coords_p).item()
    im_crop = im.crop((int(coords['topLeft'][0]), int(coords['topLeft'][1]),
                       int(coords['topLeft'][0]) + bf_img.size[0],
                       int(coords['topLeft'][1]) + bf_img.size[1]))
    # im_crop = im[int(coords['topLeft'][1]): int(coords['bottomRight'][1]),
    #           int(coords['topLeft'][0]): int(coords['bottomRight'][0])]
    # tiff.imsave(file=output_p + 'AM_cropped_2.tif', data=im_crop)
    im_crop.save(output_p + 'AM_cropped_2.tif')


def scale(arr):
    """Scale array between 0 and 1"""
    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))


def contrast(arr, min, max=1.0):
    """Clip array between min and max values"""
    return np.clip(arr, np.percentile(arr, min*100), np.percentile(arr, max*100))


def crop2coords(coords_p, img_p, save_p, window):
    # TODO: MAKE THE FILE SAVED IN A CORRECT FORMAT DEPENDING ON SAVE_P
    X, Y = np.load(coords_p)
    X = [int(x) for x in X]
    Y = [int(y) for y in Y]
    if img_p.split('/')[-1].split('.') == 'tif' or img_p.split('/')[-1].split('.') == 'tiff':
        img = tiff.imread(img_p)
        output_path = save_p + '.tiff'
        tiff.imsave(save_p, img[np.min(X)-window:np.max(X)+window, np.min(Y)-window:np.max(Y)+window])
    # if len(img_p.split('/')[-1].split('.')) == 1:
    #     img = tiff.imread(img_p)
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
    #return ion_img.T  # --> TF1 HepaJune dataset batches FASTER


def prepare_images(MF, preM_dapi, preM_fluo, composite, window=0):
    if not os.path.exists(MF + 'Analysis/CellProfilerAnalysis/'):
        os.makedirs(MF + 'Analysis/CellProfilerAnalysis/')
    preM_dapi_name = os.path.basename(preM_dapi)
    preM_fluo_name = os.path.basename(preM_fluo)
    composite_name = os.path.basename(composite)

    if preM_dapi_name.endswith('.png'):
        preM_dapi_name = preM_dapi_name[:-4]
    if preM_fluo_name.endswith('.png'):
        preM_fluo_name = preM_fluo_name[:-4]
    if composite_name.endswith('.png'):
        composite_name = composite_name[:-4]

    crop2coords(
        MF + 'Analysis/Fiducials/transformedMarks.npy',
        preM_dapi,
        MF + 'Analysis/CellProfilerAnalysis/{}_cropped.tiff'.format(os.path.basename(preM_dapi_name)),
        window=window)

    crop2coords(
        MF + 'Analysis/Fiducials/transformedMarks.npy',
        preM_fluo,
        MF + 'Analysis/CellProfilerAnalysis/{}_cropped.tiff'.format(os.path.basename(preM_fluo_name)),
        window=window)

    crop2coords(
        MF + 'Analysis/Fiducials/transformedMarks.npy',
        composite,
        MF + 'Analysis/CellProfilerAnalysis/{}_cropped.tiff'.format(os.path.basename(composite_name)),
        window=window)
