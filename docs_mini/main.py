#%%
# minimal flask api

from flask import Flask, jsonify
from flask import request
from docs_mini import ocr

app = Flask(__name__)

@app.route('/hello')
def hello():
  return jsonify({'message': 'Hello, World!'})

@app.route('/ocr_document', methods=['POST'])
def ocr_document():
  if 'file' not in request.files: return jsonify({'error': 'No file uploaded'})
  
  file = request.files['file']
  if file.filename == '': return jsonify({'error': 'No file selected'})

  res = ocr.ocr_file(file)
  
  return jsonify({'message': res})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=6060)
