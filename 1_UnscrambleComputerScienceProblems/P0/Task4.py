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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order
with no duplicates.
"""

outgoing_calls = set([call[0] for call in calls]) # O(n)
incoming_calls = set([call[1] for call in calls]) # O(n)

outgoing_texts = set([text[0] for text in texts]) # O(n)
incoming_texts = set([text[1] for text in texts]) # O(n)

possible_telemarketers = []

# Numbers that never send/receive texts and never receive incoming calls
for phone in outgoing_calls: # O(n)
    if (phone not in outgoing_texts) and (phone not in incoming_texts) and \
            (phone not in incoming_calls):
        possible_telemarketers.append(phone) # O(1)

print('These numbers could be telemarketers:')
for possible_telemarketer in sorted(possible_telemarketers): # O(n) + O(nlogn)
    print(possible_telemarketer)
