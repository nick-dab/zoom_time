from icalendar import Calendar, Event
import time
import re
import webbrowser


"""
doc: https://icalendar.readthedocs.io/en/latest/api.html?highlight=from_ical#module-icalendar.prop
"""

# Replace 'test.ics' with proper ics file containing start time and url link under location

def rm_chars(c):
    return c.group(1)



time_now = time.strftime('%H:%M:%S') # set current time via time module
cal = open('test.ics') # opening the file, returning it as file object
ccal = Calendar.from_ical(cal.read())

# extract url
for components in ccal.walk(): # iterating through each of the components in the data within calendar
    if 'https' or 'http' in components: # doesn't work if i only put 'https', not sure why. needs 'http'
        try:
            url = (re.findall(r'(https?://[^\s]+)', str(components))[0]) # searching for any string containing the url
            break
        except Exception as IndexError: # exception throws for some reason but program still runs. this catches it
            result = ''
    else:
        print("No URL exists\n")

modurl = re.sub("(.*)(.{4}$)", rm_chars, url) # removing the extra 4 special characters at the end of the extracted url string
print('Found URL:', modurl) # printing url to confirm

# get start time
for dt in ccal.walk('vEvent'):
    class_start = dt.get('dtstart') # how do you realize you can use get here?
    end = dt.get('dtend')

    class_start2 = class_start.dt

str_time = str(class_start2) # convert start time into str
start_time = re.findall('(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)', str_time)[0] # get HH:MM:SS of start time via regex


while (time_now < start_time):
    print("Waiting until start time. Current time is:", time_now)
    print("Class starts at:", start_time, "\n")
    time_now = time.strftime('%H:%M:%S') # updating time after each check
    time.sleep(2) # first check seems to be the same as initial time, keeping sleep count low could help prevent lateness

# open extracted url
if (time_now >= start_time):
    print("Class started - Opening now...")
    webbrowser.open(modurl) # web browser module to open url via default browser



