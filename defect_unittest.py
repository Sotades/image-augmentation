import unittest
import cv2
import numpy as np
from defect import Defect
from null_transform import null_transform
from transformations import random_stretch_x
import tubo


class TestDefect(unittest.TestCase):


    def setUp(self):
        self.image = cv2.imread('images/unit_test/edge_defect1.jpg')

    def test_no_distortion(self):
        # List of transformation operators
        transform_operations = [null_transform, null_transform]

        # Create a defect
        defect = Defect(self.image, *transform_operations)

        if not np.array_equal(defect.original_defect_image, defect.distorted_defect_image):
                raise AssertionError("Elements don't match!")

    def test_some_distortion(self):
        # List of transformation operators
        transform_operations = [null_transform, random_stretch_x]

        # Create a defect
        defect = Defect(self.image, *transform_operations)
        defect.distort_defect()

        for distorted_defect_image in defect.distorted_defect_images:
            if np.array_equal(defect.original_defect_image, distorted_defect_image):
                raise AssertionError("Elements don't match!")

    def test_height_width_not_null_after_distortion(self):
        pass
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
