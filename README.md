# 🚗 Road Accident Fatal Risk Intelligence Platform (RARIP)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost-orange)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Deployment%20Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview

RARIP is an AI-powered system that predicts fatal accident probability using spatio-temporal modeling and imbalance-aware machine learning.

It processes 2M+ accident records and generates:

- Fatal risk probability
- Risk score (0–100)
- Risk classification (Low / Medium / High)
- Interactive deployment dashboard

---

## 🎯 Problem Statement

Road accidents are predictable but rarely prevented.

Cities rely on historical blackspot lists instead of proactive fatal risk prediction.

RARIP aims to:

- Detect high-risk zones before fatalities occur
- Provide explainable risk scoring
- Support smart-city safety initiatives

---

## 🧠 Technical Architecture

### 1️⃣ Data Pipeline
- Cleaned 2M+ accident records
- Feature engineering (month, day_of_week, hour)
- Binary fatal classification target
- Imbalance handling (scale_pos_weight ≈ 77)

### 2️⃣ ML Model
- XGBoost Binary Classifier
- Imbalance-aware training
- Threshold tuning
- ROC-AUC ≈ 0.74
- Fatal recall up to 88%

### 3️⃣ Risk Engine
- Probability → Risk Score (0–100)
- Risk classification bands
- Grid-based spatial aggregation
- Blackspot detection

### 4️⃣ Deployment Layer
- Streamlit Dashboard
- Model artifact loading (model.pkl)
- Feature alignment (feature_columns.pkl)
- Production-safe input handling

---

## 📊 Model Performance

| Metric | Value |
|--------|--------|
| Dataset Size | 2,047,081 records |
| Fatal Rate | 1.28% |
| ROC-AUC | ~0.74 |
| Fatal Recall | 65–88% (threshold tuned) |

---

## 📁 Project Structure

```bash
road-accident-risk-intelligence/
│
├── notebooks/
│   ├── 01_data_pipeline_clean.ipynb
│   └── 02_model_training.ipynb
│
├── app/
│   └── dashboard.py
│
├── model.pkl
├── feature_columns.pkl
│
├── docs/
│   └── fatal_risk_heatmap.html
│
├── requirements.txt
└── README.md
```
---

## 🚀 How To Run Locally

### 1️⃣ Clone Repository
```
git clone https://github.com/MdShabazS/road-accident-risk-intelligence.git
```
```
cd road-accident-risk-intelligence
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run Dashboard
```
streamlit run app/dashboard.py
```
Dashboard will open at:
```
https://localhost:8501
```
---

## 🔎 Explainability (SHAP)

The system supports SHAP-based feature importance analysis to explain:

- Which features increase fatal risk
- Which road conditions reduce risk
- Model decision patterns

---

## 🌍 Use Cases

- Municipal Corporations
- Highway Authorities
- Insurance Risk Modeling
- Smart City Safety Programs

---

## 🚀 Future Enhancements

- SHAP visualization in dashboard
- Real-time weather API integration
- FastAPI REST API
- Cloud deployment (Docker + AWS)
- Graph Neural Network upgrade

---

## 👨‍💻 Author

MdShabazS  
Electronics & Communication Engineering  
Embedded & AI Systems Enthusiast  

---

## 📜 License

MIT License

