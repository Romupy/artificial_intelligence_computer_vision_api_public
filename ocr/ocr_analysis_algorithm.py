import random
import re

import cv2
import numpy as np
import pytesseract as ptess
import os
import uuid
import re
from unidecode import unidecode

class OcrAnalysisAlgorithm:
    DETECTION_CONFIDENCE = 60

    def __init__(self, image_name):
        """
        Initializes a Face object.

        Keyword arguments::
        image_name (str): The file path of the image to be analyzed.
        """
        self.image_name = image_name

    def __image_pre_processing(self):

        # **********************************************************
        # *  ____  _____  _   _  ____    ___   ____   _____  ____  *
        # * / ___|| ____|| \ | |/ ___|  / _ \ |  _ \ | ____||  _ \ *
        # *| |    |  _|  |  \| |\___ \ | | | || |_) ||  _|  | | | |*
        # *| |___ | |___ | |\  | ___) || |_| ||  _ < | |___ | |_| |*
        # * \____||_____||_| \_||____/  \___/ |_| \_\|_____||____/ *
        # **********************************************************

        return

    def character_recognition(self):
        """
        Detects characters in an image.

        Returns:
        str: The text detected in the image.
        """
        bc_image, image = self.__image_pre_processing()
        data = ptess.image_to_data(bc_image, output_type=ptess.Output.DICT)
        detected_text = ""
        for word, conf, left, top, width, height in zip(
                data["text"], data["conf"], data["left"],
                data["top"], data["width"], data["height"]
        ):
            if int(conf) > self.DETECTION_CONFIDENCE:
                detected_text += word + " "
                cv2.rectangle(
                    image, (left, top), (left + width, top + height),
                    (0, 255, 0), 2
                )
        cv2.imwrite(self.image_name, image)
        return {"text": detected_text.strip()}

    def search_word(self, search_word):
        result = {"count": 0, "locations": [], "words_found": []}
        bc_image, image = self.__image_pre_processing()
        data = ptess.image_to_data(bc_image, output_type=ptess.Output.DICT)
        for word, conf, left, top, width, height in zip(
                data["text"], data["conf"], data["left"],
                data["top"], data["width"], data["height"]
        ):
            word = re.sub(r'[^\w\s]', '', word)
            if int(conf) > self.DETECTION_CONFIDENCE \
                    and word.lower() == search_word.lower():
                result["count"] += 1
                result["locations"].append(
                    {"left": left, "top": top, "width": width, "height": width}
                )
                result["words_found"].append(word)
                cv2.rectangle(
                    image, (left, top), (left + width, top + height),
                    (0, 255, 0), 2
                )
        cv2.imwrite(self.image_name, image)
        return result

    def search_information(self, criteria):
        count = 0
        result = ""
        bc_image, image = self.__image_pre_processing()
        data = ptess.image_to_data(bc_image, output_type=ptess.Output.DICT)
        search_word_result = []
        i = 0
        for word, conf, left, top, width, height in zip(
                data["text"], data["conf"], data["left"],
                data["top"], data["width"], data["height"]
        ):
            word = re.sub(r'[^\w\s]', '', word)
            if int(conf) > self.DETECTION_CONFIDENCE \
                    and word.lower() == criteria.lower():
                count += 1

                # **********************************************************
                # *  ____  _____  _   _  ____    ___   ____   _____  ____  *
                # * / ___|| ____|| \ | |/ ___|  / _ \ |  _ \ | ____||  _ \ *
                # *| |    |  _|  |  \| |\___ \ | | | || |_) ||  _|  | | | |*
                # *| |___ | |___ | |\  | ___) || |_| ||  _ < | |___ | |_| |*
                # * \____||_____||_| \_||____/  \___/ |_| \_\|_____||____/ *
                # **********************************************************
