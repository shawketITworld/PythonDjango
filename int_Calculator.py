def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)
    
num1= int(input("Enter First Number:"))    
num2= int(input("Enter Second Number:")) 

print("Please Select Any One Option: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5.Exit")


while(True):
    choice=int(input("Enter The Choice from (1/2/3/4/5) :"))
    if choice in (1,2,3,4,5):
        if choice==1:
           print("Addition of two number",num1, "and", num2, "is :",add(num1,num2))
        elif choice==2:
           print("Subtraction of two number",num1, "and", num2, "is :",sub(num1,num2))
        elif choice==3:
           print("Multiplication of two number",num1, "and", num2, "is :",mul(num1,num2))
        elif choice==4:
           print("Division of two number",num1, "and", num2, "is :",div(num1,num2))
        elif choice==5:
           print("Thank You")
           exit()
    else:
       print("Invalid Choice number try again please")       