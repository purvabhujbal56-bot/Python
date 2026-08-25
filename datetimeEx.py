from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

# 1. Current Date
today = date.today()
print("1. Current Date:", today)

# 2. Current Time
now = datetime.now()
print("2. Current Time:", now.strftime("%H:%M:%S"))

# 3. Current Date and Time
print("3. Current Date & Time:", now)

# 4. Current Year
print("4. Current Year:", today.year)

# 5. Current Month
print("5. Current Month:", today.month)

# 6. Current Day
print("6. Current Day:", today.day)

# 7. Add 10 days
print("7. Date after 10 days:", today + timedelta(days=10))

# 8. Subtract 10 days
print("8. Date before 10 days:", today - timedelta(days=10))

# 9. Difference between dates
date1 = date(2026, 8, 1)
date2 = date(2026, 8, 12)
print("9. Difference:", (date2 - date1).days, "days")

# 10. India Location and Time
india_time = datetime.now(ZoneInfo("Asia/Kolkata"))
print("10. Location: India")
print("    India Time:", india_time.strftime("%H:%M:%S"))