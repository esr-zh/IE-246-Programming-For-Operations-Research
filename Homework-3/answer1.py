"""
    Name: Esrah
    Surname: Zahid
    Student ID: S020289
    IE 246 HW-3 Problem-1
"""

def signum(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def create_sgn_file(filename):
    with open(filename, 'r') as datafile:
        lines = datafile.readlines()

    data = []
    for line in lines:
        row = []
        for cell in line.strip().split(","):
            row.append(signum(float(cell)))
        data.append(row)

    with open("data_sgn.csv", 'w') as sgnfile:
        for row in data:
            row_str = []
            for cell in row:
                row_str.append(str(cell))
            sgnfile.write(','.join(row_str))
            sgnfile.write('\n')

create_sgn_file("data.csv")
