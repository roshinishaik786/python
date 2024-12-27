num1=int(input("enter the first number :"))
num2=int(input("enter the second number"))
print("before swapping :")
print("num1:",num1)
print("num2:",num2)
num1,num2=num2,num1
print("after swapping :")
print("num1:",num1)
print("num2:",num2)
#swapping using third variable
temp=num1
num1=num2
num2=temp
print("after swapping :")
print("num1=",num1)
print("num2=",num2)
#arithmetic operator
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("after swapping :")
print("num1=",num1)
print("num2=",num2)
