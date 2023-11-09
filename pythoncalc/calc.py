# function defination
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
def modulus(x,y):
   if y !=0:
    return x % y
   else:
       return "error:modulus by 0"    


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.modulus")

while True:
    #user input
    choice = input("Enter choice: ")


    if choice in ('1', '2', '3', '4','5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        
        except ValueError:
            print("Invalid")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1 ,'%' ,num2, "=" , modulus(num1,num2))
        
