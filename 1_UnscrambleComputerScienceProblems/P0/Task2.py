"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the
phone during September 2016.".
"""

# Dictionary to keep track of all calls
calls_dict = {}  # O(1)

for caller, reciever, timestamp, duration in calls:  # O(n)
    # Calling telephone
    if caller not in calls_dict:  # O(1)
        calls_dict[caller] = int(duration)  # O(1)
    else:
        calls_dict[caller] += int(duration)  # O(1)

    # Receiver telephone
    if reciever not in calls_dict:  # O(1)
        calls_dict[reciever] = int(duration)  # O(1)
    else:
        calls_dict[reciever] += int(duration)  # O(1)

phone, time = (max(calls_dict.items(), key=lambda x: x[1]))  # O(n)
print('%s spent the longest time, %s seconds, on the phone during'
      ' September 2016.' % (phone, time))
