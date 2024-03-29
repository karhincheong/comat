# Given a number n and an array with n elements, return the minimum value in the array
def min_from_array(n, arr):
    min_value = arr[0]
    for i in range(1, n):
        if arr[i] < min_value:
            min_value = arr[i]
    return min_value


# Given a number n and an array with n elements, return the maximum value in the array
def max_from_array(arr):
    n = len(arr)
    max_value = arr[0]
    for i in range(1, n):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value


# Given a number n and an array with n elements, return the mean of the numbers


def mean_from_array(arr):
    sum_ = 0
    for i in range(0, len(arr)):
        sum_ += arr[i]
    return round(sum_ / len(arr), 3)


# Given a number n and an array with n elements, return the mode of the numbers
def mode_from_array(arr):
    n = len(arr)
    mode = arr[0]
    count = 0
    for i in range(1, n):
        if arr[i] == mode:
            count += 1
        elif arr[i] > mode:
            mode = arr[i]
            count = 1
    return mode


# Given a number n and an array with n elements, return the median of the numbers
def median_from_array(arr):
    n = len(arr)
    arr.sort()
    if n % 2 == 0:
        return (arr[n // 2] + arr[n // 2 - 1]) / 2
    else:
        return arr[n // 2]


# Given a number n and an array with n numerical elements, return the range of the numbers
def range(arr):
    return max_from_array(arr) - min_from_array(arr)


# Given a number n and an array with n numerical elements, return the standard deviation of the numbers
def standard_deviation(arr):
    n = len(arr)
    for element in arr:
        if type(element) != int or type(element) != float:
            return None
    mean = mean_from_array(arr)
    sum_ = 0
    for i in range(0, n):
        sum_ += (arr[i] - mean) ** 2
    return (sum_ / n) ** 0.5


# Given a number n and an array with n numerical elements, return the variance of the numbers
def variance(arr):
    n = len(arr)
    for element in arr:
        if type(element) != int or type(element) != float:
            return None
    mean = mean_from_array(arr)
    sum_ = 0
    for i in range(0, n):
        sum_ += (arr[i] - mean) ** 2
    return sum_ / n
