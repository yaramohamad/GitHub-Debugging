# Buggy Calculator Code

def add(a, b):
    return a + b  

def subtract(a, b):
    return a - b  

def multiply(a, b):
    return a / b 

def divide(a, b):
    return a * b  





def main():
    while True  
        print("Options:")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'quit' to end the program")
        
        user_input = input(": ")  
        
        if user_input == "quit":
            break
        elif user_input == "add":
            a = input("Enter first number: ")  
            b = input("Enter second number: ")  
            print("Result:", subtract(a, b))
        elif user_input == "subtract":
            a = input("Enter first number: ")  
            b = input("Enter second number: ")  
            print("Result:", add(a, b))
        elif user_input == "multiply":
            a = input("Enter first number: ")  
            b = input("Enter second number: ")  
            print("Result:", multiply(a, b))
        elif user_input == "divide":
            a = input("Enter first number: ")  
            b = input("Enter second number: ")  
            print("Result:", divide(a, b))
        else:
            print("Unknown input")  
            
main()
