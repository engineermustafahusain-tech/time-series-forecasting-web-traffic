🚀 Project Overview

This project delivers an end-to-end web traffic forecasting solution using classical time-series modeling (SARIMA) with deep learning benchmarking (LSTM) and an interactive Streamlit dashboard.

The system forecasts daily website traffic, visualizes uncertainty using confidence intervals, and supports server capacity planning by identifying high-risk traffic days.

🎯 Business Problem

Modern websites must anticipate traffic demand to:

Prevent server overloads

Optimize infrastructure costs

Plan marketing campaigns effectively

Improve user experience during peak traffic

Problem Statement:

How can we accurately forecast future website traffic and proactively identify days where demand may exceed server capacity?

💡 Business Solution

Forecast daily traffic using SARIMA, a proven statistical time-series model

Benchmark performance against LSTM to validate model choice

Quantify uncertainty with confidence intervals

Visualize forecasts and capacity risks using an interactive dashboard

🧠 Key Features

✅ Daily web traffic forecasting (30-day horizon)

✅ Weekly seasonality detection (weekday vs weekend behavior)

✅ Confidence interval–based risk analysis

✅ Server capacity threshold visualization

✅ SARIMA vs LSTM performance comparison

✅ Production-ready Streamlit dashboard


📊 Dataset Description

The project uses real-world Google Analytics–style session data, aggregated to daily traffic.

Key Columns Used
Column	Description
date	Date of traffic
totalVisits	Number of website visits
forecast_visits	Predicted traffic
lower_ci	Lower confidence bound
upper_ci	Upper confidence bound
🔬 Modeling Approach
1️⃣ Data Preparation

Aggregated session-level data to daily traffic

Ensured date continuity (no missing days)

Handled missing values and anomalies

2️⃣ Stationarity Check

Applied ADF test

Used first-order differencing (d = 1)

3️⃣ Model Selection
SARIMA (Final Model)
SARIMA(1,1,1)(0,1,1,7)


Why SARIMA?

Captures weekly seasonality naturally

Performs well with limited data

Highly interpretable for business use

4️⃣ Variance Stabilization

Applied log transformation

Reduced heteroskedasticity

Improved RMSE and residual behavior

5️⃣ LSTM Benchmark (Experimental)

Built an LSTM model using sliding windows

Used Min-Max scaling and early stopping

Compared against SARIMA using identical train-test split

📈 Model Performance Comparison
Model	MAE	RMSE
SARIMA (Baseline)	328	369
Improved SARIMA	316	362
LSTM	344	397

✅ Final Model Choice

Improved SARIMA was selected due to:

Lower error

Better stability

Higher interpretability

Strong performance with limited data

📊 Dashboard Overview

The Streamlit dashboard provides:

🔹 KPI Cards

Average forecast traffic

Peak traffic

Server capacity

Risk days count

🔹 Forecast Visualization

Traffic forecast line

Confidence interval band

Server capacity alert line

🔹 Risk Analysis

Automatic identification of days exceeding capacity

Actionable insights for infrastructure planning

⚙️ Server Capacity Logic :

1) If forecast_visits > server_capacity:
    Flag as high-risk day


This enables:

Proactive scaling

Load balancing

Marketing campaign adjustments

🛠️ Tech Stack

Python

Pandas / NumPy

Statsmodels (SARIMA)

TensorFlow / Keras (LSTM)

Streamlit

Altair

Scikit-learn

▶️ How to Run Locally
git clone https://github.com/your-username/web-traffic-forecasting-dashboard.git
cd web-traffic-forecasting-dashboard
pip install -r requirements.txt
streamlit run src/streamlit_app.py

🚀 Deployment

Designed for Hugging Face Spaces

Compatible with Streamlit Cloud

Docker-friendly file structure

📌 Key Takeaways

Classical models can outperform deep learning on structured, seasonal data

Model simplicity + interpretability matter in production

Forecast uncertainty is as important as point predictions

Business-driven dashboards add real value

📄 Future Improvements

Add holiday and campaign indicators (SARIMAX)

Extend forecast horizon dynamically

Automated retraining pipeline

Email / Slack alerts for capacity breaches

👤 Author

Syed Mustafa Husain
B.Tech (IoT) | Data Science & ML Enthusiast
Focus: Time Series Forecasting, Analytics, ML Systems

⭐ Final Note

This project demonstrates end-to-end ownership — from data preparation and modeling to deployment and business interpretation — mirroring real-world industry workflows.
