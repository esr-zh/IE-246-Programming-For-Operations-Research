'''

IE 246 Homework - 2 Question - 3-A Solutions by Esrah Zahid (S020289)

'''


def hist(*args):
    frequency = {}
    for num in args:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Print the histogram
    for num in sorted(frequency.keys()):
        print(f"{num} : {'*' * frequency[num]}")

hist(3, 4, 3, 2, 4, 4, 3, 4, 1, 2, 3, 4, 5, 7, 5)
