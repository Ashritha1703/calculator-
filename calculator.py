#addition of two numbers
def add(x,y):
    return x+y
#subtraction of two numbers
def subtraction(x,y):
    return x-y
# multiplication of two numbers
def multiplication(x,y):
    return x*y
#division of two numbers
def division(x,y):
    return x/y
print("select opperation")
print("1.add")
print("2.suntraction")
print("3.multiplication")
print("4.division")
while True:
    #choosing the operation from user
    choice=input("select number(1/2/3/4):")
    #check the operation of 1 to4
    if choice in("1","2","3","4"):
        try:
            num1=float(input("enter a number:"))
            num2=float(input("enter a number:"))
        except valueError:
            print("invalid input,please valid number")
            # addition opration 
        if choice=="1":
            print(num1,"+",num2,"=",add(num1,num2))
            #subtraction operation
        elif choice=="2":
            print(num1,"-",num2,"=",subtraction(num1,num2))
            #multiplication operation
        elif choice=="3":
            print(num1,"*",num2,"=",multiplication(num1,num2))
            #division operation
        else:
            print(num1,"/",num2,"=",division(num1,num2))
        next_calculation=input("if you want to perform other calculation? (yes/no):")
        if next_calculation=="no":
            break
    else:
        print("invalid input")
    

