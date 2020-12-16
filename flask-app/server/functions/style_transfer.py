import tensorflow as tf
import tensorflow_hub as hub

from .image_helpers import crop_center, load_image

style_transfer_hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'

print("loading style transfer module...")
style_transfer_module = hub.load(style_transfer_hub_handle)
print("successfully loaded style transfer module.")

def apply_style_transfer(content_img, style_img):
    """
    Perform style transfer on a given content image with the given style image.
    Both images are expected to be given as file objects from the files property of
    the http request
    """

    # preprocess the given image files to array data so it can be processed by the style transfer module
    content_img_bin = load_image(content_img, from_url=False)
    style_img_bin = load_image(style_img, from_url=False)

    # perform style transfer
    outputs = style_transfer_module(tf.constant(content_img_bin), tf.constant(style_img_bin))
    stylized_image = outputs[0]

    return stylized_image