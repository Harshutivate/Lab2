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

def calc_median(input_values):
    # Step 1: Find the two middle values
    middle_index1 = len(input_values) // 2 - 1# middle value 1 if(2,4,6,8) it give 4
    middle_index2 = len(input_values) // 2# middle value 2 if(2,4,6,8) it give 6
    
    # Step 2: Calculate their average of the wo middle values
    median = (input_values[middle_index1] + input_values[middle_index2]) / 2
    
    print("Median = ", median)


    
display_main_menu()
input_values = get_user_input()
calc_average_temperature(input_values)
find_min_max()
calc_median(input_values)