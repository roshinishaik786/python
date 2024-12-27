name=input("enter the student name :")
s1=int(input("enter subject1 score :"))
s2=int(input("enter student2 score :"))
s3=int(input("enter student3 score :"))
print("student report :")
print("-----------------------")
print("student name:",name)
print("subject1 score :",s1)
print("subject2 score :",s2)
print("subject3 score :",s3)
if(s1>=35 and s2>35 and s3>=35):
    total=s1+s2+s3
    print("total :",total)
    average=total/3
    print("average :",average)
    if(average>=90):
        print("congratulations you have passed the 1st class")
    elif(average>=75):
        print("congratulations you have passed the 2nd class")
    else:
        print("congratulations you have passed the 3rd class")
else:
    print("better luck next time")

