"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

s = set()

# O(n)
for text in texts:
    s.add(text[0])
    s.add(text[1])

# O(n)
for call in calls:
    s.add(call[0])
    s.add(call[1])

print('There are %s different telephone numbers in the records.' % len(s))
