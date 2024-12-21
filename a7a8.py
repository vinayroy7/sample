def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_series = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)

    return fibonacci_series


terms = int(input("Enter the number of terms: "))
fibonacci_series = generate_fibonacci(terms)

print(f"Fibonacci series up to {terms} terms: {fibonacci_series}")
