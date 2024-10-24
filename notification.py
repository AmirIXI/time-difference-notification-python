import datetime
from plyer import notification

# Target date (test date)
target_date = datetime.datetime(2023, 1, 1)

# Today's date
today = datetime.datetime.now()

# Calculate time difference
time_difference = today - target_date

notification.notify(
    title="Time Difference",
    message=f"Time difference: {time_difference.days} days",
    app_name="Time Notification",
    timeout=10  # Duration of notification in seconds
)
