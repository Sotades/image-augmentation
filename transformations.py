import random
import cv2

def random_null(images):
    for img in images:
        height, width = img.shape[:2]
        yield img


def random_stretch_x(images):
    for img in images:
        shape = img.shape
        height, width = img.shape[:2]
        scale_factor = random.uniform(1, 3)
        width *= scale_factor
        width = int(width)
        dim = (width, height)
        transformed_image = cv2.resize(img, dim)
        yield transformed_image


def random_stretch_y(images):
    for img in images:
        yield img


def random_shear(images):
    for img in images:
        yield img


def random_rotate(images):
    for img in images:
        yield img


def random_scale(images):
    for img in images:
        yield img
