"""
    Name: Esrah
    Surname: Zahid
    Student ID: S020289
    IE 246 HW-3 Problem-3 a, b, c
"""

class Student:
    def __init__(self, name, id_number, gpa=0):
        self.name = name
        self.id_number = id_number
        self.gpa = gpa

    def set_gpa(self, new_gpa):
        self.gpa = new_gpa


class ForeignStudent(Student):
    def __init__(self, name, id_number, nationality, gpa=0):
        super().__init__(name, id_number, gpa)
        self.nationality = nationality


class Club:
    def __init__(self, *args):
        self.members = [student for student in args]

    def add_member(self, new_member):
        self.members.append(new_member)

    def display_members(self):
        for member in self.members:
            print(member.name)

    def get_size(self):
        return len(self.members)

print('\nAnswer (3 a) '+'#'*30)

s1 = Student("Ali Atay", "S011122")
print(s1.name)
print(s1.id_number)
print(s1.gpa)
s1.set_gpa(3.56)
print(s1.gpa)

print('\nAnswer (3 b) '+'#'*30)

s2 = ForeignStudent("Gerard Depardieu", "S012345", "France")
print(s2.name)
print(s2.id_number)
print(s2.gpa)
print(s2.nationality)
s2.set_gpa(2.44)
print(s2.gpa)

print('\nAnswer (3 c) '+'#'*30)
s1 = Student("Ali Atay", "S011122", 3.56)
s2 = ForeignStudent("Gerard Depardieu", "S012345", "France", 2.44)
ozuor = Club(s1, s2)
ozuor.display_members()
print(ozuor.get_size())
ozuor.add_member(ForeignStudent("Brad Pitt", "S054321", "US", 1.98))
ozuor.display_members()
size = ozuor.get_size()
print(size)
print(ozuor.members[0].gpa)
print(ozuor.members[1].gpa)
print(ozuor.members[2].gpa)
