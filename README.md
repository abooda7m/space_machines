# 🚀 Space Missions Dataset Analysis

This project provides a comprehensive analysis of a synthetic **Space Missions Dataset** using **Python**, **Pandas**, and **Streamlit** for interactive visualization. The dashboard enables exploration of numerical and categorical features related to various space missions.

---

## 📂 Dataset Overview

The dataset contains detailed information about numerous space missions, with **14 columns** (8 numerical, 6 categorical), including:

- **Mission ID**: Unique identifier  
- **Mission Name**, **Mission Type**, **Target Type**, **Target Name**  
- **Launch Date**, **Launch Vehicle**  
- **Distance from Earth (light-years)**  
- **Mission Duration (years)**  
- **Mission Cost (billion USD)**  
- **Scientific Yield (points)**  
- **Crew Size**  
- **Mission Success (%)**  
- **Fuel Consumption (tons)**  
- **Payload Weight (tons)**  

---

## 🎯 Problem Statement

Space missions are complex operations influenced by numerous factors like cost, duration, payload, and distance. This project aims to analyze such variables to reveal meaningful patterns that could enhance mission planning and success.

---

## 🔍 Objectives

- Explore and visualize mission characteristics and distribution.
- Analyze correlations between mission cost, duration, crew size, and success.
- Identify patterns in scientific yield, fuel consumption, and payload distribution.
- Provide regression insights into how distance impacts mission duration.

---

### 🤖 Model Overview  

This project utilizes a **Linear Regression** model to predict the success rate of space missions based on parameters like mission duration, distance, crew size, cost, and risk level. The model was selected for its simplicity, efficiency, and interpretability. It achieved an **R² score of 0.84** and an **RMSE of 4.09**, indicating strong predictive performance.

---

## 🛠️ Project Structure

```
project/
│
├── landingPage.py                # Streamlit app entry point
├── data/
│   └── space_missions_dataset.csv
│
├── tabs/
│   ├── data_overview.py         # Dataset description
│   ├── categorical_analysis.py  # ِALL categorical visualizations
│   └── numerical_analysis.py    # All numerical visualizations
│
├── requirements.txt             # Required Python libraries
└── README.md             
```

---

## 📊 Visualizations Highlights

- **Numerical Summary Table**: Descriptive statistics of all numerical columns.
- **Cost & Duration Trends**: Over time and by payload size.
- **Fuel vs Distance**: Line plot to explore fuel efficiency.
- **Regression Analysis**: How distance affects mission duration.
- **Success Rates**: Per budget category and crew size.
- **Scientific Yield**: Changes by rounded mission duration.

---

## 💡 Technologies Used

- **Python** (Pandas, Plotly, Streamlit)
- **Data Wrangling**: `pandas`, `datetime`
- **Visualization**: `plotly.express`, `px.scatter`, `px.line`, `px.bar`
- **Deployment Ready**: Compatible with Streamlit Cloud or local hosting.

---

## ▶️ Running the App

To run the project locally using `uv`:

### 1. Install `uv` (if not already installed)

```bash
pip install uv
```

> `uv` is a fast Python package manager that replaces pip and virtualenv.

---

### 2. Create and activate a virtual environment

```bash
uv venv venv
venv\Scripts\activate  # On Windows
# or on Mac/Linux:
# source venv/bin/activate
```

---

### 3. Install required packages

```bash
uv pip install -r requirements.txt
```

---

### 4. Run the Streamlit app

```bash
streamlit run landingPage.py
```

---

## 📌 Notes

This is a synthetic dataset created for educational purposes. The relationships are designed to mimic real-world patterns but do not represent actual mission data.

---

## 📈 Sample Insight

> Missions with higher budgets and moderate durations tend to yield better success rates.  
> Distance from Earth shows a strong linear correlation with mission duration.
