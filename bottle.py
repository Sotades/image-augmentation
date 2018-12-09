import math
import cv2
import matplotlib as plt
import numpy as np
from bottle_features import Bottle_features

class Bottle(object):
    def __init__(self, bottle_image):

        self.bottle_image = cv2.imread(bottle_image)
        self.bottle_image_with_boxes = np.empty_like(self.bottle_image)
        self.image_height = self.bottle_image.shape[0]
        self.image_width = self.bottle_image.shape[1]

        self.boxes_across = 0
        self.boxes_down = 0
        self.box_width_px = 0
        self.box_height_px = 0

        self.features = {}
        self.initialise_feature_boxes()


    def initialise_feature_boxes(self):
        self.features[Bottle_features.LABEL_TOP_EDGE] = []
        self.features[Bottle_features.LABEL_BOTTOM_EDGE] = []
        self.features[Bottle_features.LABEL_LEFT_EDGE] = []
        self.features[Bottle_features.LABEL_RIGHT_EDGE] = []
        self.features[Bottle_features.CAP] = []

    def calculate_box_dimensions(self, desired_boxes_across: int, desired_boxes_down: int):
        """Calculate the diminsions of the boxes for a desired number of them accross and down the image

        :param desired_boxes_across: desired number of boxes to split the image into across the image
        :param desired_boxes_down: desired number of boxes to split the image into down the image
        :return: {'box_width', 'box_height'} - dictionary of box width, box height in pixels
        """

        # How tall and wide the desired box?
        self.box_width_px = math.floor(self.image_width / desired_boxes_across)
        self.box_height_px = math.floor(self.image_height / desired_boxes_down)
        return {'box_width': self.box_width_px, 'box_height': self.box_height_px}

    def draw_and_display_rectangles(self, boxes_across, boxes_down):
        """Overlay boxes over bottle image and display it

        :return: None
        """

        np.copyto(self.bottle_image_with_boxes, self.bottle_image)
        # Draw rectangles
        # TODO implement rectangles iteration
        for down_index in range(1, boxes_down):
            for across_index in range(boxes_across):

                cv2.rectangle(self.bottle_image_with_boxes, (0, 0), (64, 64), color=(0, 255, 0), thickness=1)

        cv2.imshow('image', self.bottle_image_with_boxes)
        cv2.waitKey(0)
        cv2.destroyAllWindows()






