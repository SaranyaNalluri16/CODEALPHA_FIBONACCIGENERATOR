def fibonacci(n):
    """
    Generate the Fibonacci series up to the nth number.
    Parameters:
    n (int): The length of the Fibonacci series to generate.
    Returns:
    list: A list containing the Fibonacci series.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    # Initialize the series with the first two numbers
    series = [0, 1]
    # Generate the rest of the series
    for i in range(2, n):
        next_number = series[-1] + series[-2]
        series.append(next_number)
    
    return series
# Example usage
n = int(input("Enter n value:"))  # Change this value to generate a different length of the series
fib_series = fibonacci(n)
print(f"Fibonacci series up to {n} numbers:.{fib_series}")
