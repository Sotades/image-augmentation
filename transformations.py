""" A bunch of transformations for defect distortion

"""
import random
import cv2

def random_null(images):
    """ Perform a no operation transform on an image.

    Used as a test for calling transforms

    :param images:
    :return: transformed image
    """

    for img in images:
        yield img


def random_stretch_x(images):
    """ Stretch the defect image randomly by a factor of between 1 and 3 in the x direction

    :param images: the image to be distorted
    :return: the distorted image
    """

    for img in images:
        height, width = img.shape[:2]
        scale_factor = random.uniform(1, 3)
        width *= scale_factor
        width = int(width)
        dim = (width, height)
        transformed_image = cv2.resize(img, dim)
        yield transformed_image


def random_stretch_y(images):
    """ Stretch the defect image randomly by a factor of between 1 and 3 in the y direction

    :param images: the image to be distorted
    :return: the distorted image
    """
    for img in images:
        yield img


def random_shear(images):
    """ Apply a shear transform randomly to the image

    :param images: the image to be distorted
    :return: the distorted image
    """
    for img in images:
        yield img


def random_rotate(images):
    """ Apply a rotation randomly to the image

    :param images: the image to be rotated
    :return: the rotated image
    """
    for img in images:
        yield img


def random_scale(images):
    """ Apply a scaling randomly to the image

    :param images: the image to be scaled
    :return: the scaled image
    """
    for img in images:
        yield img
