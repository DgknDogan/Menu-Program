class Menu():
    def __init__(self):
        self.create_menu()

    """
    CREATE MENU METHOD
    ------------------
    In this section the program reads the 'menu.txt' file to reach the data.
    """
    def create_menu(self):
        self.category_list = []
        self.menu = []
        
        with open("menu.txt") as file:      #Open file to read the data.
            self.lines = file.readlines()
            
            for line in self.lines[1:]:
                self.data = line.strip().split(";")     #Clearing the data section.
                self.category_list.append(self.data[0])
                self.menu.append(self.data)     
                
        self.category_list = list(dict.fromkeys(self.category_list))    #list(dict.fromkeys()) removes repeated items in a list.


    """
    MAKE ORDER METHOD
    In this section the program calls methods one by one to follow the gradual flow. 
    """
    def make_order(self):
        self.order_list = []
        while True:         
            self.display_category()         #Gradual flow begins here.
            self.display_name()
            self.display_portion()
            self.temp = [self.portion,self.portion_list[self.portion_choice - 1]]
            self.order_list.append(list(self.temp))         #Appending orders to my order_list.
            self.operation = self.display_operation()
            if self.operation == 2:
                break
            
        self.display_checkout()

    """
    DISPLAY CATEGORY METHOD
    In this section the program displays category selection.
    """
    def display_category(self):
        i = 1
        print("Product Categories")
        for category in self.category_list:
            print(f"{i}.",category)     #Formatting the output for visibility.
            i += 1

        while True:
            try:
                self.category_choice = int(input("Please select product category: ")) #Handling invalid inputs.

                if 0 < self.category_choice < len(self.category_list) + 1:
                    print("--------------------") 
                    break
                else:
                    print("Invalid category choice..!")
            except ValueError:
                print("Invalid category choice..!")


    """
    DISPLAY NAME METHOD
    In this section the program displays name selection.
    """
    def display_name(self):
        self.name = self.category_list[self.category_choice - 1]
        self.name_list = []
        print("Products in",self.name)
        for i in range(len(self.menu)):
            if self.name in self.menu[i][0]:
                self.name_list.append(self.menu[i][1])      #Filtering names from the data by using product category.
                
        self.name_list = list(dict.fromkeys(self.name_list))
        j = 1
        for name in self.name_list:
            print(f"{j}."+name)     #Formatting the output for visibility.
            j += 1

        while True:
            try:
                self.name_choice = int(input("Please select product name: ")) #Handling invalid inputs.
                if 0<self.name_choice<len(self.name_list)+1:
                    print("--------------------")
                    break
                else:
                    print("Invalid product choice..!")
            except ValueError:
                print("Invalid product choice..!")
                  

    """
    DISPLAY PORTION METHOD
    In this section the program displays portion selection.
    """
    def display_portion(self):
        self.portion = self.name_list[self.name_choice - 1]
        self.portion_list = []
        print(str(self.portion).lstrip(" "),"Portions")     #Filtering portions from the data by using product name.
        for i in range(len(self.menu)):
            if self.portion in self.menu[i][1]:
                self.portion_list.append(self.menu[i][2])

        j = 1         
        self.portion_list = list(dict.fromkeys(self.portion_list))
        for portion in self.portion_list:
            print(f"{j}."+portion)      #Formatting the output for visibility.
            j += 1

        while True:
            try:
                self.portion_choice = int(input("Please select product portion: "))     #Handling invalid inputs.
                if 0 < self.portion_choice < len(self.portion_list) + 1:
                    print("--------------------")
                    break
                else:
                    print("Invalid protion choice..!")
            except ValueError:
                print("Invalid protion choice..!")


    """
    DISPLAY CHECKOUT METHOD
    In this section the program displays the recepit.
    """
    def display_checkout(self):
        for i in range(len(self.menu)):
            for j in range(len(self.order_list)):
                if self.menu[i][1:3] == self.order_list[j]:
                    self.order_list[j].insert(2,self.menu[i][3])        #Using nested loop for finding products to be appended to my order_list.

        self.total_amount = 0
        for i in range(len(self.order_list)):
            self.amount = float(self.order_list[i][2].lstrip(" ").lstrip("$"))
            
            self.total_amount += self.amount        #Calculating total amount.
            
        print("----------------------------------------------------------------------")         #Formatting the output for visibility.
        for i in range(len(self.order_list)):
            print(f"{''+str(self.order_list[i][0]).strip():<40}{''+str(self.order_list[i][1]).strip():<20}{''+str(self.order_list[i][2]).strip()}")
            
        print("----------------------------------------------------------------------")
        print("Total:                                                      ${:.2f}".format(self.total_amount))


    """
    DISPLAY OPERATION METHOD
    ------------------------
    In this section the program ask what operation do you want.
    If the operation is 1:
        The customer can continue to make order.
    If the operation is 2:
        The recepit is shown to the customer.
    """
    def display_operation(self):
        print("1. Add New\n2. Check Out")
        while True:
            try:
                self.operation = int(input("Please select an operation: "))  
                
                if self.operation == 1:
                    break
                
                elif self.operation == 2:
                    break

                else:
                    print("Invalid operation..!")
            except ValueError:
                print("Invalid operation..!")

        return self.operation


def main():
    menu = Menu()       #Creaing my menu Object.
    menu.make_order()       #Starting MAKE ORDER function.

main()