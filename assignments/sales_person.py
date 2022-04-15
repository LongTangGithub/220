"""
Name: Long Tang
hw11.py
Problem: Develop programs utilizing between objects and lists
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.name = name
        self.id = employee_id
        self.sales = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for sale in self.sales:
            total += sale
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return self.total_sales() >= quota

    def compare_to(self, other):
        if self.total_sales() < other.total_sales():
            return -1
        elif self.total_sales() > other.total_sales():
            return 1
        else:
            return 0

    def __str__(self):
        return "" + str(self.get_id()) + "-" + self.get_name() + ": " + str(self.total_sales())


if __name__ == "__main__":
    pass
