class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def get_info(self):
        return f"Full Name: {self.fname} {self.lname} \nAge: {self.age}"


class Student(Person):
    def __init__(self, fname, lname, age, student_id):
        super().__init__(fname, lname, age)
        self.student_id = student_id

    def get_stuinfo(self):
        return f"{self.get_info()},\nStudent ID: {self.student_id}"


class Employee(Person):
    def __init__(self, fname, lname, age, employee_number, salary):
        super().__init__(fname, lname, age)
        self.employee_number = employee_number
        self.salary = salary

    def get_empinfo(self):
        return f"{self.get_info()}, \nEmployee No: {self.employee_number}, \nSalary: {self.salary} USD"


new_student = Student("Anthony", "Smith", 35, "s346571")
print(new_student.get_stuinfo())
print("==========================")
new_employee = Employee("Sarah", "Taylor", 34, 2919736, 5000)
print(new_employee.get_empinfo())
