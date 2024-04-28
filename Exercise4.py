def display_main_menu():
    print("Enter some numbers separated by commas (eg. 5,67,32)")

def get_user_input():
    num = input()
    comm = num.split(",")
    input_values = []  # Initialize an empty list to store input values
    for i in comm:
        conv = float(i)  # Convert each input value to float and assign it to conv
        input_values.append(conv)  # Append conv to the list of input values
        print(conv)
    return input_values  # Return the list of input values

def calc_average_temperature(input_values):
    total_sum = sum(input_values)  # Sum up all input values
    average = total_sum / len(input_values)  # Calculate average
    print("Average:", average)

def find_min_max():
    print("Max",max(input_values))
    print("Min",min(input_values))
    
display_main_menu()
input_values = get_user_input()
calc_average_temperature(input_values)
find_min_max()
