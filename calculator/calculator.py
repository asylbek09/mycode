#!/usr/bin/env python3

def add(num1, num2):
    result = num1 + num2
    print(f"Result: {result}\n")

def subtract(num1, num2):
    result = num1 - num2
    print(f"Result: {result}\n")

def multiply(num1, num2):
    result = num1 * num2
    print(f"Result: {result}\n")

def divide(num1, num2):
    result = num1 / num2
    print(f"Result: {result}\n")

def main():

    trycalc = input('''Welcome to Simple Calculator!
    Do you want to use calculator? <y> or <anykey> to quit ''')

    while(trycalc == 'y'):
        
        choice = input('''Please enter:
        1 --> Addition
        2 --> Subtraction
        3 --> Multiplication
        4 --> Division
        q --> Quit \n''')

        if(choice == 'q'):
            break
        elif(choice == '1' or choice == '2' or choice == '3' or choice == '4'):
            input1 = int(input("Enter first number: "))
            input2 = int(input("Enter second number: "))

            if(choice == '1'):
                add(input1, input2)
            elif(choice == '2'):
                subtract(input1, input2)
            elif(choice == '3'):
                multiply(input1, input2)
            elif(choice == '4'):
                if input2 == 0:
                    print("Can't divide by 0")
                else:
                    divide(input1, input2)
        else:
            print("Try again with correct inputs")
                
main()