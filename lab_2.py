
def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    inputstr = input()
    strlist = inputstr.split(",")
    floatlist = []
    for x in strlist:
        floatlist.append(float(x))
    return floatlist

def calc_average(float_list):
    print("calc_average")
    average = sum(float_list) / len(float_list)
    print("Average:", average)
    return average

def find_min_max(float_list):
    print("find_min_max")
    temp_list = float_list.copy()
    temp_list.sort()
    return [temp_list[0], temp_list[-1]]

def calc_median_temperature(float_list):
    print("calc_median_temperature")
    return calc_median_temperature
    # Make a copy and sort it in ascending order
    temp_list = float_list.copy()
    temp_list.sort()
    
    n = len(temp_list)
    mid = n // 2 
    
    # If even number of elements, average the two middle values
    if n % 2 == 0:
        median = (temp_list[mid - 1] + temp_list[mid]) / 2
    # If odd number of elements, take the middle value
    else:
        median = temp_list[mid]
    
    print("Median:", median)
    return median


display_main_menu()
float_list = get_user_input()

calc_average(float_list)
find_min_max(float_list)
calc_median_temperature(float_list)
