import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="RARIP Fatal Risk Dashboard",
    layout="wide"
)

st.title("🚗 Road Accident Fatal Risk Intelligence Dashboard")

# -------------------------------
# Load Model & Feature Columns
# -------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("model.pkl")
    feature_columns = joblib.load("feature_columns.pkl")
    return model, feature_columns

model, feature_columns = load_model()

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("Input Road Conditions")

latitude = st.sidebar.number_input("Latitude", value=52.0)
longitude = st.sidebar.number_input("Longitude", value=-1.5)
hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
speed_limit = st.sidebar.slider("Speed Limit", 20, 120, 40)

st.sidebar.markdown("---")

# -------------------------------
# Prediction Logic
# -------------------------------
if st.sidebar.button("Predict Fatal Risk"):

    # Create empty feature vector
    input_dict = {col: 0 for col in feature_columns}

    # Fill numeric fields (only if they exist in training)
    if "Latitude" in input_dict:
        input_dict["Latitude"] = latitude

    if "Longitude" in input_dict:
        input_dict["Longitude"] = longitude

    if "hour" in input_dict:
        input_dict["hour"] = hour

    if "Speed_limit" in input_dict:
        input_dict["Speed_limit"] = speed_limit

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Predict
    prob = model.predict_proba(input_df)[0][1]
    risk_score = prob * 100

    # -------------------------------
    # Display Results
    # -------------------------------
    st.subheader(f"🎯 Fatal Risk Score: {risk_score:.2f} / 100")

    if risk_score >= 70:
        st.error("🚨 High Fatal Risk Zone")
    elif risk_score >= 40:
        st.warning("⚠ Medium Fatal Risk Zone")
    else:
        st.success("✅ Low Fatal Risk Zone")

    st.markdown("---")
    st.write("Model Confidence (Fatal Probability):", f"{prob:.4f}")

else:
    st.info("Adjust road conditions and click 'Predict Fatal Risk'")
