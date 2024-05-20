from django.db import models
from .ocr_analysis_algorithm import OcrAnalysisAlgorithm


class Text(models.Model):
    image = models.ImageField(upload_to='images/')
    text_detected = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {"image_name": self.image.name}

    def analyze(self):
        ocr_analysis_algorithm = OcrAnalysisAlgorithm(self.image.name)
        return ocr_analysis_algorithm.character_recognition()

    def search_word(self, search_word):
        ocr_analysis_algorithm = OcrAnalysisAlgorithm(self.image.name)
        return ocr_analysis_algorithm.search_word(search_word)

    def search_information(self, criteria):
        ocr_analysis_algorithm = OcrAnalysisAlgorithm(self.image.name)
        return ocr_analysis_algorithm.search_information(criteria)
