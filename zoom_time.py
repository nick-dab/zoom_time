"""
doc: https://icalendar.readthedocs.io/en/latest/api.html?highlight=from_ical#module-icalendar.prop
"""
from icalendar import Calendar
import time
import re
import webbrowser


# Replace 'test.ics' with proper ics file containing start time and url link under location

# set current time via time module
time_now = time.strftime("%H:%M:%S")

# opening the file, returning it as file object
cal = open("test.ics")
ccal = Calendar.from_ical(cal.read())

for event in ccal.walk("vEvent"):
    class_start_datetime = event.get("dtstart").dt
    class_end_datetime = event.get("dtend").dt
    url = str(event["location"])

while time_now < str(class_end_datetime):
     print("Waiting until start time. Current time is:", time_now)
     print("Class starts at:", class_start_datetime, "\n")
     # updating time after each check
     time_now = time.strftime("%H:%M:%S")
     time.sleep(2)
     # first check seems to be the same as initial time, keeping sleep count low could help prevent lateness

# open extracted url
if time_now >= str(class_start_datetime):
     print("Class started - Opening now...")
     # web browser module to open url via default browser
     webbrowser.open(url)

