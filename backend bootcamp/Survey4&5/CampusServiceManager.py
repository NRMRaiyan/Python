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
