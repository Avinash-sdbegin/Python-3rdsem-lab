from datetime import datetime

def get_day_of_week(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%A")
    except ValueError:
        return "Invalid date format! Use YYYY-MM-DD."

# Test the function
dates = ["2025-11-12", "2000-01-01", "2024-02-29", "2023-06-18"]
for d in dates:
    print(f"{d} ➜ {get_day_of_week(d)}")
