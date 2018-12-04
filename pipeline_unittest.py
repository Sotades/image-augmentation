import unittest
import cv2
import tubo
import numpy as np
from transformations import random_null
from transformations import random_stretch_x



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.image = cv2.imread('D:/Users/Tony/PycharmProjects/Altia/image-augmentation/images/unit_test/edge_defect1.jpg')
        # Make list of base defects
        self.images = []
        self.images.append(self.image)

    def test_no_transform(self):

        self.output = tubo.pipeline(
            self.images,
            random_null,
        )

        input_image_width = self.image.shape[1]
        input_image_height = self.image.shape[0]
        for output_image in self.output:
            output_image_width = output_image.shape[1]
            output_image_height = output_image.shape[0]
            self.assertGreaterEqual(output_image_width, input_image_width)
            self.assertEqual(output_image_height, input_image_height)

    def test_pass_args_to_create_pipeline(self, ):
        # This is how you pass a list as function parameters
        list_of_transforms = [random_null, random_null]

        # Pass in the list of parameters using the splat operator:
        self.output = tubo.pipeline(
            self.images,
            *list_of_transforms,
        )

        for output_image in self.output:
            if not np.array_equal(self.image, output_image):
                raise AssertionError("Elements don't match!")


if __name__ == '__main__':
    unittest.main()
