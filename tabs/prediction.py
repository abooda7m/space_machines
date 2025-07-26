import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def render(df):
    st.header("📈 Predict Mission Success (%)")

    # ----------------------------------------
    # 1. Select features and target variable
    # ----------------------------------------
    features = [
        'Mission Duration (years)',
        'Distance from Earth (light-years)',
        'Crew Size',
        'Mission Cost (billion USD)',
        'High Risk'
    ]
    target = 'Mission Success (%)'

    # ----------------------------------------
    # 2. Prepare the data for modeling
    # ----------------------------------------
    X = df[features].copy()
    y = df[target]

    # Convert boolean column to int
    X['High Risk'] = X['High Risk'].astype(int)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train a Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    # ----------------------------------------
    # 3. Show model performance
    # ----------------------------------------
    # st.subheader("📊 Model Performance")
    # st.write(f"R² Score: **{r2_score(y_test, y_pred):.2f}**")
    # st.write(f"RMSE: **{mean_squared_error(y_test, y_pred, squared=False):.2f}**")

    # ----------------------------------------
    # 4. User input for live prediction
    # ----------------------------------------
    st.subheader("🔮 Try Your Own Mission")

    col1, col2 = st.columns(2)
    with col1:
        duration = st.slider("Mission Duration (years)", 0, 50, 10)
        distance = st.slider("Distance from Earth ", 0, 500, 100)
        crew = st.slider("Crew Size", 0, 20, 5)
    with col2:
        cost = st.slider("Mission Cost (billion USD)", 0, 300, 50)
        risk = st.selectbox("High Risk Mission?", ["Yes", "No"])
        risk_val = 1 if risk == "Yes" else 0

    # Create DataFrame for prediction
    input_data = pd.DataFrame([[duration, distance, crew, cost, risk_val]], columns=features)

    # Check if all inputs are zero (excluding High Risk)
    if input_data.drop(columns=["High Risk"]).sum().sum() == 0:
        st.warning("🚫 Cannot predict: All inputs are zero. Please provide mission details.")
    else:
        prediction = model.predict(input_data)[0]
        prediction = min(max(prediction, 0), 100)  # Cap the prediction between 0–100%
        st.success(f"🎯 Predicted Mission Success Rate: **{prediction:.2f}%**")
