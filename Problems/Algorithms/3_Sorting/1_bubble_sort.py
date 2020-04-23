"""
Bubble Sort Exercises:
Now that you know how bubble sort works, you'll implement bubble sort
for two exercises.

Exercise 1:
Sam records when they wake up every morning. Assuming Sam always wakes up in
the same hour, use bubble sort to sort by earliest to latest.

Exercise 2:
Sam doesn't always go to sleep in the same hour. Given the following times Sam
has gone to sleep, sort the times from latest to earliest.

Complexity analysis:
Time complexity: O(n^2)
Space complexity: O(n)
"""


def bubble_sort_1(l):
    for i in range(len(l)):
        for j in range(1, len(l)):
            # Compare current and previous elements
            current = l[j]
            previous = l[j-1]

            # If previous element is less than current, then continue
            if previous <= current:
                continue
            else:
                # Else, swap current and previous elements in the array
                l[j] = previous
                l[j-1] = current
    return l


def bubble_sort_2(l):
    for i in range(len(l)):
        for j in range(1, len(l)):
            curr_hour, curr_min = l[j]
            prev_hour, prev_min = l[j-1]

            if prev_hour > curr_hour or (prev_hour == curr_hour
                                         and prev_min > curr_min):
                continue
            else:
                l[j] = (prev_hour, prev_min)
                l[j-1] = (curr_hour, curr_min)
    return l


# Tests
wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22,
                13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]
bubble_sort_1(wakeup_times)
print("Pass" if (wakeup_times[0] == 3) else "Fail")

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20),
               (22, 5), (24, 23), (21, 58), (24, 3)]
bubble_sort_2(sleep_times)
print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20),
                                 (22, 5), (21, 58), (21, 55)]) else "Fail")
