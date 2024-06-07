class Student:
    passingMark = 50

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"Name: {self.name}, Mark: {self.mark}"

    def pass_or_fail(self):
        # Changed passOrFail to pass_or_fail since a name of a method should be lowercase
        if self.mark >= Student.passingMark:
            return "Pass"
        else:
            return "Fail"


student1 = Student('John', 52)
status1 = student1.pass_or_fail()

student2 = Student('Jenny', 69)
status2 = student2.pass_or_fail()

print(f"Student 1: {student1}, Status: {status1}")
print(f"Student 2: {student2}, Status: {status2}")

# Updated passingMark
Student.passingMark = 60

status1 = student1.pass_or_fail()
status2 = student2.pass_or_fail()
print("================================================")
print(f"Updated status for: {student1}: {status1}")
print(f"Updated status for: {student2}: {status2}")
