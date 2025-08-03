# 🛡️ Online Payment Fraud Detection Using Machine Learning

This mini project aims to detect fraudulent activities in online payment systems using a combination of **machine learning** (for transaction analysis) and **rule-based techniques** (for phishing detection). It is developed using **Python**, **Flask**, **HTML/CSS**, and **regex logic**.

---

## 📌 Project Objective

To create a web-based system that:
- Detects phishing messages (emails, SMS, URLs) using pattern matching
- Identifies suspicious credit card transactions using trained ML models
- Provides awareness to users about different types of fraud

---

## 🚀 Project Modules

### 🔹 1. Phishing Detection and Awareness Tool
- Rule-based logic using `phishing_patterns.json`
- Scans for risky keywords in user messages, links, or emails
- Scores input and classifies it as **Phishing** or **Safe**
- Frontend: `phishing.html` (form), rendered through Flask

### 🔹 2. Transaction Fraud Detection Module
- Uses **Random Forest** model trained on credit card datasets
- Input: CSV file of transactions (e.g., `creditcard.csv`, `transactions.csv`)
- Output: Flags suspicious transactions using `fraud_model_rf.pkl` and other trained models
- Frontend: `transaction.html`, supports file upload and displays fraud output

---

## 📁 Project Structure

online-payment-fraud-detection/
│
├── app.py # Main Flask app with routing logic
├── train_model.py # Script to train ML models
├── phishing_patterns.json # JSON-based phishing detection rules
├── fraud_model_rf.pkl # Trained fraud detection model
├── supervised_model.pkl # Optional second model
├── transactions.csv # Sample transaction input
├── creditcard.csv # Dataset used for model training
│
├── templates/
│ ├── homepage.html
│ ├── phishing.html
│ ├── transaction.html
│ ├── heatmap.html
│
├── static/
│ └── transaction.js
│
├── uploads/
│ └── creditcard.csv (uploaded copy)
│
├── requirements.txt # Python dependencies
└── .gitignore # Files to exclude from version control


---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Scikit-learn**
- **Regex**
- **Pandas, NumPy**
- **HTML/CSS/JavaScript**
- **Matplotlib & Seaborn** (for visualizations)

---

## ⚙️ How to Run the Project

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/yourusername/online-payment-fraud-detection.git
cd online-payment-fraud-detection

2.pip install -r requirements.txt
3.python app.py
4.http://localhost:5000/

📨 Phishing Detection
Example Message:
"Verify your account now at http://bank-alert.ru or you will be blocked."
Result:
Phishing


###Future Improvements
Add login/authentication for users

Use deep learning for improved phishing detection

API integration for live bank data

SMS/Email alert system for detected frauds

