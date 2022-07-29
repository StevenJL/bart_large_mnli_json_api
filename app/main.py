from transformers import pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/transform', methods=['POST'])
def transform():
    parameters_json = request.get_json()
    sequence_to_classify = parameters_json['sequence_to_classify']
    candidate_labels = parameters_json['candidate_labels']
    res = classifier(sequence_to_classify, candidate_labels)
    return jsonify(res)
