#1 comparision operator
'''
a=int(input("Enter a:"))
b=int(input("Enter b:"))

if a>b:
    print("b is Smallest")
else:
    print("a is Smallest")

#2 largest(c o)

a=int(input("Enter a:"))
b=int(input("Enter b:"))

if a>b:
    print("a is Largest")
else:
    print("b is Largest")

#3 absolute number

num=int(input("Enter number:"))

res=abs(num)

print("Absolute number:",res)

#4 even or odd

num=int(input("Enter number:"))

if num%2==0:
    print("Number is Even")
else:
    print("Number is Odd")

#5 check mult 5

num=int(input("Enter number:"))

if num%5==0:
    print("Number is Multi of 5")
else:
    print("Number is not Multi of 5")

#6 check mult 10

num=int(input("Enter number:"))

if num%10==0:
    print("Number is Multi of 10")
else:
    print("Number is not Multi of 10")

#7 check num is two digit

num=int(input("Enter Number:"))

if num>=10 and num<=99:
    print("Number is two digit")
else:
    print("Number is not two digit")

#8 check num is three digit

num=int(input("Enter Number:"))

if num>=100 and num<=999:
    print("Number is three digit")
else:
    print("Number is not three digit")

#9check num end with zero

num=int(input("Enter the Number:"))

if num%10==0:
    print("A numbers is end with zero")
else:
    print("A numbers is not end with zero")

#10 50 ><

num=int(input("ENter the Number:"))

if num**2>=50:
    print("A number of sq is greater 50")
else:
    print("A number of sq is lesser 50")

#11  0/NOT

a=int(input("Enter Number a:"))
b=int(input("Enter NUmber b:"))

if (a-b)==0:
    print("difference is 0")
else:
    print("difference is",a-b)

#12 cs pass/fail
sciencemark=int(input("Enter Mark:"))

if sciencemark>=50:
    print("Pass")
else:
    print("Fail")

#13 divi by 10
num=int(input("Enter Number:"))

if num%10==0:
    print("Num is divisible by 10")
else:
    print("Num is not divi by 10")

#14

a=int(input("Enter a:"))
b=int(input("Enter b:"))

if a>b:
    print("A is biggest digit")
else:
    print("B is biggest digit")

#15 based on choice
num=int(input("Enter the Number:"))

if num==1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")

#16 based on choice
num=int(input("Enter the Number:"))

if num==1:
    print("You can go out and play")
else:
    print("You cannot go out and play")

#17 square or rectangle
len=int(input("Enter length:"))
bre=int(input("Enter breadth:"))

if len==bre:
    print("its square")
else:
    print("its rectangle")

#18 ASCII value for upper case

n=int(input("Enter ASCII num:"))

if n>=65 and n<=90:
    print("In the range of ASCII(upper case)",n)
else:
    print("Not upper case range")


#19 ASCII value for lower case

n=int(input("Enter ASCII num:"))

if n>=97 and n<=122:
    print("In the range of ASCII(lower case)",n)
else:
    print("Not lower case range")

#20 ASCII value for numeric

n=int(input("Enter ASCII num:"))

if n>=48 and n<=57:
    print("In the range of ASCII(numeric)",n)
else:
    print("Not in numeric range")

#21 mutli of 3 and 5

num=int(input("Enter the number:"))

if num%5==0 and num%3==0:
    print("A entered number is mutliple of 3 and 5")
else:
    print("Number is not multiple of 3 and 5")

#22 num is three digit and multi of 10

num=int(input("Enter the number:"))


if num>=100 and num<=999 and num%10==0:
    print("a given number is a three-digit number and also a multiple of 10")
else:
    print("digit is not three digit or not divisbile by 10")

#23 num is three digit and multi of 2,5,10

num=int(input("Enter the number:"))


if num>=100 and num<=999 and num%2==0 and num%5==0 and num%10==0:
    print("a given number is a three-digit number and also a multiple of 2, 5, and 10")
else:
    print("digit is not three digit or not divisbile by 2,5,10")


#24 even num and product them

a=int(input("Enter a :"))
b=int(input("Enter b :"))

if a%2==0 and b%2==0:
    print("given inputs are even and its product:",a*b)
else:
    print("Sum of a and b is:",a+b)

#25 buzz number 

num=int(input("Enter Number:"))

if num%10==7 and num%7==0:
    print("its buzz number")
else:
    print("not buzz number")

#if elif else

#26 largest number three integers

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

if a>b and a>c:
    print("A is greater number")
elif b>a and b>c:
    print("B is greater number")
else:
    print("c is greater number")

#27 smallest number in three integers

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

if b>a and c>a:
    print("A is smallest number")
elif a>b and c>b:
    print("B is smallest number")
else:
    print("c is smallest number")

#28 pos/neg

num=int(input("Enter num:"))

if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

#29 libary charges
days=int(input("Enter days:"))

if 1<=days<=5:
    print("40 paisa per day")
elif 6<=days<=10:
    print("65 paisa per day")
else:
    print("80 paisa per day")

#30 basic calculator

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
oper=input("Enter operation +,-,*,/:")

if oper=='+':
    print("add operation:",num1+num2)
elif oper=='-':
    print("sub operation:",num1-num2)
elif oper=='*':
    print("mutli operation:",num1*num2)
elif oper=='/':
    print("divi operation:",num1/num2)

#31 number is divi by 3,5,7

num=int(input("Enter num:"))

if num%3==0:
    print("Num is divi by 3")
elif num%5==0:
    print("Num is divi by 5")
elif num%7==0:
    print("Num is divi by 7")

#32  tariff

weight=int(input("Enter weight of the parcel:"))
typ=input("Enter type of booking(Ordinary/Express):")

if 1<=weight<=100 and typ=="O":
    print("Ord Booking 80")
elif 1<=weight<=100 and typ=="E":
    print("Exp Booking 100")
elif 101<=weight<=500 and typ=="O":
    print("Ord Booking 150")
elif 101<=weight<=500 and typ=="E":
    print("Exp Booking 200")
elif 501<=weight<=1000 and typ=="O":
   print("Ord Booking 210")
elif 501<=weight<=1000 and typ=="E":
    print("Exp Booking 250")
elif weight>=1000:
   print("Ord Booking 250 and Exp Booking 300")


#33 purchase laptop

price = float(input("Price of laptop : "))

if price <= 50000:
    discount = 0

elif price <= 100000:
    discount = price * 10 / 100

elif price <= 150000:
    discount = price * 15 / 100

else:
    discount = price * 20 / 100

total_price = price - discount

print("Price of laptop :", price)
print("Discount :", discount)
print("Total Price :", total_price)'''

    




    






