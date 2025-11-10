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
    # Make sure the CSV file is in the same directory or use a correct relative path
    return pd.read_csv("processed_worldcup_data.csv")