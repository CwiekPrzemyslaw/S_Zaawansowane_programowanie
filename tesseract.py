import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "S:/tesseract/tesseract.exe"

img = cv2.imread('z1.jpg')

pytesseract.image_to_string(img)