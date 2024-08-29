#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == 'admin' and password == '12345':
        return 'Access granted'
    elif username == 'ADMIN' and password == '12345':
        return 'Access granted'
    else:
        return 'Access denied'
    pass

def hows_the_weather(temperature):
    # your code here
    temperature == 33
    temperature == 55
    temperature == 99
    temperature == 75
    
    if temperature == 33:
        return 'It\'s brisk out there!'
    elif temperature == 55:
        return 'It\'s a little chilly out there!'
    elif temperature == 99:
        return 'It\'s too dang hot out there!'
    elif temperature == 75:
        return 'It\'s perfect out there!'
    pass

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero")
    else:
        print("Invalid operation!")
        return None
    pass
