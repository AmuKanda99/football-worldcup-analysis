import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# ----------------------------------------
# PAGE SETUP
# ----------------------------------------
st.set_page_config(
    page_title="World Cup Dashboard",
    page_icon="⚽",
    layout="wide"
)

# ----------------------------------------
# LOAD DATA
# ----------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/processed_worldcup_data.csv")

# ----------------------------------------
# DISPLAY DATA
# ----------------------------------------
data = load_data()

st.title("World Cup Dashboard")
st.subheader("Raw Data Preview")

# Show the data in an interactive table
st.dataframe(data)

if st.checkbox("Show raw data"):
    st.dataframe(data)
st.subheader("Summary Statistics")
st.write(data.describe())