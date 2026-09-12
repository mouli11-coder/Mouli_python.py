#Student Management system

Name=input("Enter student name:")
Roll_Number=int(input("Enter Roll Number:"))
Department=input("Enter Department")

#Input Mark

Python=int(input("Enter Python mark:"))
English=int(input("Enter English mark:"))
Maths=int(input("Enter Maths mark:"))

Total=Python+English+Maths
Average=Total/3

#Grade
if Total>=250:
    Grade= "A"

elif 150<=Total<=200:
     Grade="B"
elif 100<=Total<=150:
     Grade="C"
else:
     Grade="D"
#Pass/Fail

if Total>=100:
    Result="Pass"
else:
    Result="Fail"

print("-----------------")
print("  STUDENT MARK SHEET     ")
print("-----------------")
print(f"Name: {Name}")
print(f"Roll_Number: {Roll_Number}")
print(f"Department: {Department}")
print("----------------------------")
print(f"Python: {Python}")
print(f"English: {English}")
print(f"Maths: {Maths}")
print("----------------------------")
print(f"Total : {Total}")
print(f"Average : {Average}")
print(f"Grade: {Grade}")
print(f"Result: {Result}")
print("----------------------------")




    

