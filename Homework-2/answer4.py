'''

IE 246 Homework - 2 Question - 4 Solutions by Esrah Zahid (S020289)

'''
def pascal(row_number):
    if row_number == 1:
        result = [[1]]
    else:
        previous_row = pascal(row_number - 1)
        current_row = [1] + [previous_row[-1][i] + previous_row[-1][i + 1] for i in range(len(previous_row[-1]) - 1)] + [1]
        result = previous_row + [current_row]

    print(result[row_number-1])
    return result

result = pascal(12)
