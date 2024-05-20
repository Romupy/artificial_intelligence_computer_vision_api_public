## Artificial Intelligence Computer Vision API (Censored Version)
API for image analysis based on computer vision, facial_recognition and OCR. 

## facial_recognition
Endpoints:
- ### [POST] /facial_recognition/analyze_faces

• form-data
- image: image file

## Optical character recognition

- ### [POST] /ocr/detect_text

• form-data
- image: image file

- ### [POST] /ocr/search_word

• form-data
- image: image file
- search_word: word

-  ### [POST] /ocr/search_information

• form-data
- image: image file
- criteria: word criteria
