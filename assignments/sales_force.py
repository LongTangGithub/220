"""
Name: Long Tang
hw11.py
Problem: Develop programs utilizing between objects and lists
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from hw11.sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        f_name = open(file_name, "r")
        lists = f_name.readlines()
        for line in lists:
            self.sales_people.append(line.replace("\n", "").split(","))

    def quota_report(self, quota):
        list = []

        for sales in self.sales_people:
            emp = SalesPerson(sales[0], sales[1])
            n_sale = str(sales[2])
            sale_list = n_sale.strip().split(" ")

            for i in sale_list:
                emp.enter_sale(float(i))

            sale_list = [sales[0], sales[1], emp.total_sales(), emp.met_quota(quota)]
            list.append(sale_list)

        return list

    def top_seller(self):
        final_list = []
        max_sell = 0
        emp = []
        j = 0
        for sales in self.sales_people:

            emp.append(SalesPerson(sales[0], sales[1]))
            n_sale = str(sales[2])
            sale_list = n_sale.strip().split(" ")

            for i in sale_list:
                emp[j].enter_sale(float(i))
            j += 1

        for top_seller in emp:
            if max_sell < top_seller.total_sales():
                max_sell = top_seller.total_sales()

        for seller in emp:
            if seller.total_sales() == max_sell:
                final_list.append(seller)

        return final_list

    def individual_sales(self, employee_id):
        emp = []
        j = 0

        for sales in self.sales_people:
            emp.append(SalesPerson(sales[0], sales[1]))
            n_sale = str(sales[2])
            sale_list = n_sale.strip().split(" ")

            for i in sale_list:
                emp[j].enter_sale(float(i))
            j += 1

        for person in emp:
            if employee_id == person.get_id():
                return person
            else:
                return None

    def get_sale_frequencies(self):
        emp = []
        j = 0
        Dict = {}

        for sales in self.sales_people:
            emp.append(SalesPerson(sales[0], sales[1]))
            n_sale = str(sales[2])
            sale_list = n_sale.strip().split(" ")

            for i in sale_list:
                emp[j].enter_sale(float(i))
            j += 1

        for sells in emp:
            cnt = 0
            for i in range(len(emp)):
                if sells.total_sales() == emp[i].total_sales():
                    cnt += 1
            Dict[sells] = cnt

        return Dict


if __name__ == '__main__':
    pass
