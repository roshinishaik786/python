Num=int(input("enter the integer :"))
if((Num%3==0) and (Num%5==0)):
    print(Num,"is a multiple of 3 and 5")
else:
    print(Num,"is not multple with 3 and 5")
result="multiple of 3 and 5" if((Num%3==0) and (Num%5==0)) else "not multiple whit 3 and 5"
print(result)