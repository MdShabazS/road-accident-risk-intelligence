\# 🚗 Road Accident Risk Intelligence Platform (RARIP)



\## 📌 Overview

An AI-powered system that predicts fatal accident probability and identifies high-risk road zones using spatio-temporal modeling and imbalance-aware machine learning.



---



\## 🎯 Problem

Road accidents are predictable but rarely prevented. Cities rely on historical blackspot lists instead of proactive fatal risk prediction.



---



\## 🧠 Solution

RARIP predicts fatal accident probability using:



\- XGBoost Binary Classifier

\- Class imbalance handling (scale\_pos\_weight ≈ 77)

\- Spatio-temporal feature engineering

\- Grid-based spatial risk aggregation

\- Interactive heatmap visualization



---



\## 📊 Model Performance



\- Dataset Size: 2M+ accident records

\- ROC-AUC: ~0.74

\- Fatal Recall: 65–88% (threshold-tuned)

\- Imbalance-Aware Training



---



\## 🌍 Features



✔ Fatal risk scoring (0–100 scale)  

✔ Low / Medium / High risk classification  

✔ Spatial blackspot detection  

✔ Interactive heatmap export  

✔ Deployable architecture blueprint  



---



\## 🏗 Architecture



Data Pipeline → Feature Engineering → XGBoost Fatal Risk Model → Risk Scoring Engine → Spatial Aggregation → Interactive Dashboard



---



\## 📁 Project Structure



road-accident-risk-intelligence/

│

├── notebooks/

│ ├── 01\_data\_pipeline\_clean.ipynb

│ └── 02\_model\_training.ipynb

│

├── docs/

│ └── fatal\_risk\_heatmap.html

│

├── requirements.txt

├── PROJECT\_SUMMARY.txt

└── README.md



---



\## 🚀 Future Enhancements



\- SHAP explainability

\- Real-time weather integration

\- FastAPI deployment

\- City-level SaaS deployment



---



\## 📌 Use Cases



\- Municipal corporations

\- Highway authorities

\- Insurance companies

\- Smart city initiatives





