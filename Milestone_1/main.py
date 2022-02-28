# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

my_student_dict = {
    "name": "Arjun",
    "scores": [70, 88, 90, 99]
}

avg = (lambda x: sum(x) / len(x))

print(avg(my_student_dict["scores"]))


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def avegrage(self):
        avg = lambda x: sum(x) / len(x)
        return avg(self.scores)

    @staticmethod
    def sum(scores):
        return sum(scores)

    @classmethod
    def participation(cls, game):
        return f"Student is {cls.__name__} and he plays {game}"

    def __len__(self):
        return len(self.scores)

    def __getitem__(self, i):
        return self.scores[i]

    def __repr__(self):
        return f"<Student {self.scores}>"

    # def __str__(self):
    #     return f"Student {self.name} has {self.avegrage()} Average Scores"


class WorkingStudent(Student):
    def __init__(self,name, scores, salary):
        super().__init__(name,scores)
        self.salary = salary


stud_obj = Student("Lx", [30, 29, 45, 36, 30])
print(stud_obj.avegrage())
print(stud_obj)
print("Length : ", len(stud_obj))

workin_stud = WorkingStudent("AJ", [76, 95, 78, 77, 89], 15000)
for i in stud_obj:
    print(i)

print(stud_obj.sum([21, 23, 54, 23, 12]))
print(stud_obj.participation("Socer"))
print(workin_stud.participation("Hockey"))

print("__ 1 and 2 are prime numbers don't need to check __")
prime_numbers = [1,2]
noe = 10
cnt = 0
for i in range(3, noe * 2, 2):
    for j in range(3, i, 2):
        cnt += 1
        if i % j == 0:
            continue
    # print(i, end=', ')
    prime_numbers.append(i)
    if len(prime_numbers) >= noe:
        break
print(len(prime_numbers))
print(prime_numbers)
print("Line Executed Time : ", cnt)