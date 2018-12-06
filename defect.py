import tubo
import cv2
import numpy
from transformations import random_stretch_x
from transformations import random_stretch_y
from transformations import random_shear
from transformations import random_scale
from transformations import random_rotate
from typing import List


class Defect:

    # Initializer / Instance Attributes
    def __init__(self, original_defect_image: dict(type=numpy.ndarray, help='original image of defect'), *transform_operations: dict(type=list, help='list of transform operator function names to use in pipeline')):

        self.original_defect_image = original_defect_image  # original image of defect
        self.original_defect_images = []
        self.distorted_defect_image = []
        self.distorted_defect_images = []

        self.undistorted_height: int       # height of surrounding undistorted image box
        self.undistorted_width: int        # width of surrounding undistorted image box
        self.distorted_height: int         # height of surrounding distorted image box
        self.distorted_width: int          # width of surrounding distorted image box
        self.transform_operations = transform_operations

        self.undistorted_height = self.original_defect_image.shape[0]
        self.undistorted_width = self.original_defect_image.shape[1]

    def distort_defect(self):
        self.original_defect_images.append(self.original_defect_image)

        # apply the pipeline to the defect to distort it
        distorted_defect_images = tubo.pipeline(
            self.original_defect_images,
            *self.transform_operations)

        # recalculate 'box' of defect
        for distorted_defect_image in distorted_defect_images:
            self.distorted_defect_image = distorted_defect_image
            self.distorted_height = distorted_defect_image.shape[1]
            self.distorted_width = distorted_defect_image.shape[0]
            cv2.imwrite('images/unit_test/edge_defect1_distorted.jpg', distorted_defect_image)



