"""
Caching can be defined as the process of storing data into a temporary data
storage to avoid recomputation or to avoid reading the data from a relatively
slower part of memory again and again. Thus cachig serves as a fast "look-up"
storage allowing programs to execute faster.

Let's use caching to chalk out an efficient solution for a problem.

Problem Statement
A child is running up a staircase with and can hop either 1 step, 2 steps or
3 steps at a time. If the staircase has n steps, write a function to count the
number of possible ways in which child can run up the stairs.

For e.g.
n == 1 then answer = 1
n == 3 then answer = 4
n == 5 then answer = 13
"""


def staircase(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase(n-1) + staircase(n-2) + staircase(n-3)


"""
While using recursion for the above problem, you might have noticed a small
problem with efficiency.

Let's take a look at an example.

Say the total number of steps are 5. This means that we will have to call at
(n=4), (n=3), and (n=2)

To calculate the answer for n=4, we would have to call (n=3), (n=2) and (n=1)

You can notice that even for a small number of staircases (here 5), we are
calling n=3 and n=2 multiple times. Each time we call a method, additional
time is required to calculate the solution. In contrast, instead of calling
on a particular value of n again and again, we can calculate it once and store
the result to speed up our program.

Your job is to use any data-structure that you have used until now to write a
faster implementation of the function you wrote earlier while using recursion.
"""


def staircase_cache(n):
    num_dict = dict({})

    return staircase_cache_helper(n, num_dict)


def staircase_cache_helper(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n-1) in num_dict:
            first_output = num_dict[n-1]
        else:
            first_output = staircase_cache_helper(n-1, num_dict)

        if (n-2) in num_dict:
            second_output = num_dict[n-2]
        else:
            second_output = staircase_cache_helper(n-2, num_dict)

        if (n-3) in num_dict:
            third_output = num_dict[n-3]
        else:
            third_output = staircase_cache_helper(n-3, num_dict)

        output = first_output + second_output + third_output

    num_dict[n] = output
    return output


# Tests
def test_function(test_case):
    answer = staircase_cache(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case = [4, 7]
test_function(test_case)

test_case = [5, 13]
test_function(test_case)

test_case = [3, 4]
test_function(test_case)

test_case = [20, 121415]
test_function(test_case)
