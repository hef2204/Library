from datetime import timedelta, datetime
import json
import string


class Customers:
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
    
    def __str__(self):
        return f"Customer: {self.name} ({self.age})"
    
    def update_address(self, new_address):
        self.address = new_address
        return True
    
    def update_email(self, new_email):
        self.email = new_email
        return True
    
    def get_details(self):
        return f"Customer: {self.name} ({self.age})\nAddress: {self.address}\nEmail: {self.email}"
    