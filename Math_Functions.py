import math
print("Welcome to the simple math helper. \nWhat would you like to calculate?")
choice = int(input("1. Sqrt \n2. Log\n3. Factorial \n>"))

if choice == 1:
    value = int(input("Enter the number to sqrt:\n>"))
    print(math.sqrt(value)) 
    
elif choice > 1 and choice == 2 :
    value = int(input("Enter the number for the log:\n>"))
    print("Common logarithm: ",math.log(10,value))
    print("\nNatural logarithm: ",math.log(value))
    
elif choice > 2 and choice == 3 :
    value = int(input("Enter the number for the Factorial:\n>"))
    print (math.factorial(value))
