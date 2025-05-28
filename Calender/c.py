import datetime
from datetime import date, time
import calendar

# Using calendar
print("Calendar module:")
print([calendar.month_name[i] for i in range(1, 13)])

# Using datetime
print("Datetime module:")
print([datetime.date(2023, i, 1).strftime("%B") for i in range(1, 13)])

# Using date and time
print("Date and Time:")
print([date(2023, i, 1).strftime("%B") for i in range(1, 13)])
