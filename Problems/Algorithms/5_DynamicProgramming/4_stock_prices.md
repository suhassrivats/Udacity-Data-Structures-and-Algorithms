
# Stock Prices

You are given access to yesterday's stock prices for a single stock. The data is in the form of an array with the stock price in 30 minute intervals from 9:30 a.m EST opening to 4:00 p.m EST closing time. With this data, write a function that returns the maximum profit obtainable. You will need to buy before you can sell.

For example, suppose you have the following prices:

`prices = [3, 4, 7, 8, 6]`

>Note: This is a shortened array, just for the sake of example—a full set of prices for the day would have 13 elements (one price for each 30 minute interval betwen 9:30 and 4:00), as seen in the test cases further down in this notebook.

In order to get the maximum profit in this example, you would want to buy at a price of 3 and sell at a price of 8 to yield a maximum profit of 5. In other words, you are looking for the greatest possible difference between two numbers in the array.

Fill out the function below and run it against the test cases. Take into consideration the time complexity of your solution. 


```python
def max_returns(prices):
    """
    Calculate maxiumum possible return
    
    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """
    
    return prices
```

<span class="graffiti-highlight graffiti-id_uc722im-id_o4cterg"><i></i><button>Hide Solution</button></span>


```python
# Solution

def max_returns(arr):
    """
    The idea is to pick two dates:
        1. buy date
        2. sell date
    We will keep track of our max profit while iterating over the list
    At each step we will make the greedy choice by choosing prices such that our profit is maximum 
    """
    min_price_index = 0
    max_price_index = 1
    current_min_price_index = 0
    
    if len(arr) < 2:
        return
    
    for index in range(1, len(arr)):
        # current minimum price
        if arr[index] < arr[current_min_price_index]:
            current_min_price_index = index
            
        # current max profit
        if arr[max_price_index] - arr[min_price_index] < arr[index] - arr[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index
    max_profit = arr[max_price_index] - arr[min_price_index]
    return max_profit
```


```python
# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
```


```python
prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)
```


```python
prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
test_function(test_case)
```


```python
prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
test_function(test_case)
```
