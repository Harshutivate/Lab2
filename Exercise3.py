def display_main_menu():
    print("Enter some numbers seperated by commas(eg. 5,67,32")
    
def get_user_input():
    num = input()
    comm = num.split(",")
    print(comm)
    for i in comm:
        conv = float(i)
        print(conv)
    
def calc_average():
    print("calc_average")
    
def find_min_max():
    print("no")
def sort_temperature():
    print("no")
def calc_median_temperature():
    print("no")
display_main_menu()
get_user_input()