import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page setup
st.set_page_config(page_title="Advanced EDA & Feature Engineering Dashboard", layout="wide")
st.title("📊 EDA Engineering Dashboard")
st.markdown("Interact with the final product of your clean, engineered Python data pipeline.")

# Load or generate clean preview data
@st.cache_data
def load_data():
    try:
        return pd.read_csv('cleaned_data.csv')
    except FileNotFoundError:
        np.random.seed(42)
        df_mock = pd.DataFrame({
            'Customer_ID': range(1001, 2001),
            'Age': np.random.randint(18, 70, size=1000),
            'Income': np.random.normal(55000, 12000, size=1000),
            'Total_Spend': np.random.exponential(200, size=1000),
            'Purchase_Count': np.random.randint(1, 50, size=1000),
            'City': np.random.choice(['New York', 'Los Angeles', 'Chicago'], size=1000),
            'Avg_Spend_Per_Purchase': np.random.uniform(5, 50, size=1000),
            'Income_Spend_Ratio': np.random.uniform(0.001, 0.05, size=1000),
            'Age_Group': np.random.randint(1, 4, size=1000)
        })
        return df_mock

df = load_data()

# Interactive Sidebar Filters
st.sidebar.header("🔍 Dataset Filters")
selected_city = st.sidebar.multiselect("Select City:", options=df['City'].dropna().unique(), default=df['City'].dropna().unique())
age_range = st.sidebar.slider("Select Age Range:", int(df['Age'].min()), int(df['Age'].max()), (int(df['Age'].min()), int(df['Age'].max())))

# Apply filters dynamically
filtered_df = df[(df['City'].isin(selected_city)) & (df['Age'].between(age_range[0], age_range[1]))]

# Key Performance Indicators
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", f"{len(filtered_df):,}")
col2.metric("Avg Customer Income", f"${filtered_df['Income'].mean():,.2f}")
col3.metric("Avg Total Spend", f"${filtered_df['Total_Spend'].mean():,.2f}")
col4.metric("Avg Spend/Purchase", f"${filtered_df['Avg_Spend_Per_Purchase'].mean():,.2f}")

st.markdown("---")

# Visual Charts for Engineered Features
st.subheader("🚀 Engineered Features Distribution Analysis")
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.write("##### Feature 1: Average Spend per Purchase Distribution")
    fig_spend = px.histogram(filtered_df, x="Avg_Spend_Per_Purchase", color="City", nbins=30, barmode="overlay", template="plotly_dark")
    st.plotly_chart(fig_spend, use_container_width=True)

with chart_col2:
    st.write("##### Feature 2: Income-to-Spend Ratio vs. Customer Age")
    fig_scatter = px.scatter(filtered_df, x="Age", y="Income_Spend_Ratio", color="City", template="plotly_dark")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Dataset Dataframe Preview
st.subheader("📋 Clean Dataset Snapshot")
st.dataframe(filtered_df.head(50), use_container_width=True)
