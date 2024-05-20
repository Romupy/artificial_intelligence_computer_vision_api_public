import os
import cv2
import uuid
from statistics import median
import numpy as np


class FaceAnalysisAlgorithm:
    """
    Class for facial analysis.

    This class provides methods for detecting faces in an image, analyzing
    facial skin brightness, and determining the type of facial skin.

    Attributes:
    image_name (str): The file path of the image to be analyzed.

    Methods:
    face_detection(): Detects faces in an image and analyzes facial skin.
    __skin_brightness_detection(coordinates, sizes, gray_image_name):
        Detects facial skin brightness.
    __skin_type_detection(result): Determines the type of facial skin.
    __remove_double_detection(rectangles): Removes rectangles containing
    others.
    """

    PATH = 'face/classifiers/'
    CASCADE_PATHS = [
        os.path.abspath(PATH + 'haarcascade_frontalface_default.xml'),
        os.path.abspath(PATH + 'haarcascade_profileface.xml'),
    ]
    ALGORITHM_PARAMETERS = [
        {'scale_factor': 1.45, 'min_neighbors': 5},
        {'scale_factor': 1.48, 'min_neighbors': 6},
        {'scale_factor': 1.55, 'min_neighbors': 6},
        {'scale_factor': 1.60, 'min_neighbors': 6},
        {'scale_factor': 1.70, 'min_neighbors': 6}
    ]

    # **********************************************************
    # *  ____  _____  _   _  ____    ___   ____   _____  ____  *
    # * / ___|| ____|| \ | |/ ___|  / _ \ |  _ \ | ____||  _ \ *
    # *| |    |  _|  |  \| |\___ \ | | | || |_) ||  _|  | | | |*
    # *| |___ | |___ | |\  | ___) || |_| ||  _ < | |___ | |_| |*
    # * \____||_____||_| \_||____/  \___/ |_| \_\|_____||____/ *
    # **********************************************************

    def __init__(self, image_name):
        """
        Initializes a Face object.

        Keyword arguments::
        image_name (str): The file path of the image to be analyzed.
        """
        self.image_name = image_name

    def face_detection(self):
        """
        Method that detects faces in an image.

        This method utilizes a Haar Cascade classifier to detect faces in the
        provided image.
        Detected faces are processed to remove rectangles containing others,
        and the remaining rectangles are analyzed for facial skin brightness.

        Returns:
        dict -- Dictionary containing the number of faces detected and
        information about the facial skin.
        Example: {'Nnmber_of_faces_detected': 2, 'facial_skin': [...]}
        """
        gray = None
        faces_detected_results = None
        img = None

        # **********************************************************
        # *  ____  _____  _   _  ____    ___   ____   _____  ____  *
        # * / ___|| ____|| \ | |/ ___|  / _ \ |  _ \ | ____||  _ \ *
        # *| |    |  _|  |  \| |\___ \ | | | || |_) ||  _|  | | | |*
        # *| |___ | |___ | |\  | ___) || |_| ||  _ < | |___ | |_| |*
        # * \____||_____||_| \_||____/  \___/ |_| \_\|_____||____/ *
        # **********************************************************

        return {"number_of_faces_detected": len(faces),
                "facial_skin": skin_brightness}

    @staticmethod
    def __skin_brightness_detection(coordinates, sizes, gray_image_name):
        """
        Method that detects facial skin brightness.

        This method analyzes the brightness of facial skin in the specified
        region of the grayscale image.

        Keyword arguments:
        coordinates (dict): Dictionary containing the 'x' and 'y' coordinates
        of the region.
        sizes (dict): Dictionary containing the width ('w') and height ('h') of
        the region.
        gray_image_name (str): The file path of the grayscale image to be
        analyzed.

        Returns:
        dict: A dictionary containing the brightness of the facial skin in the
        specified region rounded to two decimal places and skin information.
        Example: {'skin_brightness': 0.75, 'skin_info': 'light skin'}
       """
        img = cv2.imread(gray_image_name)

        # **********************************************************
        # *  ____  _____  _   _  ____    ___   ____   _____  ____  *
        # * / ___|| ____|| \ | |/ ___|  / _ \ |  _ \ | ____||  _ \ *
        # *| |    |  _|  |  \| |\___ \ | | | || |_) ||  _|  | | | |*
        # *| |___ | |___ | |\  | ___) || |_| ||  _ < | |___ | |_| |*
        # * \____||_____||_| \_||____/  \___/ |_| \_\|_____||____/ *
        # **********************************************************

        return {"skin_brightness": result, "skin_info": skin_info}

    @staticmethod
    def __skin_type_detection(result):
        """
        Method that detects the type of facial skin based on brightness result.

        Keyword arguments:
        result (float): The brightness result of the facial skin in the
        specified region.

        Returns:
        str: String indicating the detected type of facial skin.
        Possible values: 'dark skin', 'matte skin', 'light skin', 'no skin'.
        """

        # **********************************************************
        # *  ____  _____  _   _  ____    ___   ____   _____  ____  *
        # * / ___|| ____|| \ | |/ ___|  / _ \ |  _ \ | ____||  _ \ *
        # *| |    |  _|  |  \| |\___ \ | | | || |_) ||  _|  | | | |*
        # *| |___ | |___ | |\  | ___) || |_| ||  _ < | |___ | |_| |*
        # * \____||_____||_| \_||____/  \___/ |_| \_\|_____||____/ *
        # **********************************************************

    @staticmethod
    def __remove_double_detection(rectangles):
        """
        Method that removes double detection, the method that removes
        rectangles containing others from the list.

        This method takes a list of rectangles represented as tuples
        (x, y, w, h).
        It removes rectangles that contain other rectangles.

        Keyword arguments:
        rectangles -- List of rectangles to be processed.
                      Represented as tuples (x, y, w, h).

        Returns:
        List -- List of rectangles that do not contain any other rectangles.
        """
        retained_rectangles = []
        for i in range(len(rectangles)):
            x_i, y_i, w_i, h_i = rectangles[i]
            is_contained = False
            for j in range(len(rectangles)):
                if i != j:
                    x_j, y_j, w_j, h_j = rectangles[j]
                    if (x_i <= x_j and y_i <= y_j and x_i + w_i >= x_j + w_j
                            and y_i + h_i >= y_j + h_j):
                        is_contained = True
                        break
            if not is_contained:
                retained_rectangles.append((x_i, y_i, w_i, h_i))
        return retained_rectangles

    @staticmethod
    def __rotate_image(img, angle):
        """
        Method that rotates an image.

        This method rotates an image by the specified angle.

        Keyword arguments:
        img -- Image to be rotated.
        angle -- Angle in degrees.

        Returns:
        Image -- Rotated image.
        """
        height, width = img.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))
        return rotated_image
