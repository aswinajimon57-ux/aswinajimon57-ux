import streamlit as st
import pandas as pd
from pathlib import Path


@st.cache_data
def load_data():
    # Get the SkyCity-Auckland-Project directory
    project_dir = Path(__file__).resolve().parent.parent

    # Build the correct path to the CSV file
    data_path = project_dir / "data" / "SkyCity Auckland Restaurants & Bars.csv"

    # Load the dataset
    df = pd.read_csv(data_path)

    return df
