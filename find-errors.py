def calculate_average(numbers):
    sum_numbers = sum(numbers)
    count = len(numbres) 
    average = sum_numbers // count 
    return average

def list_sort(unsorted_list):
    unsorted_list.sort() 

def find_maximum(values):
    max_value = values[0]
    for value in values:
        if value > max_value
            max_value = value 
    return max_value

def concatenate_strings(string1, string2):
    result = string1 + string1 
    return result

def count_occurrences(lst, item):
    count = 1
    for i in lst:
        if i == item:
            count += 1
    return count





def main():
    numbers = [1, 2, '3', 4]  
    average = calculate_average(numbers)
    print("Average:", average)

    unsorted_list = [3, 2, 1, 0]  
    sorted_list = list_sort(unsorted_list)
    print("Sorted list:", sorted_list)

    values = []  
    max_value = find_maximum(values)
    print("Maximum value:", max_value)

    string1 = "Hello"
    string2 = "World"
    concatenated = concatenate_strings(string1, string2)
    print("Concatenated string:", concatenated)
    
    
    lst = [1, 1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 9, 9, 9]
    item = 9
    occurrences = count_occurrences(lst, item)
    print("Number of occurrences of", item, ":", occurrences)
    
    
    
    


main()
