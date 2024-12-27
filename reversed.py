num=int(input("enter the integer value :"))
rem=0
reversed_num=0
while(num!=0):
    rem=num%10
    reversed_num=reversed_num*10+rem
    num//=10
print("reversed number",reversed_num)