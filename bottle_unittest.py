import unittest
from bottle import Bottle


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bottle = Bottle('images/unit_test/bottle.jpg')

    def test_initializer(self):
        self.assertIsInstance(self.bottle, Bottle)
        self.assertTrue(self.bottle.features)

    def test_calculate_box_dimensions(self):

        # GIVEN a Bottle class is created
        # WHEN the image width is 355 pixels
        # AND the image height is 1280
        self.bottle = Bottle('images/unit_test/bottle.jpg')

        # AND the desired boxes across is 4
        # AND the desired boxes down is 10
        boxes = self.bottle.calculate_box_dimensions(desired_boxes_across=4, desired_boxes_down=10)
        # THEN I expect the box width to be 88 pixels
        # AND I expect the box height to be 128 pixels
        self.assertEqual(boxes['box_width'], 88)
        self.assertEqual(boxes['box_height'], 128)

    def test_draw_and_display_rectangles(self):
        self.bottle = Bottle('images/unit_test/bottle.jpg')
        boxes = self.bottle.calculate_box_dimensions(desired_boxes_across=4, desired_boxes_down=10)
        self.bottle.draw_and_display_rectangles(boxes_across=4, boxes_down=10)
        return









if __name__ == '__main__':
    unittest.main()
