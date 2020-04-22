# calculetor code 

# this function add only two number
def add(x , y):
    return(x + y)

# this function subtracts only two number
def subtract(x , y):
    return(x - y)

# this function multipy only two function
def multiply(x , y):
    return(x * y)

# this function devide only two function 
def devide(x , y):
    return(x / y)
# this function power two functionn
def power(x , y):
    return(x ** y)
# this function make parcent between two function
def percent(x , y):
    return(x % y)

print ("choose a option")
print("1.addition")
print("2.subtract")
print("3.multiply")
print("4.devition")
print("5.power")
print("6.percent")

# take input from user
choice = input("choose one (1/2/3/4/5/6)")
num1 = float(input("enter first opareted number:"))
num2 = float(input("enter secend opareted number:"))

if choice == '1':
    print(num1, "+" , num2, "=", add(num1 ,num2))

elif choice == '2':
    print(num1, "-" ,num2, "=", subtract(num1 ,num2))

elif choice == "3":
    print(num1, "*" ,num2, "=" , multiply(num1 , num2))

elif choice == '4':
    print(num1 , "/" , num2, "=", devide(num1 , num2))
    
elif choice == '5':
     print(num1, "**" ,num2, "=" , power(num1 , num2))
     
elif choice == '6':
    print(num1, "%" ,num2, "=" , percent(num1 , num2))
     
else:
    print("this input is not valid")