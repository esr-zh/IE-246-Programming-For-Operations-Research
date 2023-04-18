'''

IE 246 Homework - 2 Question - 2 Solutions by Esrah Zahid (S020289)

'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def euler(min_inc=1e-12):
    e_approx, i, increment = 0, 0, 0
    while True:
        increment = 1 / factorial(i)
        if increment < min_inc:
            return e_approx
        e_approx += increment
        i += 1

# Example usage:
result = euler()
print(result)
