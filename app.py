from flask import Flask, request, render_template, send_file
import os
from convert_csv import convert_csv

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'

# Ensure upload and converted directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    input_file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_file_path)

    # Define output file path
    output_file_path = os.path.join(CONVERTED_FOLDER, 'converted_' + file.filename)

    # Convert the file
    convert_csv(input_file_path, output_file_path)

    return send_file(output_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
