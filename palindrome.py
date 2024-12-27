num=int(input("enter the integer value :"))
rem=0
reversed_num=0
n=num
while(num!=0):
    rem=num%10
    reversed_num=reversed_num*10+rem
    num//=10
if(reversed_num==n):
    print(n,"it is a palindrome number")
else:
    print(n," it is not a palindrome number ")