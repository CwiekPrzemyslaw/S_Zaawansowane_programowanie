from flask import Flask, request, jsonify
import cv2
import numpy as np
import requests

app = Flask(__name__)

# Ścieżka do pliku z modelem i pliku z etykietami
frozen_model = 'potrzebne_pliki/frozen_inference_graph.pb'
config_file = 'potrzebne_pliki/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
classLabels = []
file_name = 'potrzebne_pliki/coco.names'

# Wczytanie etykiet
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')

# Utworzenie modelu detekcji
model = cv2.dnn_DetectionModel(frozen_model, config_file)
model.setInputSize(320, 320)
model.setInputScale((1.0/127.5))
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)


@app.route('/detect_persons/url', methods=['GET'])
def detect_persons_from_url():
    if 'url' in request.args:
        # Pobranie obrazka z URL
        url = request.args.get('url')
        response = requests.get(url)
        img = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_UNCHANGED)
        
        # Wykrycie obiektów na obrazie
        ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.48)
        
        # Zliczenie osób
        person_count = np.count_nonzero(ClassIndex == classLabels.index('person') + 1)
        
        return jsonify({'person_count': person_count})
    else:
        return jsonify({'error': 'URL parameter "url" not provided.'}), 400


@app.route('/detect_persons/image', methods=['GET'])
def detect_persons_from_image():
    if 'image' in request.files:
        # Odczytanie obrazka z przekazanego pliku
        file = request.files['image']
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        # Wykrycie obiektów na obrazie
        ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.48)
        
        # Zliczenie osób
        person_count = np.count_nonzero(ClassIndex == classLabels.index('person') + 1)
        
        return jsonify({'person_count': person_count})
    else:
        return jsonify({'error': 'No image provided in the request.'}), 400


@app.route('/detect_persons', methods=['POST'])
def detect_persons_post():
    if 'image' in request.files:
        # Odczytanie obrazka z przekazanego pliku
        file = request.files['image']
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        # Wykrycie obiektów na obrazie
        ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.48)
        
        # Zliczenie osób
        person_count = np.count_nonzero(ClassIndex == classLabels.index('person') + 1)
        
        return jsonify({'person_count': person_count})
    else:
        return jsonify({'error': 'No image provided in the request.'}), 400


if __name__ == '__main__':
    app.run(debug=True)
