'''

IE 246 Homework - 2 Question - 2-B Solutions by Esrah Zahid (S020289)

'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def euler(min_inc=1e-12):
    e_approx, i = 0, 0
    while True:
        increment = 1 / factorial(i)
        if increment < min_inc:
            return e_approx
        e_approx += increment
        i += 1

def guess_ln(x, max_err=0.00001):
    e_approx = euler()
    while True:
        guess = float(input(f"Make a guess for ln({x}): "))
        exp_guess = e_approx ** guess
        error = abs(x - exp_guess)

        if error <= max_err:
            print("Your guess is acceptable.")
            return guess
        elif exp_guess < x:
            print("You have underestimated.")
        else:
            print("You have overestimated.")

y = guess_ln(5)
print(y)
