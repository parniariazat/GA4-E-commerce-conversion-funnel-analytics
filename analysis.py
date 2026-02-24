import pandas as pd
import matplotlib.pyplot as plt

# Load data
sessions = pd.read_csv("data/sessions.csv")
events = pd.read_csv("data/events.csv")
transactions = pd.read_csv("data/transactions.csv")

# --- Create purchase flag per session ---
purchase_sessions = (
    events[events["event_name"] == "purchase"]
    .groupby("session_id")["event_count"]
    .sum()
    .reset_index()
)

purchase_sessions["purchased"] = 1
purchase_sessions = purchase_sessions[["session_id", "purchased"]]

# --- Merge with sessions ---
df = sessions.merge(purchase_sessions, on="session_id", how="left")
df["purchased"] = df["purchased"].fillna(0)

# --- Merge revenue ---
df = df.merge(transactions, on="session_id", how="left")
df["revenue"] = df["revenue"].fillna(0)

print(df.head())



# Step 2: Conversion Rate Analysis

conversion_by_source = (
    df.groupby("traffic_source")
    .agg(
        sessions=("session_id", "count"),
        purchases=("purchased", "sum")
    )
)

conversion_by_source["conversion_rate"] = (
    conversion_by_source["purchases"] / conversion_by_source["sessions"]
)

print("\nConversion Rate by Traffic Source:")
print(conversion_by_source)




# Step 3: Conversion Rate Figure

conversion_by_source["conversion_rate"].plot(kind="bar")
plt.title("Conversion Rate by Traffic Source")
plt.ylabel("Conversion Rate")
plt.xlabel("Traffic Source")
plt.tight_layout()
plt.show()





# Step 4: Device

conversion_by_device = (
    df.groupby("device")
    .agg(
        sessions=("session_id", "count"),
        purchases=("purchased", "sum")
    )
)

conversion_by_device["conversion_rate"] = (
    conversion_by_device["purchases"] / conversion_by_device["sessions"]
)

print("\nConversion Rate by Device:")
print(conversion_by_device)

conversion_by_device["conversion_rate"].plot(kind="bar")
plt.title("Conversion Rate by Device")
plt.ylabel("Conversion Rate")
plt.xlabel("Device")
plt.tight_layout()
plt.show()





# Step 5: Funnel Analysis

funnel_steps = ["view_item", "add_to_cart", "begin_checkout", "purchase"]

funnel_counts = (
    events[events["event_name"].isin(funnel_steps)]
    .groupby("event_name")["event_count"]
    .sum()
    .reindex(funnel_steps)
)

print("\nFunnel Counts:")
print(funnel_counts)

# Conversion between steps
funnel_conversion = funnel_counts / funnel_counts.shift(1)
print("\nFunnel Step Conversion Rates:")
print(funnel_conversion)

funnel_conversion_clean = funnel_conversion.dropna()
print("\nFunnel Step Conversion Rates (Clean):")
print(funnel_conversion_clean)






# Step 6: Revenue Analysis by Traffic Source

revenue_by_source = (
    df.groupby("traffic_source")
    .agg(
        sessions=("session_id", "count"),
        total_revenue=("revenue", "sum")
    )
)

revenue_by_source["revenue_per_session"] = (
    revenue_by_source["total_revenue"] / revenue_by_source["sessions"]
)

print("\nRevenue by Traffic Source:")
print(revenue_by_source)


revenue_by_source["revenue_per_session"].plot(kind="bar")
plt.title("Revenue per Session by Traffic Source")
plt.ylabel("Revenue per Session")
plt.xlabel("Traffic Source")
plt.tight_layout()
plt.show()






# Step 7: Revenue Analysis by Device

revenue_by_device = (
    df.groupby("device")
    .agg(
        sessions=("session_id", "count"),
        total_revenue=("revenue", "sum")
    )
)

revenue_by_device["revenue_per_session"] = (
    revenue_by_device["total_revenue"] / revenue_by_device["sessions"]
)

print("\nRevenue by Device:")
print(revenue_by_device)


revenue_by_device["revenue_per_session"].plot(kind="bar")
plt.title("Revenue per Session by Device")
plt.ylabel("Revenue per Session")
plt.xlabel("Device")
plt.tight_layout()
plt.show()
