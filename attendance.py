import csv
import os
from datetime import datetime

# File to store attendance
ATTENDANCE_FILE = "attendance.csv"

# Function to mark attendance
def mark_attendance(name):
    # Check if attendance file exists
    file_exists = os.path.isfile(ATTENDANCE_FILE)

    with open(ATTENDANCE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        
        # Write header if file is new
        if not file_exists:
            writer.writerow(["Name", "Date", "Time"])
        
        # Get current time
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")

        # Write attendance entry
        writer.writerow([name, date, time])
        print(f"✅ {name} marked present at {time} on {date}.")
