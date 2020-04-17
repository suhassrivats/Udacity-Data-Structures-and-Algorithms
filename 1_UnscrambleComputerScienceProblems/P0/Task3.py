"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order
with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

###################### Part A ######################

# This list will contain all the calls from Bangaloreans
blr_calls = [call for call in calls if call[0].startswith('(080)')]  # O(n)

# This list will contain all calls to a certain area code by Bangaloreans
blr_dialed = [call[1] for call in blr_calls]  # O(n)

# This list will contain all area-codes dialed by Bangaloreans
blr_dialed_areas = set()  # O(1)

# Total time complexity including for loop and sort: O(n*m^2 + nlogn)
for call in blr_dialed:  # O(n)

    # Total time complexity inside for loop: O(m^2 + m) = O(m^2)

    # Fixed lines with enclosed brackets
    # The if block would take, O(m^2) time complexity. Since, phone m is a
    # constant (lenth of a phone number is 10-13 digits). Time complexity of
    # if block is O(1).

    if re.search(r'\(\w+\)', call):  # O(m)
        area_code = re.search(r'(\(.*?\))', call).group()  # O(m)
        blr_dialed_areas.add(area_code)  # O(1)

    # Moblie numbers starting with 7,8 or 9
    # The elif block takes O(m) time complexity

    elif re.search(r'(^[7|8|9])', call):  # O(m)
        area_code = call[:4]  # O(1)
        blr_dialed_areas.add(area_code)  # O(1)

print("The numbers called by people in Bangalore have codes:")

# O(nlogn) - Sort; O(n) - loop
for blr_dialed_area in sorted(list(blr_dialed_areas)):
    print(blr_dialed_area)

###################### Part B ######################

# List contains all calls made by Bangaloreans to Bangaloreans - O(n)
blr_dialed_blr = [call for call in blr_dialed if call.startswith('(080)')]
percentage = round((len(blr_dialed_blr)/len(blr_dialed) * 100), 2) # O(1)

print('%s percent of calls from fixed lines in Bangalore are calls '
      'to other fixed lines in Bangalore.' % percentage)
