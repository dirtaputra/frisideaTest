# Find Max Value
def findMax(list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max

# Find Min Value


def findMin(list):
    min = list[0]
    for num in list:
        if num < min:
            min = num
    return min

# Find Average value


def Average(list):
    return sum(list) / len(list)
