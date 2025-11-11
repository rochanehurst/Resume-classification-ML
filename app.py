from flask import Flask, request, jsonify, render_template
import joblib
import re
from io import BytesIO
from PyPDF2 import PdfReader

app = Flask(__name__)

# ===== LOAD MODEL AND OBJECTS =====
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')


# ===== CLEANING FUNCTION =====
def clean_input(text):
    text = str(text).replace(',', '\n')
    skills_list = text.split('\n')
    cleaned_skills = []
    for skill in skills_list:
        skill = skill.strip().lower()
        skill = re.sub(r'[^a-z0-9\s]', ' ', skill)
        skill = re.sub(r'\s+', ' ', skill)
        if skill:
            cleaned_skills.append(skill)
    return ' '.join(cleaned_skills)


# ===== TEXT EXTRACTION FROM PDF =====
def extract_text_from_pdf(file_stream):
    """Extracts text from a PDF file."""
    pdf_reader = PdfReader(BytesIO(file_stream))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text


# ===== ROUTES =====
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['resume']
    filename = file.filename.lower()

    # Handle PDF or TXT
    if filename.endswith('.pdf'):
        text = extract_text_from_pdf(file.read())
    elif filename.endswith('.txt'):
        text = file.read().decode('utf-8', errors='ignore')
    else:
        return jsonify({'error': 'Unsupported file type. Please upload .pdf or .txt'}), 400

    cleaned_text = clean_input(text)
    X = vectorizer.transform([cleaned_text])
    pred_num = model.predict(X)[0]
    pred_label = label_encoder.inverse_transform([pred_num])[0]

   
    return jsonify({'predicted_job': pred_label})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
