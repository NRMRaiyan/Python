#(A) Student Results
class Student:
    def __init__(self, name, student_id, marks):
        # Validate marks before storing the student data
        if not isinstance(marks, (int, float)) or isinstance(marks, bool):
            raise ValueError("Marks must be numeric")

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")

        self.name = name
        self.student_id = student_id
        self.marks = marks

    def get_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"ID: {self.student_id}, "
            f"Marks: {self.marks}, "
            f"Grade: {self.get_grade()}"
        )


# Testing the Student class
student1 = Student("Rafi", "101", 85)
student2 = Student("Nila", "102", 47)

print(student1)
print(student2)


#(B) Student Wallet - Bank Account
class BankAccount:

    # Class variable
    bank_name = "Campus Bank"

    def __init__(self, account_holder, opening_balance):

        if (not isinstance(opening_balance, (int, float))
                or isinstance(opening_balance, bool)):
            raise ValueError("Opening balance must be numeric")

        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")

        self.account_holder = account_holder
        self._balance = opening_balance

    def deposit(self, amount):

        if (not isinstance(amount, (int, float))
                or isinstance(amount, bool)):
            raise ValueError("Deposit amount must be numeric")

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount

    def withdraw(self, amount):

        if (not isinstance(amount, (int, float))
                or isinstance(amount, bool)):
            raise ValueError("Withdrawal amount must be numeric")

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount

    def show_balance(self):
        return self._balance


# Testing the BankAccount class

account = BankAccount("Rafi", 1000)

print("Bank:", BankAccount.bank_name)
print("Account Holder:", account.account_holder)

account.deposit(500)
account.withdraw(300)

print("Final Balance:", account.show_balance())

#(C) Staff Hierarchy
class Employee:
    def __init__(self, name, base_salary):
        if (not isinstance(base_salary, (int, float))
                or isinstance(base_salary, bool)):
            raise ValueError("Base salary must be numeric")

        if base_salary < 0:
            raise ValueError("Base salary cannot be negative")

        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def summary(self):
        return (
            f"Name: {self.name}, "
            f"Role: {self.__class__.__name__}, "
            f"Salary: {self.calculate_salary()}"
        )


# Child class: Developer
# Inheritance: Developer inherits from Employee
class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        if (not isinstance(bonus, (int, float))
                or isinstance(bonus, bool)):
            raise ValueError("Bonus must be numeric")

        if bonus < 0:
            raise ValueError("Bonus cannot be negative")

        super().__init__(name, base_salary)
        self.bonus = bonus

    # Method overriding
    def calculate_salary(self):
        return self.base_salary + self.bonus


# Child class: Manager
# Inheritance: Manager inherits from Employee
class Manager(Employee):
    def __init__(self, name, base_salary, allowance):
        if (not isinstance(allowance, (int, float))
                or isinstance(allowance, bool)):
            raise ValueError("Allowance must be numeric")

        if allowance < 0:
            raise ValueError("Allowance cannot be negative")

        super().__init__(name, base_salary)
        self.allowance = allowance

    # Method overriding
    def calculate_salary(self):
        return self.base_salary + self.allowance


# Driver code for Part (C)

employee1 = Employee("Rafi", 25000)
employee2 = Developer("Nila", 30000, 5000)
employee3 = Manager("Karim", 40000, 10000)

# Polymorphism: different employee objects in one list
employees = [employee1, employee2, employee3]

for employee in employees:
    print(employee.summary())