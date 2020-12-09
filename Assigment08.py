# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Stephanie Tarczynski,12.8.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Stephanie Tarczynski,12.8.2020,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, product_name = "", product_price= 0.0):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    # Product Name
    @property
    def product_name(self):  # getter
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, name):
        if str(value).isnumeric() == False:
            self.__first_name = name
        else:
            raise Exception("Names cannot be numbers")

    # Product Price
    @property
    def product_price(self):  # getter or acessor
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, price):
        if str(value).isnumeric() == True:
            self.__first_name = price
        else:
            raise Exception("The value should be a number")

    # -- Methods --
    def __str__(self):
        return self.product_name + ', ' + self.product_price
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    pass

    # TODO: Add Code to process data from a file
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :rtype: object
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        try:
            file_name = open(file_name, "x")
            file_name.close()
        except FileExistsError:
            pass

        file = open(file_name, "r")
        for line in file:
            product_name, product_price = line.split(",")
            row = Product(product_name, product_price)
            list_of_rows.append(row)
        file.close()
        return list_of_rows


    # TODO: Add Code to process data to a file
    def write_data_to_file(file_name, list_of_rows):
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row.product_name + "," + row.product_price + "\n")
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(name, price, list_of_rows):
        row = Product(name, price)
        list_of_rows.append(row)
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Processes inputs and outputs from the user to a file

    methods:
        print_menu_Tasks()
        input_menu_choice()
        print_current_Data_in_list(list_of_rows)
        input_new_product_and_price()
    changelog: (When,Who,What)
    RRoot,1.1.2030,Created Class
    Stephanie Tarczynski,12.8.2020,Modified code to complete assignment 8
            """
    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Show Current Data
            2) Add data
            3) Save Data to File        
            ''')
        print()  # Add an extra line for looks
    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice
    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_Data_in_list(list_of_rows):
        data = FileProcessor.read_data_from_file(strFileName, list_of_rows)
        return data
    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_and_price():
        product = input("Enter the product: ")
        price = input("Enter the price: ")
        return product, price

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# Load data from file into a list of product objects when script starts

lstOfProductObjects = FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

while (True):
# Show user a menu of options
    IO.print_menu_Tasks()
# Get user's menu option choice
    choice = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if choice.strip() == '1':
        for row in lstOfProductObjects:
            print(row)
        continue
    # Let user add data to the list of product objects
    elif choice.strip() == '2':
        product, price = IO.input_new_product_and_price()
        lstOfProductObjects = FileProcessor.add_data_to_list(product, price, lstOfProductObjects)
        continue
    # let user save current data to file and exit program
    elif choice.strip() == '3':
        lstOfProductObjects = FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
        input("List saved. Press enter to exit.")
        break  # exit
    else:
        print("Invalid Option")
