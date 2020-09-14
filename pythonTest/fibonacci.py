def fibonacciSeries(n):
    fibonacci_numbers = [0, 1]
    for i in range(len(fibonacci_numbers), n):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    return fibonacci_numbers
