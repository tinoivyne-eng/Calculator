# Functions and operators

def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
   try:
       return x / y
   except ZeroDivisionError:
       return "Error: Cannot divide by zero "

# Show text

print("Calculator")   
print("Choose Operation : ")
print("1. Add:")
print("2. Subtract:")
print("3. Multiply:")
print("4. Divide:")


# inputs

choice = (input("Enter your choice between (1/2/3/4) :"))

if choice not in ["1", "2", "3", "4"]:
    print("Invalid choice")
else:
    first_num = float(input("Enter your first number here :"))
    second_num = float(input("Enter your second number here :"))


# comparisons

    if choice == "1":
        print("Result = ", add(first_num, second_num))

    elif choice == "2":
        print("Result =  ", subtract(first_num, second_num))

    elif choice == "3":
        print("Result = ", multiply(first_num, second_num))

    elif choice == "4":
        print("Result = ", divide(first_num, second_num))
    else:
         ("Print Invalid choice")
    