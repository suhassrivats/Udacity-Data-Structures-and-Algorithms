"""
Problem Statement:
Given arrival and departure times of trains on a single day in a railway
platform, find out the minimum number of platforms required so that no train
has to wait for the other(s) to leave.

You will be given arrival and departure times in the form of a list.

Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be
written as 930. Similarly, 13:45 would be given as 1345
"""


def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms
    (int) required
    so that no train has to wait for other(s) to leave
    """

    # Sort both arrival and departure arrays
    arrival.sort()
    departure.sort()

    platforms = 1
    result = 1
    i = 1
    j = 0

    while i < len(arrival) and j < len(arrival):

        # Check if next element in sorted order is arrival, then increment
        # number of platforms needed
        if arrival[i] < departure[j]:
            platforms += 1
            i += 1

            if platforms > result:
                result = platforms

        # If departure, decrement by 1
        else:
            platforms -= 1
            j += 1

    print(result)
    return result


# Tests
def test_function(testcase):
    arrival = testcase[0]
    departure = testcase[1]
    solution = testcase[2]
    output = min_platforms(arrival, departure)
    if output == solution:
        print('Pass')
    else:
        print('Fail')


arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
testcase = [arrival, departure, 3]
test_function(testcase)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)