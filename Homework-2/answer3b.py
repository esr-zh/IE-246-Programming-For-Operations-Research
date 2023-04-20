'''

IE 246 Homework - 2 Question - 3-B Solutions by Esrah Zahid (S020289)

'''
def count_sort(item):
    return -item[1], item[0]

def hist(*args):
    frequency = {}
    for num in args:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    sorted_items = sorted(frequency.items(), key=count_sort)
    for num, count in sorted_items:
        print(f"{num} : {'*' * count}")

hist(3, 4, 3, 2, 4, 4, 3, 4, 1, 2, 3, 4, 5, 7, 5)
