# EDA Engineering Dashboard

An interactive, production-ready DataOps pipeline and Streamlit dashboard built to clean raw data, handle statistical anomalies, engineer high-impact business features, and visualize data trends instantly.

##  Features & Pipeline Stages
- **Data Cleanup:** Automatic boundary correction for age entry errors (-5 and 120 anomalies rectified).
- **Missing Value Imputation:** Statistical median handling combined with Advanced K-Nearest Neighbors (KNN) Imputation for missing continuous metrics.
- **Outlier Neutralization:** Mathematical capping and flooring utilizing the Interquartile Range (IQR) method.
- **Feature Engineering:** 
  - `Avg_Spend_Per_Purchase` (Mathematical ratio profiling)
  - `Income_Spend_Ratio` (Financial health indicator)
  - `Age_Group` (Continuous demographic binning)
- **Interactive App UI:** Interactive Streamlit dashboard integrated with dynamic filtering controls and responsive Plotly charts.

##  Tech Stack
- **Languages:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Plotly, Streamlit
- **Environment:** Visual Studio Code & Jupyter Notebooks

## Installation & How to Run
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```
2. Install the necessary project dependencies:
   ```bash
   pip install streamlit plotly pandas numpy scikit-learn
   ```
3. Boot up the interactive application server:
   ```bash
   python -m streamlit run app.py
   ```
