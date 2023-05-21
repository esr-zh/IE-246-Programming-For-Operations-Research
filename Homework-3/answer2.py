"""
    Name: Esrah
    Surname: Zahid
    Student ID: S020289
    IE 246 HW-3 Problem-2 a, b, c
"""

class Vector():
    def __init__(self, num_list):
        self.content = num_list

    def get_norm(self):
        return (sum([i**2 for i in self.content]))**0.5

    def __add__(self, other):
        if len(self.content) != len(other.content):
            print("The lengths of vectors do not match!")
            return None
        return Vector([a + b for a, b in zip(self.content, other.content)])

    def __sub__(self, other):
        if len(self.content) != len(other.content):
            print("The lengths of vectors do not match!")
            return None
        return Vector([a - b for a, b in zip(self.content, other.content)])

    def __mul__(self, other):
        """Calculates the inner product of two vectors."""
        if len(self.content) != len(other.content):
            print("The lengths of vectors do not match!")
            return None
        return sum(a * b for a, b in zip(self.content, other.content))


print('\nAnswer (2 a) '+'#'*30)
x = Vector([3,5,2])
r0 = x.get_norm()
print(r0)
print(type(r0))

print('\nAnswer (2 b) '+'#'*30)
x = Vector([3, 5, 2])
y = Vector([7, 5, 8])
z = Vector([9, 1])

r1 = x + y
print(r1.content if r1 else None)
print(type(r1))

r2 = x - y
print(r2.content if r2 else None)
print(type(r2))

r3 = x + z
r4 = y - z

print('\nAnswer (2 c) '+'#'*30)
x = Vector([3, 5, 2])
y = Vector([7, 5, 8])
z = Vector([9, 1])

r1 = x * y
print(r1)

r2 = x * z
