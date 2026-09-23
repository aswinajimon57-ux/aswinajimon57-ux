# SkyCity Auckland Order Channel Intelligence Dashboard

> A Streamlit-based hospitality analytics dashboard for analyzing restaurant order channels, profitability, channel diversification, and aggregator dependency across the SkyCity Auckland dataset.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/python/)

## 🚀 Live Demo

**[Open the Live Streamlit Dashboard](https://aswinajimon57-ux-aizl4e4vffcbkx9xyuwhem.streamlit.app/)**


---

## Project Overview

The **SkyCity Auckland Order Channel Intelligence Dashboard** is an end-to-end data analytics project designed to examine how hospitality businesses receive orders across different channels and how channel mix relates to profitability and aggregator dependency.

The dashboard transforms restaurant-level order data into an interactive business intelligence view covering:

- Total monthly order volume
- Active restaurant count
- Average order value
- In-store market share
- Delivery vs. in-store order dominance
- Net profit by ordering channel
- Channel diversification
- Aggregator dependency and risk categories
- Automated executive-level insights

The project demonstrates practical skills in **data cleaning, validation, KPI engineering, business analytics, interactive visualization, and Streamlit deployment**.

---

## Business Problem

Hospitality businesses often operate through a combination of direct and third-party ordering channels. Understanding the contribution and dependency of each channel can help analysts identify:

- Which channels generate the largest order volumes
- How profitability differs between channels
- Whether businesses are overly dependent on aggregators
- How diversified the ordering mix is
- Where direct ordering channels may require further attention

This project converts those questions into an interactive analytics dashboard.

---

## Key Features

### 1. Executive KPI Dashboard

The dashboard provides high-level KPIs including:

- **Total Monthly Orders**
- **Active Restaurants**
- **Average Order Value**
- **In-Store Share**

### 2. Global Filtering

Users can dynamically filter the analysis by:

- Subregion
- Cuisine Type
- Business Segment

All downstream KPIs and visualizations update based on the selected filters.

### 3. Delivery vs. In-Store Analysis

Compares:

- In-Store Orders
- Uber Eats Orders
- DoorDash Orders
- Self-Delivery Orders

The dashboard also presents an aggregated **Delivery vs. In-Store** comparison.

### 4. Channel Profitability

Net profit is calculated and compared across:

- In-Store
- Uber Eats
- DoorDash
- Self Delivery

This provides a channel-level profitability perspective rather than focusing only on order volume.

### 5. Channel Diversification

A diversification score is calculated for each business and visualized as a distribution.

This helps identify differences in how concentrated or diversified businesses are across ordering channels.

### 6. Aggregator Dependency Risk

The project calculates an aggregator-dependence measure and classifies businesses into:

| Risk Category | Threshold |
|---|---:|
| Balanced | < 50% |
| Moderate Risk | 50%–69.99% |
| High Risk | ≥ 70% |

These thresholds are analytical rules defined for this project and should not be interpreted as an industry-standard risk framework.

### 7. Automated Executive Insights

The dashboard automatically identifies:

- Dominant ordering channel
- Average aggregator dependency
- Overall dependency status
- A direct-channel strategy message

---

## Dashboard Preview

Add screenshots of the deployed application to an `assets/` folder.

Recommended screenshots:

### Executive Dashboard
![Executive Dashboard](assets/dashboard-overview.png)

### Channel Profitability
![Channel Profitability](assets/channel-profitability.png)

### Aggregator Dependency & Risk
![Aggregator Dependency](assets/aggregator-risk.png)

### Interactive Filters
![Dashboard Filters](assets/filters.png)

> Recommended screenshot size: approximately 1600×900 or 1920×1080. Crop out browser tabs/address bars where possible.

---

## Data & Analytics Workflow

```text
Raw Restaurant Dataset
        ↓
Data Loading
        ↓
Validation
        ↓
KPI / Feature Engineering
        ↓
Interactive Filtering
        ↓
Business Metrics
        ↓
Visual Analytics
        ↓
Automated Executive Insights
```

### Data processing modules

The project separates core functionality into reusable modules:

```text
utils/
├── data_loader.py
├── kpi_calculator.py
└── validation.py
```

This keeps data loading, validation, and KPI calculations separate from the Streamlit presentation layer.

---

## Project Structure

```text
SkyCity-Auckland-Project/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── SkyCity Auckland Restaurants & Bars.csv
│
└── utils/
    ├── data_loader.py
    ├── kpi_calculator.py
    └── validation.py
```

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming and analytics |
| Pandas | Data manipulation and aggregation |
| NumPy | Numerical operations |
| Plotly | Interactive visualizations |
| Streamlit | Dashboard development and deployment |
| OpenPyXL | Excel-related data support |
| Git & GitHub | Version control and portfolio hosting |

---

## Important Metrics

### Average Order Value

The dashboard calculates the mean AOV across the filtered restaurant population:

```python
avg_aov = df_filtered["AOV"].mean()
```

### In-Store Market Share

Channel market share is calculated using the filtered dataset:

```python
shares = calculate_channel_market_share(df_filtered)
```

### Aggregator Dependency

The project uses an `AggregatorDependence` measure to classify businesses into dependency categories.

### Diversification Score

A `DiversificationScore` is calculated for each restaurant and displayed as a distribution to understand channel-mix concentration.

---

## Validation

Before analytics are performed, the dataset passes through validation functions:

```python
df = validate_order_totals(df)
df = validate_channel_share(df)
```

This ensures that the dashboard's downstream calculations are based on validated order-channel data.

---

## Installation & Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/aswinajimon57-ux/aswinajimon57-ux.git
cd aswinajimon57-ux
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Deployment

The application is deployed using **Streamlit Community Cloud**.

For deployment:

1. Push the project to GitHub.
2. Select the repository and `main` branch.
3. Set the main file to:

```text
app.py
```

4. Use Python 3.12.
5. Streamlit installs dependencies from `requirements.txt`.

---

## Example Business Questions Answered

The dashboard can be used to answer questions such as:

- What percentage of orders come from in-store sales?
- How large is the delivery channel relative to in-store ordering?
- Which ordering channel contributes the most net profit?
- How dependent are restaurants on third-party aggregators?
- How diversified is the ordering-channel mix?
- How do these metrics change by subregion, cuisine, or business segment?

---

## What I Learned

This project helped strengthen practical experience in:

- Exploratory and business-focused data analysis
- Data validation
- KPI design
- Feature engineering
- Interactive dashboard development
- Data visualization
- Modular Python project structure
- Streamlit deployment
- Translating analytical results into executive-level insights

---

## Future Improvements

Potential extensions include:

- Time-series trend analysis
- Restaurant-level drill-down pages
- Geographic visualization
- Predictive order-volume forecasting
- Customer segmentation
- Profit-margin analysis by restaurant
- Downloadable executive reports
- Automated anomaly detection
- More granular commission and delivery-cost analysis

---

## Disclaimer

This project is intended as a portfolio/business analytics demonstration. The risk thresholds and strategic messages are analytical assumptions defined within the project and are not official SkyCity policies or industry standards.

---

## Author

**Aswin A.**

Data Analytics | Machine Learning | Python

GitHub: `https://github.com/aswinajimon57-ux`

