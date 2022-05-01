# Given a number n and an array with n elements, return the minimum value in the array
def min_from_array(n, arr):
    min_value = arr[0]
    for i in range(1, n):
        if arr[i] < min_value:
            min_value = arr[i]
    return min_value


# Given a number n and an array with n elements, return the maximum value in the array


def max_from_array(n, arr):
    max_value = arr[0]
    for i in range(1, n):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value


# Given a number n and an array with n elements, return the mean of the numbers


def mean_from_array(n, arr):
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    return sum / n


# Given a number n and an array with n elements, return the mode of the numbers


def mode_from_array(n, arr):
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


def median_from_array(n, arr):
    arr.sort()
    if n % 2 == 0:
        return (arr[n // 2] + arr[n // 2 - 1]) / 2
    else:
        return arr[n // 2]


# Given a number n and an array with n numerical elements, return the standard deviation of the numbers


def standard_deviation(n, arr):
    for element in arr:
        if type(element) != int or type(element) != float:
            return None
    mean = mean_from_array(n, arr)
    sum = 0
    for i in range(0, n):
        sum += (arr[i] - mean) ** 2
    return (sum / n) ** 0.5
