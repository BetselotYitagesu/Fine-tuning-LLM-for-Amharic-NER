# ------------------------
# src/vendor_scorecard.py
# ------------------------
import json
import pandas as pd
from datetime import datetime

# Load vendor Telegram data (example structure)
with open("../vendor_data.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

# Group posts by vendor 
vendor_stats = {}
for post in posts:
    vendor = post["vendor"]
    date = datetime.fromisoformat(post["timestamp"])
    week_key = f"{date.year}-W{date.isocalendar().week}"
    
    if vendor not in vendor_stats:
        vendor_stats[vendor] = {"weeks": set(), "views": [], "prices": []}

    vendor_stats[vendor]["weeks"].add(week_key)
    vendor_stats[vendor]["views"].append(post.get("views", 0))
    vendor_stats[vendor]["prices"].append(post.get("price", 0))

# Calculate metrics
score_data = []
for vendor, stats in vendor_stats.items():
    posts_per_week = len(stats["views"]) / len(stats["weeks"])
    avg_views = sum(stats["views"]) / len(stats["views"])
    avg_price = sum(stats["prices"]) / len(stats["prices"])
    lending_score = (avg_views * 0.5) + (posts_per_week * 0.5)

    score_data.append({
        "Vendor": vendor,
        "Posts/Week": round(posts_per_week, 2),
        "Avg. Views/Post": round(avg_views, 2),
        "Avg. Price (ETB)": round(avg_price, 2),
        "Lending Score": round(lending_score, 2),
    })

# Save scorecard
score_df = pd.DataFrame(score_data)
score_df.to_csv("../vendor_scorecard.csv", index=False)
print("Vendor scorecard saved to vendor_scorecard.csv")

