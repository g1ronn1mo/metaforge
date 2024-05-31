from flask import Flask, request, jsonify
from langchain_community.document_transformers import DoctranPropertyExtractor
from langchain_core.documents import Document
import json
import os

app = Flask(__name__)

# Load properties from properties.json file
with open('properties.json', 'r') as file:
    properties = json.load(file)

property_extractor = DoctranPropertyExtractor(properties=properties)

@app.route('/extract', methods=['POST'])
def extract_properties():
    data = request.json
    sample_text = data.get('text', '')
    documents = [Document(page_content=sample_text)]
    
    extracted_document = property_extractor.transform_documents(documents, properties=properties)
    return jsonify(extracted_document[0].metadata)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)