import functools
import os
import uuid

from matplotlib import gridspec
import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf

def crop_center(image):
    """Returns a cropped square image."""
    shape = image.shape
    new_shape = min(shape[1], shape[2])
    offset_y = max(shape[1] - shape[2], 0) // 2
    offset_x = max(shape[2] - shape[1], 0) // 2
    image = tf.image.crop_to_bounding_box(
        image, offset_y, offset_x, new_shape, new_shape)
    return image


@functools.lru_cache(maxsize=None)
def load_image(image_url_or_file, from_url, image_size=(256, 256), preserve_aspect_ratio=True):
    """
    Given an image source, which is either a url to an image or a file-like object,
    load and prepare an image as an input for the style transfer model.
    """

    # if the image source is a url, get the file then set the image source as the path to the file.
    if from_url:
        # Cache image file locally.
        image_source = tf.keras.utils.get_file(os.path.basename(image_url_or_file)[-128:], image_url_or_file)
    else:
        # otherwise, the image source is a filelike object and can be passed to plt imread directly
        image_source = image_url_or_file

    # convert image to float32 numpy array, add batch dimension, and normalize to range [0, 1]
    img = plt.imread(image_source).astype(np.float32)[np.newaxis, ...]
    if img.max() > 1.0:
        img = img / 255.
    if len(img.shape) == 3:
        img = tf.stack([img, img, img], axis=-1)
    img = crop_center(img)
    img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
    return img

def save_image(img, flask_app):
    """
    Save an img tensor (the output image from the style_transfer module) 
    of shape=(1, 256, 256, 3), dtype=float32 to the given filename location

    returns the filename of the saved file.
    """
    # generate a random id for the filename
    result_filename = str(uuid.uuid4()) + '.jpg'

    # get the first image in the batch
    img = img[0]
    # switch to numpy so imsave can understand the data type of the array of image data
    img = img.numpy()

    # save the image to the filesystem so it can be referenced by the client application
    plt.imsave(os.path.join(flask_app.config["RESULTS_FOLDER"], result_filename), img)

    return result_filename