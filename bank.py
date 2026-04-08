import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'

    def __init__(self):
        if Path(self.database).exists():
            with open(self.database, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = []

    def save(self):
        with open(self.database, 'w') as f:
            json.dump(self.data, f, indent=4)

    def generate_account(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return "Invalid age or PIN"

        account = {
            "name": name,
            "age": age,
            "email": email,
            "Pin": int(pin),
            "accountNo": self.generate_account(),
            "Balance": 0
        }

        self.data.append(account)
        self.save()
        return account

    def find_user(self, acc, pin):
        for user in self.data:
            if user['accountNo'] == acc and user['Pin'] == int(pin):
                return user
        return None

    def deposit(self, acc, pin, amount):
        user = self.find_user(acc, pin)
        if not user:
            return "User not found"

        if amount <= 0 or amount > 10000:
            return "Invalid amount"

        user['Balance'] += amount
        self.save()
        return "Deposit successful"

    def withdraw(self, acc, pin, amount):
        user = self.find_user(acc, pin)
        if not user:
            return "User not found"

        if user['Balance'] < amount:
            return "Insufficient balance"

        user['Balance'] -= amount
        self.save()
        return "Withdrawal successful"

    def update_details(self, acc, pin, name, email, new_pin):
        user = self.find_user(acc, pin)
        if not user:
            return "User not found"

        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if new_pin:
            if len(str(new_pin)) == 4:
                user['Pin'] = int(new_pin)
            else:
                return "PIN must be 4 digits"

        self.save()
        return "Updated successfully"

    def delete_account(self, acc, pin):
        user = self.find_user(acc, pin)
        if not user:
            return "User not found"

        self.data.remove(user)
        self.save()
        return "Account deleted"