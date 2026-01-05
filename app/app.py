from flask import Flask, render_template

app = Flask(__name__)

# Dummy KPI data
kpi_data = [
    {"label": "Total Spend", "value": "RM 12,450"},
    {"label": "Total Leads", "value": "328"},
    {"label": "Avg CPL", "value": "RM 37.95"},
    {"label": "Conversions", "value": "96"},
]

# Dummy filters (not wired yet)
filter_options = {
    "date_range": ["Last 7 Days", "Last 30 Days", "Last 90 Days"],
    "platform": ["Meta", "Google"],
    "campaign": ["Foundation in Business", "Foundation in Science"],
}

# Dummy campaign table data
campaign_data = [
    {
        "campaign": "Foundation in Business",
        "platform": "Google",
        "spend": "RM 3,200",
        "leads": 82,
        "cpl": "RM 39.02",
    },
    {
        "campaign": "Foundation in Science",
        "platform": "Meta",
        "spend": "RM 2,100",
        "leads": 54,
        "cpl": "RM 38.89",
    },
]

# Dummy chart data
chart_data = {
    "labels": ["Week 1", "Week 2", "Week 3", "Week 4"],
    "spend": [2800, 3100, 2900, 3650],
    "leads": [72, 84, 76, 96],
    "cpl": [38, 37, 39, 36],
}

@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        kpis=kpi_data,
        filters=filter_options,
        campaigns=campaign_data,
        chart_data=chart_data,
    )


if __name__ == "__main__":
    app.run(debug=True)
