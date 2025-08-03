from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import random
import re
import os
import json


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze-upload', methods=['POST'])
def analyze_upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        df = pd.read_csv(file)
        df = df.head(20)
        if 'Class' in df.columns:
            df = df.drop(columns=['Class'])
        df['Fraud'] = [random.choice(['Fraud', 'Not Fraud']) for _ in range(len(df))]

       
        fraud_count = df['Fraud'].value_counts().to_dict()
        risk_data = [{'label': label, 'count': fraud_count.get(label, 0)} for label in ['Fraud', 'Not Fraud']]

        result = df.to_dict(orient='records')
        return jsonify({
            'result': result,
            'columns': df.columns.tolist(),
            'risk_data': risk_data
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
with open("phishing_patterns.json", "r") as f:
 phishing_rules = json.load(f)

@app.route("/phishing-check", methods=["POST"])
def phishing_check():
    data = request.get_json()
    user_input = data.get("text", "")
    text = re.sub(r"[^\w\s:/.-]", "", user_input.lower())

    score = 0
    matches = []

    
    weight_map = {
        "high": 50,
        "medium": 30,
        "low": 20
    }

   
    for risk_level, patterns in phishing_rules.items():
        weight = weight_map.get(risk_level, 0)
        for pattern in patterns:
            if re.search(pattern, text):
                score += weight
                matches.append(f"{risk_level.title()} risk: matched '{pattern}'")

    score = min(score, 100)
    status = "Phishing" if score >= 50 else "Safe"

    return jsonify({
        "input": user_input,
        "score": score,
        "status": status,
        "matches": matches
    })

if __name__ == '__main__':
    app.run(debug=True)
