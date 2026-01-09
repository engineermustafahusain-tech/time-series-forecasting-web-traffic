import os
import pandas as pd
import streamlit as st
import altair as alt

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Web Traffic Forecast Dashboard",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA (HF / Docker SAFE)
# --------------------------------------------------
@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)  # /app/src
    file_path = os.path.join(base_dir, "sarima_forecast_output.csv")
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# --------------------------------------------------
# SIDEBAR CONFIG
# --------------------------------------------------
st.sidebar.header("⚙️ Configuration")

server_capacity = st.sidebar.slider(
    "Server Capacity (visits/day)",
    min_value=int(df['forecast_visits'].min()),
    max_value=int(df['forecast_visits'].max()) + 500,
    value=int(df['forecast_visits'].mean())
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("📊 Web Traffic Forecast Dashboard")
st.markdown(
    "**Model:** Improved SARIMA (1,1,1)(0,1,1,7)  \n"
    "**Forecast Horizon:** 30 Days"
)

st.divider()

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------
breach_days = df[df['forecast_visits'] > server_capacity]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Forecast Traffic", int(df['forecast_visits'].mean()))
col2.metric("Peak Forecast Traffic", int(df['forecast_visits'].max()))
col3.metric("Server Capacity", server_capacity)
col4.metric("Risk Days", len(breach_days))

st.divider()

# --------------------------------------------------
# FORECAST CHART WITH CONFIDENCE & CAPACITY
# --------------------------------------------------
st.subheader("📈 Traffic Forecast with Confidence Interval & Capacity")

base = alt.Chart(df).encode(
    x=alt.X("date:T", title="Date")
)

# Forecast line
forecast_line = base.mark_line(
    color="#1f77b4",
    strokeWidth=3
).encode(
    y=alt.Y("forecast_visits:Q", title="Visits")
)

# Confidence interval
confidence_band = base.mark_area(
    opacity=0.25,
    color="#aec7e8"
).encode(
    y="lower_ci:Q",
    y2="upper_ci:Q"
)

# Server capacity line
capacity_df = pd.DataFrame({
    "date": df['date'],
    "capacity": [server_capacity] * len(df)
})

capacity_line = alt.Chart(capacity_df).mark_line(
    color="red",
    strokeDash=[6, 6],
    strokeWidth=2
).encode(
    x="date:T",
    y="capacity:Q"
)

st.altair_chart(
    (confidence_band + forecast_line + capacity_line)
    .properties(height=420),
    use_container_width=True
)

st.caption(
    "🔹 Blue line: forecast | Light blue band: uncertainty | "
    "Red dashed line: server capacity threshold"
)

st.divider()

# --------------------------------------------------
# WEEKLY PATTERN
# --------------------------------------------------
st.subheader("📅 Average Forecast Traffic by Weekday")

df['weekday'] = df['date'].dt.day_name()

weekly_avg = (
    df.groupby('weekday')['forecast_visits']
    .mean()
    .reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    .reset_index()
)

weekly_chart = alt.Chart(weekly_avg).mark_bar().encode(
    x=alt.X("weekday:N", sort=None),
    y=alt.Y("forecast_visits:Q", title="Avg Visits"),
    color=alt.Color("weekday:N", legend=None)
)

st.altair_chart(weekly_chart, use_container_width=True)

st.divider()

# --------------------------------------------------
# CAPACITY BREACH TABLE
# --------------------------------------------------
st.subheader("🚨 Capacity Breach Days")

if breach_days.empty:
    st.success("✅ No capacity breach predicted in the forecast horizon.")
else:
    st.error(f"⚠️ {len(breach_days)} days exceed server capacity.")
    st.dataframe(
        breach_days[['date', 'forecast_visits', 'upper_ci']],
        use_container_width=True
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.caption(
    "Forecast generated using Improved SARIMA model. "
    "Designed for infrastructure planning and traffic risk analysis."
)
