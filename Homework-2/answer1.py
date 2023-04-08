'''

IE 246 Homework - 2 Question - 1 Solutions by Esrah Zahid (S020289)

'''

def summary(lst):
    minimum = min(lst)
    mean = sum(lst) / len(lst)
    variance = sum([(x - mean)**2 for x in lst]) / (len(lst) - 1)
    stddev = variance**(1/2)
    n = len(lst)
    sorted_lst = sorted(lst)
    median = (sorted_lst[(n-1)//2] + sorted_lst[n//2]) / 2
    maximum = max(lst)
    statistics = {'min': minimum, 'mean': mean, 'median': median, 'var': variance, 'stddev': stddev, 'max': maximum}
    return statistics

lst1 = [1,4,3,2,5]
lst2 = [1,4,3,2,5,6]
print(summary(lst1))
print(summary(lst2))
