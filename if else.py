
1.num=int (input("enter the number :"))
if(num%2==0):

    print("number is even")
else:
    print("number is odd")
-----------------------------------------------------------------------
2.a=int (input("enter the number :"))
b=int (input("enter the number :"))
c=int (input("enter the number :"))
if(a>b):
    print("a is largest ")
elif(b>c):
    print("b is largest ")
elif(c>a):
    print("c is largest ")
else:
    print("number is not valid")
----------------------------------------------------------------------
3.num=int (input("enter the number :"))
if(num%4==0 or num%400==0):
    print ("number is leap year ")
else:
    print("number is not leap year ")
----------------------------------------------------------------------
4.num=int (input("enter the number :"))
if(num>80):
    print("Grade A")
elif(num>70):
    print("Grade B")
elif(num>60):
    print("Grade C")
elif(num>50):
    print("Grade D")
else:
    print("Grade F")
----------------------------------------------------------------------
5.char=input("enter the character :")
if(char=='a'or char=='e'or char=='i'or char=='o'or char=='u'):
    print("vowel")
else:
    print("consonant")
----------------------------------------------------------------------
6.first=int(input ("enter  first:"))
second=int(input ("enter second :"))
print("sum =",first + second)
----------------------------------------------------------------------
7.first=int(input ("enter  first:"))
second=int(input ("enter second :"))
print("sum =",first + second)
print("sub =",first - second)
print("multi=",first * second)
print("divi=",first / second)
----------------------------------------------------------------------
8.num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
----------------------------------------------------------------------
9.char1=input("enter the name :")
char2=input("enter the password :")
if (char1== 'admin' or char2 == '1234'):
  print("lodin sucessful")
else:
    print("Login Failed")
----------------------------------------------------------------------
10.a=int(input ("enter the first"))
b=int(input ("enter the second"))
c=int(input ("enter the third"))
if(a + b > c and  b + c > a  and a + c > b ):
    print("tringle is valid")
else:
    print("tringle is not valid")
----------------------------------------------------------------------
11.weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(" Underweight")
elif 18.5 <= bmi < 24.9:
    print(" Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")
----------------------------------------------------------------------
12.float= float(input("Enter your number : "))
price=float>1000
if price % 10:
    print("10 % discount avalible ")
elif(1000>500):
    print("5 % discount avalible ")
else:
    print("no discount ")	
----------------------------------------------------------------------	
13.int=int(input("enter the number:"))
if(int<0):
    print("infant")
elif(int<4):
    print("toddler")
elif(int<12):
    print("chlid")
elif(int<19):
    print("teenager")
elif(int<59):
    print("adult")
elif(int<60):
    print("senior")
else:
    print("")
 
----------------------------------------------------------------------	
14.week = int(input("Enter a number (1,7): "))

if week == 1:
    print("Monday")
elif week == 2:
    print("Tuesday")
elif week == 3:
    print("Wednesday")
elif week == 4:
    print("Thursday")
elif week == 5:
    print("Friday")
elif week == 6:
    print("Saturday")
elif week == 7:
    print("Sunday")
else:
    print("Invalid number")
----------------------------------------------------------------------	
15.balance =10000
print("ATM")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

number = int(input("Enter your choice (1-3): "))

if number == 1:
    print("balance is:", balance)

elif number == 2:
    deposit = float(input("Enter to deposit amount: "))
    if deposit > 0:
        balance += deposit
        print("Deposit successful")
    else:
        print("machine error ")

elif number == 3:
    withdraw = float(input("withdraw amount: "))
    if withdraw > balance:
        print("withdraw balance")
    elif withdraw <= 0:
        print("machine error ")
    else:
        balance -= withdraw
        print("Withdrawal successful")

else:
    print("enter the 1,2,3")
----------------------------------------------------------------------	
16.num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
ch = input("+,-,*,/: ")
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("character is not valid")

print(num1, ch , num2, ":", result)
----------------------------------------------------------------------	

