# Consumer-Behavior-GA4-Analysis
This project presents an applied consumer behaviour and marketing analytics study using a GA4-style e-commerce dataset. The analysis focuses on conversion performance, purchase funnel dynamics, and revenue generation across traffic sources and devices.

## Objectives
- Analyze conversion rates by traffic source and device
- Examine customer drop-off across the purchase funnel
- Evaluate revenue per session to support marketing decision-making

## Data
The dataset follows a Google Analytics 4 (GA4)-style structure and includes:
- Session-level data (traffic source, device, country, date)
- Event-level data (view_item, add_to_cart, begin_checkout, purchase)
- Transaction-level revenue data

## Methodology
- Data integration and preprocessing using Python (pandas)
- Calculation of key marketing KPIs:
  - Conversion Rate
  - Funnel Step Conversion
  - Revenue per Session
- Visualization using matplotlib

## Key Insights
- Paid and Social channels demonstrate higher conversion rates and revenue per session
- Desktop and mobile users exhibit comparable conversion performance, with a trade-off between conversion frequency and transaction value
- Funnel analysis indicates a healthy purchase journey with no critical bottlenecks

## Project Structure
```
├── analysis.py
├── requirements.txt
├── README.md
├── data/
│   ├── sessions.csv
│   ├── events.csv
│   └── transactions.csv
└── figures/
    ├── conversion_rate_by_traffic_source.png
    ├── conversion_rate_by_device.png
    ├── revenue_per_session_by_traffic_source.png
    └── revenue_per_session_by_device.png

## Tools
- Python
- pandas
- matplotlib

## Author
Parnia Riazat
