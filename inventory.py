import os
from tabulate import tabulate

#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return int(self.quantity)

    def get_code(self):
        return str(self.code).lower()

    def get_value(self):
        return int(self.cost) * int(self.quantity)

    def print_info(self):
        print(f"*" * 75)
        print(tabulate([[self.country, self.code, self.product, self.cost, self.quantity]], headers = ["Country", "Code", "Product", "Cost", "Quantity"]))

    def sale_info(self):
        print(f"*" * 75)
        print("SALE NOW ON")
        print(f"CODE: {self.code}")
        print(f"PRODUCT: {self.product}")
        print("WHILE STOCKS LAST")

    def __str__ (self):
        return (f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}")

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

def read_shoes_data():
    # Text file data structure as follows:
        # [0] = Country
        # [1] = Code 
        # [2] = Product 
        # [3] = Cost 
        # [4] = Quantity
    # Fist line as column headers, therefore needs to be removed/omitted

    try:
        shoe_list.clear()
        with open(os.path.join(os.path.dirname(__file__), "inventory.txt"), "r") as f:
            for line_number, line in enumerate(f, start=1):
                if line_number != 1:
                    line = line.strip() # .strip() removes the line break
                    line = line.split(",") # split() turns info into a list
                    temp_object = Shoe(line[0], line[1], line[2], line[3], line[4])
                    shoe_list.append(temp_object)

        return print("Shoes data retrieved from inventory.txt")

    except Exception as Arguement:
        print(f"An error occured:\n\t{Arguement}")

def capture_shoes():

    while True:
        try:
            temp_country = input("Enter the name of the country: ")
            temp_code = input("Enter the Product Code: ")
            temp_product = input("Enter the Product Name: ")
            temp_cost = int(input("Enter the Product Cost: "))
            temp_qauntity = int(input("Enter the Product Quantity: "))

            temp_line = f"\n{temp_country},{temp_code},{temp_product},{temp_cost},{temp_qauntity}"
            with open(os.path.join(os.path.dirname(__file__), "inventory.txt"), "a") as f:
                f.write(temp_line)
            
            temp_object = Shoe({temp_country}, {temp_code}, {temp_product}, {temp_cost}, {temp_qauntity})
            shoe_list.append(temp_object)     
        
            return print("Product Captured.")

        except ValueError:
            print(f"Use integers only when asked to enter a number")

        except Exception as Arguement:
            print(f"An error occured:\n\t{Arguement}")

def view_all():
    
    read_shoes_data()

    temp_list = []

    for shoe in shoe_list:
        temp_shoe = shoe.__str__()
        temp_shoe = temp_shoe.split(",")
        temp_list.append(temp_shoe)

    print(tabulate(temp_list, headers = ["Country", "Code", "Product", "Cost", "Quantity"]))
        

def re_stock():
    while True:
        try:

            read_shoes_data()

            # find the minimum stock value
            temp_quantities_list = []

            for shoe in shoe_list:
                temp_quantities_list.append(shoe.get_quantity())
            
            min_quantity = min(temp_quantities_list)

            # ask for user to provide updated stock numbers
            for shoe in shoe_list:
                if shoe.get_quantity() == min_quantity:
                    print(f"Shoe: {shoe.product}\t\tCurrent Stock: {shoe.quantity}")
                    shoe.quantity = int(input("Enter an updated stock count: "))
                    break

            # write data to the txt file
            with open(os.path.join(os.path.dirname(__file__), "inventory.txt"), "w") as f:
                
                f.write("Country,Code,Product,Cost,Quantity")
                for shoe in shoe_list:
                    f.write(f"\n{shoe.__str__()}")
            
            return

        except ValueError:
            print(f"Integers only for the quantity")
        except Exception as Arguement:
            print(f"An error occured:\n\t{Arguement}")

def search_shoe():
    
    while True:
        try:
            read_shoes_data()

            find_code = input("Enter the code you are looking for (-e to exit): ").lower()

            if find_code == "-e":
                break

            for shoe in shoe_list:
                if shoe.get_code() == find_code:
                    shoe.print_info()

        except Exception as Arguement:
            print(f"An error occured:\n\t{Arguement}")


def value_per_item():
    
    temp_list = []

    read_shoes_data()

    for shoe in shoe_list:
        temp_shoe = shoe.__str__()
        temp_shoe = temp_shoe.split(",")
        temp_shoe.append(f"{shoe.get_value():,}")
        temp_list.append(temp_shoe)

    print(tabulate(temp_list, headers = ["Country", "Code", "Product", "Cost", "Quantity", "Value"]))

def highest_qty():
    
    max_quantity = 0
    shoe_on_sale = ""

    read_shoes_data()

    for shoe in shoe_list:
        if shoe.get_quantity() > max_quantity:
            max_quantity = shoe.get_quantity()
            shoe_on_sale = shoe
    
    shoe_on_sale.sale_info()

    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============

while True:
    try:
        menu_option = input("The following options are available\n"
                            "\t\"add\" - add a product\n"
                            "\t\"view\" - view all product\n"
                            "\t\"update\" - update stock for a product\n"
                            "\t\"search\" - search for a specific product\n"
                            "\t\"value\" - view the value of all products\n"
                            "\t\"sale\" - view the sales promotions\n"
                            "\t\"exit\" - close program\n"
                            "Select your option: ").lower()

        match menu_option:
            case "add":
                capture_shoes()
            case "view":
                view_all()
            case "update":
                re_stock()
            case "search":
                search_shoe()
            case "value":
                value_per_item()
            case "sale":
                highest_qty()
            case "exit":
                print('Goodbye!!!')
                exit()                


    except Exception as Arguement:
            print(f"An error occured:\n\t{Arguement}")
    