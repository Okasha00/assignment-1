#Assignment 1
#make a simple Calculater
#BY usman naeem

                                       # start programe
num1 = int(input("enter first number\n"))
num2 = int(input("enter second number\n"))

operater = input("select operater to perform \t'6+ for addition' \t'- for subtraction' \t'* for product' \t'/ for division'\n")

if operater == '+':
    print("sum = ",num1+num2)
elif operater == '-':
    print("subtraction =",num1-num2)
elif operater == '*':
    print("product = ",num1*num2)
elif operater == '/':
    print("division =",num1/num2)
