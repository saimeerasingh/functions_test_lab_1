
def return_10():
    return 10

def add(num1,num2):
    return num1 + num2 

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1/num2

def length_of_string(string):
    return len(string)    

def join_string(string1,string2):
    return string1 + string2

def add_string_as_number(string1,string2):
    return int(string1) + int(string2)


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def number_to_full_month_name(num1):
    return months[num1 -1]

def number_to_short_month_name(num1):
    return (months[num1-1][:3])

def volume_of_cube(num1):
    return pow(num1,3)

def test_reverse_string(string1):
    return string1[::-1]

def test_fahrenheit_to_celsius(farenheit):
    celsius = (farenheit - 32) * (5.0/9.0)
    return celsius