print("************** 1. Basics of Python Programing*************")
'''Day1 Learning (theory)
IDEs, REPL..
Foundation of a Programming Language (refer the notes)
What is python
Why Python
Interpreter vs Compiler
How a python program run
'''
######### ALL ABOUT VARIABLES ##########
#Day2 Learning
'''1. Variable Properties -
Dynamic inference - based on the assigned value it will automatically decides/infer/identify/refers the type dynamically
'''
name="inceptez"
salary=10000

#Dynamically typed: If a variable is created with a specific data type, can be changed later
salary=10000
print(type(salary))
salary="Ten thousand"
print(type(salary))

#Strongly typed: Python allow us to operate between the variables of same datatype (of the same hierarchy) and doesn't allow to operate between different datatypes.
print(name+salary)
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
'''

#2. naming convention
#A variable can have camel case or init upper or with underscores
empSal=10000
EmpSal=10000
emp_sal=10000
#A variable name must start with a letter or the underscore character
sal=10000
_sal=10000
#A variable name cannot start with a number
#below doesnt work
#1emp_sal=10000
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
emp1_sal=10000
#below doesnt work
#emp1-sal=10000
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#both are different...
Age=40
age=35

#3. How to check a given TYPE is of what we expect (isinstance) or doing typecasting int(), str(), float()

sal=10000
bonus=2000
print(type(sal))
print(type(bonus))
nett_sal=sal+bonus

#not possible due to strongly typed feature
sal=10000
bonus='2000'
#nett_sal=sal+bonus

#not possible due to strongly typed feature
sal=10000
bonus='2000'
nett_sal=sal+int(bonus)
print(nett_sal)

sal=10000
#bonus='2000'
bonus=2000

if isinstance(bonus,str):
 nett_sal=sal+int(bonus)
 print(nett_sal)
else:
 nett_sal=sal+bonus
 print(nett_sal)


#4. input (assigning value directly/using input function/passing arguments) / output (print/assigning/return)
#assigning value directly (Hardcoding)
sal=10000

#Run time input
#below input will collect salary as string (using input function)
sal=input()
#below input will collect salary as string and type cast to int
sal=int(input())
bonus=int(input())

if isinstance(bonus,str):
 nett_sal=sal+int(bonus)
 print(nett_sal)
else:
 nett_sal=sal+bonus
 print(nett_sal)

#pass parameters to a variable
def func1(x):
 a=x;
 print(a)

func1(1000)

#Day3 Learning
print("A. Python is an indent based programming language")
# Indentation can be using tab or spaces (usually 4 spaces),
# the levels of indent help to write blocks of code rather than using braces
#Python is an indend based prog language
#indents help you write the code with better readability and python needs it mandatorily, since we dont have block options like (do/done) or {} in python
#indendation has to be uniform within the block of code (not across the block of code)
#optimal number of spaces used for doing intendation is 4 spaces
#No indendation is needed, because we are not doing any block operation
empid=1
sal=10000
bonus=1000
nett_sal=sal+bonus
print("nett sal of emp",empid, " is ",nett_sal)

#Indendation is needed, because we are doing block operation with in the for loop
empid=list([1,2])
sal=list([10000,20000])
bonus=1000
for i in sal:
    nett_sal=i+bonus
    print("nett sal is ",nett_sal)

print("nett sal is ",nett_sal)

#indendation has to be uniform within the block of code (not across the block of code)
for i in sal:
	nett_sal=i+2000
	print("nett sal is ",nett_sal)

for i in sal:
        nett_sal=i+2000
        print("nett sal is ",nett_sal)

print("B. This is a commented line in Python")
#Hash is used for single line comment
'''
For multiline Comments
We use 3 enclosed single quotes
'''

#Python treats single quotes the same as double quotes.
print("C. Playing with Quotes: Python treats single quotes the same as double quotes.")
#both the below asset variables are same
asset1='This is Inceptez Technology Asset'
asset2="This is Inceptez Technology Asset"
print(asset1)
print(asset2)

#Need of using double quotes
#we can use escape sequence also
asset1='This is Inceptez Technology\'s Asset'
#Enclose single quotes with double quotes to use any number of single quotes

asset1="This is Inceptez Technology's Asset"
#below will consider the entire text in a single line, but wanted to type multiple lines
asset2="This is Inceptez Technology's Asset \n This is used for our learning"
print(asset1)
print(asset2)
#For handling paragraph/multilines text, we can use 3 single or doublequotes
paragraph='''Dynamically Inferred
Dynamically Typed
Strongly Typed'''
paragraph="""Dynamically Inferred variable's
Dynamically Typed variable's
Strongly Typed variable's"""
paragraph='''Dynamically Inferred "variable"
Dynamically Typed
Strongly Typed'''

print("D. Standard output options of print statements")
empname="Vidhya"
sal=10000
print("empname is getting a salary of sal")
#print(empname + " is getting a salary of "+sal)
#below print function is taking only 1 argument
string_to_print=empname + " is getting a salary of "+str(sal)
print(string_to_print)
#below print function is taking 3 arguments and printing them individually
print(empname," is getting a salary of ",sal,"this emp ",empname,"is a happy employee")
empname="Magi"
sal=20000
print(empname," is getting a salary of ",sal)

#Formatted string Print statements - positional args
print("{0} is getting a salary of {1} and {0} is happy with it".format(empname,sal))

#Formatted string Print statements other way (3.6x onwards) - named args
print(f"{empname} is getting a salary of {sal}")

print("E. Variable Properties - Dynamic inference + mutable & immutable properties")
employername="inceptez"
print(type(employername))

#Mutable & Immutable Properties at the nutshell (We learn this in collection types)
#list are mutable
empnames=["Prem","Selva","Bala"]
empnames[0]='Mage'

#strings are immutable (indexed sequenced collection of alphanumeric characters)
employername="inceptez"
#below operation represents, we are trying to update a variable (not possible due to immutable characteristics)
#update statement in hive
employername[0]='I'
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
'''
#below operation represents, we are recreating/reinitializing/reassigning the value to a variable
#insert overwrite statement in hive
employername=employername.capitalize()

#Day4 Learning
print('F. Simple Datatypes, Complex Datatypes (list,dictionary,tuple,set) learning subsequently')
#numeric - int,float,exponential/complex
#string - str
#other datatypes - bool, bytes, None
#int
a:int=100
a:int=100.10
a:int=int(100.10)
#or
#float
a:float=100.10
#complex
a=3e100

#string - sequence datatype
a:str="inceptez"
print(a[0])

#Misc/other datatypes
#bool - usually functions return boolean type, can be used for unconditional conditional structures like if or for infinate looping
a:bool=True
a:bool=False
#bytes is used to convert a value to binay object that can be used as reference.
a:bytes=bytes(100)
memoryview(a)

#None type - None is used for futuristic purposes as a placeholder Unknown Equivalent to Null type in our DB
a:None=None

print('G. Operators')
#Operators help us -> arithmetic, comparison/relational, assignment, logical
#using assignment+arithmetic operators
a=10+20
#a+=10
b=20+20
#comparison/relational
print(a==b)
#logical
print(not(a==b))

#Assignment Operators -> Arithmetic Operators -> Relational Operators -> Logical Operators
#find the greatest of 2 numbers
a=100
b=50+int(input())
if a>b or a==b:
 print("a is greater or equal to b")
else:
 print("b is greater")

#Try to know, but not important
#Bitwise Operators - bit by bit comparison, hence slow in performance, hence used very less..
a=100
b=50+int(input())
if (a>b) | (a==b):
 print("a is greater than b or a is equal to b")
else:
 print("b is greater")

#Unary Operator - a single operator doesn't really operates when defined, but if applied with binary operator it will be operated
amt=-100
print(amt)

#Binary Operator - operating two or more opertors is binary
total_amt=amt+10
print(total_amt)

#Ternary operator
curtime=8.30
salutation="Good morning" if (curtime >=0) & (curtime<12.0) else "Good night"


print("H.Built in functions on top of the variables")
#how to use builtin functions - Depends upto the need (NO NEED TO REMEMBER/RECALL ALL THE FUNCTIONS)
#type .functioname() -> hover your mouse to understand the desc of the function
#type .functioname() -> press ctrl+mouse click to see the (abstracted) source code of the function and description
#ctrl+click further on the opened function to understand which are all the programs referring to it...
#How to understand and use a function?
#To understand we have to hover and go through the def of the function including the input/output/arguments
#To use the function go through the description of the function
employername="inceptez technologies {0} {1}"
#functions can be composable
modifed_employername=employername.format("pvt.","ltd.").capitalize()
employername="inceptez technologies"
print(modifed_employername)
joinword='inception'
print(employername.join(joinword))
print(employername.partition(' '))
a='Tanvi'
b=list(['inceptez-','-abc-','-xyz'])
print(a.join(b))
'''
Akalesh S P -> partition(" ") -> (Akalesh," ",S P)
'''
amt=60
print(str(amt).zfill(5))

amt='INR600'
print(amt.isalnum())
amt=' '
print(amt.isspace())
amt='100'
print(amt.encode('utf-8'))

employername=" inceptez technologies "
print(amt.strip())

employername=" inceptez technologies "
print(employername.strip())

employername="'inceptez technologies'"
print(employername.strip("'"))

employername="'inceptez' 'technologies'"
print(employername.replace("'","",2))

print(employername.__len__())
print(len(employername))

amt=100
print(amt.__lt__(500))
amt=-100
print(amt.__lt__(0))
if amt.__abs__().__eq__(amt):
    print("given value is positive")
else:
    print("given value is negative")

print(amt.__hash__())
print(abs(amt))

#bigquery -> abs(farm_fingerprint/uuid(column)) -> hash

#Day 5
print("Control Structures")
#if should be only once, elif can be multiples, else should be only once
print('I. Conditional Structure')
#What is the fundamental of conditional structure
print('simple/direct conditional structure')
curtime=11
if (curtime >=0) and (curtime<12.0):
    print("Good morning")

curtime=8
if (curtime >=0) and (curtime<12.0):
    print("Good morning")
elif (curtime >=12.0) and (curtime<17.0):
    print("Good afternoon")


curtime=19
if (curtime >=0) and (curtime<12.0):
    print("Good morning")
else:
    print("Good night")

curtime=19
if (curtime >=0) and (curtime<12.0):
    print("Good morning")
elif (curtime >=12.0) and (curtime<17.0):
    print("Good afternoon")
else:
    print("Good night")

#Bitwise operators & logical operators are same
# (bit-wise not preferred much, because of performance challenges)
curtime=8.30
if (curtime >=0) & (curtime<12.0):
    print("Good morning")
elif (curtime >=12.0) & (curtime<17.0):
    print("Good afternoon")
else:
    print("Good night")

#brain works!!
#vel (traffic)-> guindy -> ashok pillar
#vel (traffic)-> pallavaram -> ashok pillar
#vel (traffic/no traffic) -> saidapet -> ashok pillar

#Ternary operator
curtime=8.30
salutation="Good morning" if (curtime >=0) & (curtime<12.0) else "Good night"

#Realtime simple usecase for if else
#greatest of 2 numbers
num1=30
num2=20
if num1>num2:
    print("num1 is greater",num1)
else:
    print("num2 is greater", num2)

#greatest or equivalent of 2 numbers
num1=30
num2=30
if num1>num2:
    print("num1 is greater",num1)
elif num1.__eq__(num2):
    print("num1 and num2 are same",num1,num2)
else:
    print("num2 is greater", num2)

print('Complex/Nested conditional structure')
#First write a psedo code that covers all possible combination of the results,
# if we anticipate some more conditions can be added in the later, create a placeholder for that using "pass"
print("Choose the option for upcoming or ask")
popup=input()
#ask,upcoming
if (popup=='upcoming'):
    print("Choose the option for DE Weekday or DE Weekend")
    popup_option=input()
    if popup_option=='DE Weekday':
        print("Timing 7 AM to 9 AM")
    elif popup_option=='DE Weekend':
        print("Timing 9 AM to 2 PM")
    else:
        print("Wrong option chosen, dont do anything, como out of the iteration")
elif (popup=='ask'):
    print("Choose the option for email communication or phone communication")
    popup_option=input()
    if popup_option=='email':
        print("sending the email to Inceptez")
        mail=input()
    elif popup_option=='phone':
        print("sending the phone number")
        phone=int(input())
else:
    print("choose either upcoming or ask")

#Greatest of 3 numbers (with or without nested conditions)
a,b,c=10,20,20
print(max(list([a,b,c])))


#Greatest or equivalent of all 3 numbers
a,b,c=10,20,20
#print("max is ",max(list([a,b,c])))


#Greatest or equivalent of all 3 numbers
a,b,c=10,20,30
'''
Pseudo code: greatest among the 3 numbers
a>=b and a>=c -> a is greater
b>=a and b>=c -> b is greater
c>=a and c>=b -> c is greater
'''

'''
Pseudo code: greatest among the 3 numbers or equivalent of all 3 numbers
a==b and b==c -> all 3 are same
a>=b and a>=c -> a is greater
b>=a and b>=c -> b is greater
c>=a and c>=b -> c is greater
'''
a,b,c=30,20,30
#bit costly, comparing with the nested condition
#common approach, better in readability
if a==b and a==c:
    print("all are same a,b,c",a,b,c)
elif a>=b and a>=c:
    print("Max value is a", a)
elif b>=a and b>=c:
    print("Max value is b", b)
else:
    print("Max value is c", c)

#or
#smart approach
if a==b and a==c:
    print("all are same a,b,c",a,b,c)
else:
    print("Max value is ", max(list([a,b,c])))

#Greatest of 3 numbers (without nested conditions)
a,b,c=30,35,40
if a>=b and a>=c:
    print("Max value is a", a)
elif b>=a and b>=c:
    print("Max value is b", b)
else:
    print("Max value is c", c)

#Greatest of 3 numbers (with nested conditions)
a,b,c=60,60,60
#usha's code
#optimized approach
if (a==b) & (a==c):
    print('All 3 are same {0},{1},{1}'.format(a,b,c))
elif(a>b):
    if(a>c):
        print('{0} is greatest'.format(a))
    else:
        print('{0} is greatest'.format(c))
else:
    if(b>c):
        print('{0} is greatest'.format(b))
    else:
        print('{0} is greatest'.format(c))

#Selva's Code
#comprehensive approach
#a, b, c = 10, 20, 20
if a >= b and a >= c:
    if a > b and a > c:
        print("a ({0}) is greater than b ({1}),c({2})".format(a, b, c))
    elif a == b:
        print("a ({0}) is equal to b ({1})".format(a, b))
    else:
        print("a ({0}) is equal to c({1})".format(a, c))
elif b >= a and b >= c:
    if b > a and b > c:
        print("b ({1}) is greater than a({0}),c({2})".format(a, b, c))
    elif b == a:
        print("b ({1}) is equal to a ({0})".format(a, b))
    else:
        print("b ({0}) is equal to c ({1})".format(b, c))
else:
    if c > a and c > b:
        print("c ({2}) is greater than a ({0}),b ({1})".format(a, b, c))
    elif c == a:
        print("c ({1})is equal to a ({0})".format(a, c))
    else:
        print("c ({1}) is equal to b ({1})".format(b, c))

#Day 6
print('J. Looping Constructs - How much explicitly the looping construct is Important in Function based programming - Not much important')
#Topics:
# Conditional looping/Un Conditional looping
# Entry controlled & Exit Controlled looping and infinate looping
# for, while, do while, break, continue, enumerate, else
# if condition for loop/while loop? Yes
# for loop/while loop followed by a if condition? Yes
#Looping is a recursion or iteration performed on group of elements or in a range of values for operating on multiple values or multiple times
#Realife example of looping - mon to friday going to office, until sunday i am going to office
#DE or DB Developers lif - DE/ETL Developer data ingestion/curation i am doing on hourly/daily basis., DB Developer - select statement will run loop in the background
#eg. table 100 rows -> select custid from table; -> for row in total_records: custid of a given row

#Python supports 2 types of looping constructs -> for and while loop (do while loop, python doesn't support)

#Looping is a recursion or iteration performed on group of iterable elements or in a range of values
# for operating on multiple values or multiple times
#loop
#word='irfan'
rangeofvals=list(range(0,10))
print(rangeofvals)
for val in rangeofvals:
    print(val+10)

print(list(map(lambda x:x,rangeofvals)))

#collection types: array/list, struct/tuple, map/dict, set

#For loop ->
# For loop is a looping construct used for iterating of iterable types (all collections + string are iterable in python)
# For loop doesn't know how many times the iteration is going to happen
# Mostly used looping construct is for loop

#1. Simple For loop
empsallist=list([10000,20000,30000,15000])
bonuspct=10
for sal in empsallist:
    finalsal=(sal)+(sal*bonuspct)/100
    print(f"final salary is {finalsal}")

#to operate on 2 lists empid and empsallist, we can't use in a single for loop iterating 2 lists as given below
#for eid,sal in empid,empsallist:
#Enumerate function will help us get the index and the value of a given list
#list(enumerate(empid))
#[(0, 100), (1, 101), (2, 110), (3, 112)] - list of tuples of 2 attributes
empid=[100,101,110,112]
empsallist=list([10000,20000,30000,15000])
bonuspct=10
for idx,eid in enumerate(empid):
        sal=empsallist[idx]
        finalsal=(sal)+(sal*bonuspct)/100
        print(f"finalsalary of employee {eid} is {finalsal}")

#2. Nested Loops:
#College wise subjects for Engg Sem1
collegelst=["SRM","SVN"]
subjectlst=["Engg Mat","Engg Eng","Engg Drawing"]
sectionlst=["A","B","C"]
for coll in collegelst:
    for sub in subjectlst:
        for sec in sectionlst:
            #dictionarypairs=dict(coll,sub)
            print(f"{coll} is taking {sub} for section of sec {sec}")

#Building Tables using Python program
#2 x 1=2
#2 x 2=4
#2 x 3=6
#.
#.
#2 x 10=20
tablevalue=list(range(2,21))
maxvalues=list(range(1,11))
for i in tablevalue:
    for j in maxvalues:
        print(f"{i} x {j} = ",i*j)

#With Break Statement
tablevalue=list(range(2,21))
maxvalues=list(range(1,11))
print("input 2 to 20 tables")
maxtablevalue=int(input())
for i in tablevalue:
    for j in maxvalues:
        print(f"{i} x {j} = ",i*j)
    if i==maxtablevalue:
        break

#Day 7
#looping constructs - for, while, else, do while, break, continue, if elif else - pass
#Break - Break is used to terminate the loop if a condition is met. Note: For loop cannot applied with any condition
statelst=['TND','AND','GOA','MUM','PON','KOL']
for state in statelst:
        print(f"State is {state}")

#identify what are the union territories in this list of states we have
#in in SQL databases
statelst=['TND','AND','GOA','MUM','PON','KOL']
for state in statelst:
    if state =='GOA' or state =='PON':
        print(f"union territory is {state}")
    print("program is further executing if i don't use continue on all the states")
    print(f"Loop is iterated for all states and territory {state}")

#identify whether we have atleast one union territory in this list of states of not
#exists in SQL databases
statelst=['TND','AND','GOA','MUM','PON','KOL']
for state in statelst:
    if state =='GOA' or state =='PON':
        print(f"union territory is present {state}")
        break

#Continue - Continue will help us stop the execution of the given iteration and continue with the next iteration
#Eg. Apply tax for only regular states and no tax for union terriory
#exists in SQL databases
#break in the below eg. will break the loop and come out of the loop (skipping MUM, PON, KOL) when GOA is reached.
#continue in the below eg. will continue the loop further for ('TND','AND','MUM','KOL') by skipping GOA and PON.
statelst=['TND','AND','GOA','MUM','PON','KOL']
statetax=18
for state in statelst:
    if state =='GOA' or state =='PON':
        print(f"Tax is not applicable for this states {state}")
        #break
        continue
    #else:
        #print(f"Tax is applicable for this states {state}")
    print("program is further executing if i don't use continue")
    print(f"Tax is applicable for only these states {state}")
a=5
b=2
if a>=b:
    pass
else:
    print("else statement")

#While loop -> while loop is an another looping construct used for iterating based on the condition(s)
# Two types of while loops are there (entry controlled/exit controlled)
#entry controlled loop - Loop will execute n number of iterations when the condition is met (it may leads to infinate looping if the condition is meeting always)
# or loop will not do any one iteration if the condition is not met
# Eg. while can be used to run the loop infinately, to some number of iteration as per our need.
# Realtime Eg. of while loop ->
# Application -> close all DB connections (loop and retry few times to gracefully close the connection otherwise terminate it)
#else is optional
strt=1
end=3
while strt<=end:
    print("trying to close the connection gracefully for iteration ",strt)
    strt=strt+1

#else can be used in while loop in Python programming.
#else will be executed post the while loop (condition is not met) reached the maximum iteration , below eg. when strt=4 the else part of while will run.
strt=4
end=3
while strt<=end:
    print("trying to close the connection gracefully for iteration ",strt)
    strt=strt+1
else:
    print("close the connection forcefully")

#Our daily life we are using while loop when we use our PC?
#usage of passwords
# [hduser@localhost data]$ sudo hduser
# [sudo] password for hduser:
# Sorry, try again.
# [sudo] password for hduser:
# Sorry, try again.
# [sudo] password for hduser:
# Sorry, try again.
# sudo: 3 incorrect password attempts
# login functionality in Python?
#variables 3 - start, ending, storedpassword, password, username
#entry controlled, break
####################################All our Aspirant's code:###########################
#Sonam's Code
username= input("Enter the username \n")
actualpassword='hduser'.encode()
start=1
usernamelist= ["hduser", "sonam", "hduser1"]
while start<=3:
        password= input("password is :")
        if usernamelist.count(username) and actualpassword == password:
            print("login successful")
            break
        elif actualpassword != password:
              print("sorry maximum attempts reached")
        else:
              print("Wrong user")

#Tanvi's Code
username=input("Enter user name:\n")
userlist=["hduser","hduser1"]
savedpwd="hduser".encode()
validuser,validpwd=False,False
while True:
    if userlist.count(username) and not validuser:
        print(f"User {username} exists!")
        validuser=True
        for i in range(3):
            print(f" Attempt #{i+1}, Enter password:")
            pwd = input().encode()
            if pwd.decode() == savedpwd.decode():
                print("Login successful!")
                validpwd=True
                break
        if not validpwd:
            print("Max attempts reached. Access denied!")
        break
    elif not userlist.count(username):
        print(f"User {username} is not valid! Please enter valid credentials.")
        break

#Tarun's code
username ="Irfan"
Passowrd = "Password123"
userID =input("enter the username")
if userID == username:
    i=1
    while i <= 3:
        passcode = input("enter the Password")
        if (passcode == Passowrd):
            print("logged in")
            break
        elif (i ==3):
            print("sorry you have reached maximum tries.")
            break
        else:
            print("wrong password try again")
            i +=1
else:
    print("userid not valid")


#Mage's code
username =input("[hduser@localhost data]$ ")
userpass =input(f"[sudo] password for {username}:")
attend =1
savepass ='hduser'.encode()
while attend <=3:
     if savepass == userpass.encode():
         print("Welcome To Our Linux file system for  Batch WD32")
         break;
     elif attend ==3:
         print("Sorry, try again.")
         print(f"sudo: {attend} incorrect password attempts")
         break
     else:
         print("Sorry, try again.")
         userpass=input(f"[sudo] password for {username}:")
         attend+=1

#Selva's code
User_Name = input("hduser@localhost ~ : sudo \n")
sudoUserName = ['selva', 'irfan','inceptez']
atmt = 0
final_atmt = 2
while True:
    # print("sudo user login")
    if sudoUserName.count(User_Name):
        password = input("[sudo] password for hduser:\n")
        passwordList = ['selva123','irfan123', 'inceptez123']
        idx = sudoUserName.index(User_Name)
        if passwordList[idx] == password:
            # print(f"{passwordList.decode()},{password.decode()}")
            print("Sudo User logged in successfully")
            break
        elif final_atmt > atmt :
            atmt = atmt+1
            # print(f"{passwordList.decode()},{password.decode()}")
            print("sorry,try again.")
        else:
            print("3 in correct password attempts ")
            break
    else:
        print("wrong username info")
        break

#Usha's code
#login functionality in Python
username = input('Enter the username to login as sudo user: ')
count=1
actual_pwd='hduser'.encode()
while(count<=3):
   password = input(f'[sudo] password for {username}: ').encode()
   if(password.decode() == actual_pwd.decode()):
       print('Login successful')
       break;
   else:
       count = count + 1
       print('Sorry, try again.')
else:
    print('sudo: 3 incorrect password attempts')

#Chanakya's code
pas ="123"
tries = 0
while tries < 3:
    pasw = input()
    if pas == pasw:
        print("Authenticated")
        break
    else:
        tries += 1
        if tries == 3:
            print("maximum tries exhausted")
        else:
            print("try again")

#Lakshmi's code
username=input("Enter username:")
st=1
end=2
while True:
    if username=="sudo hduser":
        print("The given username is correct")
    elif username != "sudo hduser":
        print("incorrect username")
        break
    password = input("[sudo] password for hduser:")
    if password == "hduser":
        print("Password is correct, login successful")
        break
    elif st<=end:
        print("Sorry, try again.")
        st=st+1
    else:
        print("sudo: 3 incorrect password attempts")
        break
#######################################################################################

#Do While loop - First allow the loop to execute atleast once, then do the conditional check and then decide to further run the loop or not
strt=1
end=3
while True:
    print("DO-> allowed for the first time at any cost")
    if(strt<=end):
        print("While -> continuing the loop")
        strt+=1
    else:
        break

#Wanted to implement the sudoer command logic of linux in python
username=input("Enter the username\n")
sudoerlist=["hduser","hduser1"]
storedpasswd='hduser'.encode()
strt=1
end=2
sudoind=0
while True:
    print("Allowing the user to do sudoer operation at any cost")
    print("""We trust you have received the usual lecture from the local System
             Administrator. It usually boils down to these three things:""")
    if sudoerlist.count(username) and sudoind==0:
        print(f"given user {username} is a sudoer, i can further proceed with him")
        sudoind=1
    elif not(sudoerlist.count(username)) and sudoind==0:
        print(f"{username} is not in the sudoers file.  This incident will be reported.")
        break
    passwd = input("enter the password\n").encode()
    if storedpasswd.decode()==passwd.decode():
        print(f"given user {username} is allowed to perform this operation")
        break
    elif strt<=end:
        print(f"Try another time {strt}")
        strt=strt+1
    else:
        print(f"Max attempt is reached, hence terminating {strt}")
        break

#Day 8
print('K. Collection Types')
#Application of using some of the collection types in realtime world?
#{"process":"ETL Process1","source":["hive","Bigquery"],"target":["HDFS","GCS"],"cols":["custid","upper(custname) as upper_custname"],"tablename":"customer","where":"(city='chennai')","gcs_uri":"gcs://abc/xyz_bucket/"}
import json
openfile=open("/home/hduser/sparkdata/file2.json",'r')
readjsonfile=json.load(openfile)
cols=readjsonfile['cols']
query='select '+cols[0]+','+cols[1]+' from '+readjsonfile['tablename']+' where '+readjsonfile['where']+';'
sources=readjsonfile["source"]
type(sources)
for i in sources:
 print(f"running the query {query} on the db of {i}")
 print(query)

#Hive - array, stuct, map
#Python - list, tuple, dictionary, set, string
#What is collection type?
#########################
# Group/collection of values/items/element/attributes organized in some simple/complex way
#Eg. List homogeneous collection contains group of simple/collections organized in a form of indexed sequenced fashion
#in a DB table perspective list is equivalent to column value
a=10
print(a)
#       idx:0,val:10k  idx:1,val:20k
sal_lst=[10000,20000]
#or
sal_lst=list([10000,20000])
print(sal_lst)
#Eg. tuple hetrogeneous collection contains group of simple/collections organized in a form of indexed sequenced fashion
#in a DB table perspective tuple is equivalent to a row contains multiple columns
emp_lst=tuple((1,'Irfan',sal_lst))
print(emp_lst)
#Eg. Dictionary key,value pair collection contains group of simple/collections organized in a form of list(key,value) pair fashion
#in a DB table perspective dict is equivalent to columnname and its value or it can be an associative values or it can be help us achive lookup operation
emp_sal_dict=dict({1:'Irfan',2:'Prem'})
emp_details_dict=dict({1:('Irfan',41),2:('Prem',35)})
cust_transdetails_dict=dict({1:[41,55,80],1:[35,50]})
print(emp_sal_dict)
#Eg. Set Iterable homogeneous collection contains group of simple/collections organized in a form of deduplicated/unique and ordered elements types used mainly for performing set operations
#in a DB table perspective dict is equivalent to deduplicated ordered column values stored for performing set operations like union, difference, intersection etc.,
#       idx:0,val:1  idx:1,val:2
empid_set={1,2,5,3,4,1}
print(empid_set)

#collection types - list, dict, tuple, set

######What are the topics we have learn in collection types#######
#all the coll types in python is iterable (can be looped)
#Notation, access, resizable/mutable/immutable?,  insert/update/delete, functions to apply
#Application of the collection types

#The indexed-sequenced/named/iterable collection of homogeneous/hetrogeneous data types of
# elements/items/keys/values which can support iterations
# if we have more than one dimension of value stored in a variable we call it as collection.
# Refer the pdf document for more details... from page 18 onwards..

#Why we need collection types?
#To manage complex dataset in a hirarchical structure stored, to process semi structure data, nested data, dynamic schemaful data..

#different notations we use?
# list[],dict/set{},tuple()

#different types of collection types?
#sequence/iterable (str,tuple,list...), mapping type(dictionary)

#category of collection types
#mutable/immutable

#functions applied?
#we are going to see in detail

#Collection Types: complex data types
#iterable or non-iterable - mutable/immutable

#python-hive
#list - Array (duplicated list)
#Dictionary - Map
#Tuple - Struct
#set - Array (de duplicated list)

#Day 9
print("List type in python (PRIORITY1)")
#Notation: []
#Accessed using ? index starting from 0 ending with len(list)-1 or just put -1
#Definition
#indexed-sequence collection of homogeneous elements/attributes/items/values/object
sal_lst=[10000,20000,40000,30000]
print("list operations")
#List can be hetrogeneous too (but not suggested, because python is a stongly typed language)
sal_lst=[10000,20000,40000,30000,'15000']

#All the python collections are iterable
for sal in sal_lst:
    print(int(sal)+1000)

#select/access
sal_lst=[10000,20000,40000,30000,15000]
#accessed using the index, loops, functions like map/filter/max/sum
print("accessing using index ",sal_lst[0])
for sal in sal_lst:
    print("accessing using loop ",int(sal)+1000)
print("accessing using functions ",max(sal_lst))

#insert/update/delete
#append in the last (proves list is mutable/resizable/can be inserted)
sal_lst.append(45000)
print("sal_lst after appending",sal_lst)

#insert in the index position
sal_lst.insert(2,35000)
print("sal_lst after inserting in an index of 2",sal_lst)

#update the list elements (mutable)
sal_lst[1]=25000
print("sal_lst after updating in an index of 1 from 20000 to 25000",sal_lst)

sal_lst[1]=25000
print("sal_lst after updating in an index of 1 from 20000 to 25000",sal_lst)

sal_lst[1:4]=[25000,45000,35000]
print("sal_lst after updating multiple elements in a range of values",sal_lst)

#delete the elements of the list using value
#pop (delete) the elements of the list using index
print(sal_lst.pop(1))
print("sal_lst after popping out a given index element",sal_lst)
#search for a value with in the given index (range) value and pop(remove) it
sal_lst=[10000, 45000, 35000, 15000,45000]
sal_lst.remove(45000)
print("sal_lst after removing out a given element",sal_lst)
sal_lst=[10000, 45000, 35000, 15000,45000]
for i in sal_lst:
 if i==45000:
  sal_lst.remove(i)
print("sal_lst after removing out first occurance of the given elements",sal_lst)

#search for a value with in the given index (range) value and remove all the occurances (not the first occurance alone)
sal_lst=[10000, 45000, 35000, 15000,45000]
for i in sal_lst:
    if i == 45000:
     sal_lst.pop(sal_lst.index(i))
print("sal_lst after removing out all occurances of the given elements",sal_lst)

#search for a value with in the given index (range) and update with some other value
sal_lst=[10000, 45000, 35000, 15000,45000]
for idx,val in enumerate(sal_lst):
    if val == 45000:
     sal_lst[idx]=val+1000
print("sal_lst after updating all salary of 45000 with 45000+1000",sal_lst)

#Day 9
#Day 9
#certain builtin functions to try out
#sorting the list
sal_lst=[10000, 45000, 35000, 15000,45000]
sal_lst.sort()
print(sal_lst)
print(sal_lst.count(45000))
sal_lst1=sal_lst.copy()
sal_lst.extend(sal_lst1)
sal_lst.sort()
sal_lst.reverse()
print(sal_lst)
sal_lst.clear()
print(sal_lst)

print("Tuples (immutable) - () - similar to Scala")
#Syntactically python and scala are same
#semantically - tuples in scala is not iterable and the position of elements starts from 1, access using _position
#semantically - tuples in python is iterable and the position of elements starts from 0, access using [0]
#Tuple - Notation () is used to load row/recordset from a given table, hetrogeneous type, immutable, iterable, accessed using indexes

emp_tup=(1,'Mage',10000,'Chennai')

print("Tuple looping is possible in python and it proves tuple is added in sequence hierarchy in python - We don't use it regulary")
for i in emp_tup:
    print(f"values of the record is {i}")

print('tuple starts with zero index {0} - Use this regularly')
print('First column value of the given row is {0}'.format(emp_tup[0]))
col1=emp_tup[0]
print(f'First column value of the given row is {col1}')
print(f'First column value of the given row is {emp_tup[0]}')
print(f'Second column value of the given row is {emp_tup[1]}')
print(f'Third column value of the given row is {emp_tup[2]}')

print("tuple doesn't support any add/update/delete operation")
#update will not work naturally
#emp_tup[1]='Magendiran'
#Delete or Add is not possible naturally
print(f"exiting tuple {emp_tup}")
print(emp_tup.__add__(emp_tup))
print(f"added tuple will not really get added {emp_tup}")

print('What is the Workaround (if a functionality is not directly available, still how can we achieve the same func with some other options)?')
#1. Either recreate the given tuple applying the functionalities
emp_tup=emp_tup.__add__(emp_tup)
#2. Other Workarounds to perform all mutable operation on a tuple
emp_tup=(1, 'Mage', 10000, 'Chennai', 30, 'SSE')
print(f"Original Tuple {emp_tup}")
emp_tup_lst=list(emp_tup)
#[1, 'Mage', 10000, 'Chennai', 30, 'SSE']
emp_tup_lst[1]='MAGE'
emp_tup_lst.pop(2)
emp_tup=tuple(emp_tup_lst)
print(f"final Tuple {emp_tup}")

print("Dictionaries (mutable) - {k:v, k:v}")
# When to go for tuple and when with dictionary - its equivalent to the tradeoff between csv and json / sql(mysql) vs nosql(hbase/es)
# Tuple - index/Positional access, storing fixed number of unbounded elements (type and the name are not bounded), eg. fixed fields records
# dictionary - key based access, variable number of bounded elements (type and name are bounded) eg. dynamic fields records
print("Dictionaries in python is Map in scala map in hive")

emp_dict={"empid":1,"name":"Venu","salary":10000}
print(f"Original Dictionary {emp_dict}")
#Adding Items - if the key is not found
emp_dict.update({"city":"Chennai"})
print(f"City added Dictionary {emp_dict}")
#Updating Items - if the key repeats
emp_dict.update({"city":"Mumbai"})
print(f"City updated Dictionary {emp_dict}")

#Removing an Item
#Delete the given key
emp_dict.pop("name")
#Delete the last element of a dictionary
emp_dict.popitem()
#Delete all the elements of a dict
#emp_dict.clear()
print(f"City updated Dictionary {emp_dict}")

#Iteration of Dictionary
emp_dict={"empid":1,"name":"Venu","salary":10000}
#Iterate on the items of the Dict - will return list of tuples
for key,value in emp_dict.items():
    print(key,'=',value)

#Iterate on the keys of the Dict
for key in emp_dict.keys():
    print(key)
#Iterate on the values of the Dict
for value in emp_dict.values():
    print(value)

#Some additional functions
print(emp_dict.items())
print(emp_dict.values())
print(emp_dict.keys())
emp_dict1=emp_dict.copy()

print("Set (mutable) - Notation {} - Set is a sorted and distinct collection of iterable elements, cannot be accessed using index "
      "because we can't anticipate the same order or values present in a set to access using the index")
cid_set1={1,2,5,4,10,4}
cid_set2={1,2,5,4,10}

#how to access the element of a set (cant be access directly by using index/key/values)- Index can't be used
set3={2}
cid_set1.issuperset(set3)

#set is iterable
for i in cid_set1:
    if i==4:
        print(i)

#set is mutable (updatable)
cid_set1={1,2,5,4,10}
#add will help add/update an element not the set
cid_set1.add(5)
set3={11}
#update will help add/update another set
cid_set1.update(set3)
#set is mutable (resizable)
cid_set1.add(6)

#set is mutable (resizable) - Removing/popping/cleaning
cid_set1.remove(5)
cid_set1.pop()
cid_set1.clear()

#set is supported with set operation
print("common elements between 2 sets",cid_set1.intersection(cid_set2))

#Day 10
cid_set1={1,2,5,4,10,4}
cid_set2={1,2,5,3,11}
print("output will be displayed by like common elements removed from the first set",cid_set1.difference(cid_set2))
print("no update happened in the first set",cid_set1)
print("Actually the first set will be updated with the result of difference",cid_set1.difference_update(cid_set2))
print("update happened in the first set",cid_set1)

cid_set1={1,2,5,4,10,4}
cid_set2={1,2,5,3,11}
print("output will be displayed by like both set values are merged, deduplicated & sorted",cid_set1.union(cid_set2))

cid_set1={1,5}
cid_set2={1,2,5,3,11}
print("Check whether the set1 is a subset of set2 ie: if set1 contains all matching elements of set2",cid_set1.issubset(cid_set2))

cid_set1={1,2,5,4,10,4}
#cid_set2={1,2,3,11}
cid_set2={1,2}
print("Check whether the set1 is a superset of set2 ie: if set2 contains all matching elements of set1",cid_set1.issuperset(cid_set2))

cid_set1={1,2,5,4,10,4}
cid_set2={1,11,12,13}
print("Return true if both the sets are not having any one of the matching elements",cid_set1.isdisjoint(cid_set2))

cid_set1={1,2,5,4,10,4}
cid_set2={3,2,5,11,12,13}
print("Display Difference between both two sets vice versa",cid_set1.symmetric_difference(cid_set2))
print("Update (in the first set) the Difference between both two sets vice versa",cid_set1.symmetric_difference_update(cid_set2))

#Pls practice on this today:
print(" Accessing the nested complex types")

#{"results":
# [{"gender":"male","name":{"title":"Mr","first":"Lucas","last":"Gallardo"},"location":{"street":{"number":49,"name":"Ronda de Toledo"},"city":"Bilbao","state":"Navarra","country":"Spain","postcode":72759,"coordinates":{"latitude":"-24.1241","longitude":"-42.9993"},"timezone":{"offset":"+5:45","description":"Kathmandu"}},"email":"lucas.gallardo@example.com","login":{"uuid":"a4c0f1db-35ef-43b9-9d23-b1da970f4876","username":"blackduck720","password":"spank","salt":"ov40nTLe","md5":"2d2a37e544c2423dabd30e45b04d01de","sha1":"2c6398b2cd82becb356a624b661978c9c0ae699c","sha256":"e26278657a9c3d9b17572dd14c75e402deebef7ff25600981c923a8e0b307759"},"dob":{"date":"1951-01-05T20:37:44.406Z","age":71},"registered":{"date":"2016-09-08T07:29:59.842Z","age":6},"phone":"954-092-544","cell":"671-763-895","id":{"name":"DNI","value":"97111064-H"},"picture":{"large":"https://randomuser.me/api/portraits/men/65.jpg","medium":"https://randomuser.me/api/portraits/med/men/65.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/65.jpg"},"nat":"ES"}
# ,{"gender":"female","name":{"title":"Mrs","first":"Elisa","last":"Gallardo"},"location":{"street":{"number":49,"name":"Ronda de Toledo"},"city":"Bilbao","state":"Navarra","country":"Spain","postcode":72759,"coordinates":{"latitude":"-24.1241","longitude":"-42.9993"},"timezone":{"offset":"+5:45","description":"Kathmandu"}},"email":"lucas.gallardo@example.com","login":{"uuid":"a4c0f1db-35ef-43b9-9d23-b1da970f4876","username":"blackduck720","password":"spank","salt":"ov40nTLe","md5":"2d2a37e544c2423dabd30e45b04d01de","sha1":"2c6398b2cd82becb356a624b661978c9c0ae699c","sha256":"e26278657a9c3d9b17572dd14c75e402deebef7ff25600981c923a8e0b307759"},"dob":{"date":"1951-01-05T20:37:44.406Z","age":71},"registered":{"date":"2016-09-08T07:29:59.842Z","age":6},"phone":"954-092-544","cell":"671-763-895","id":{"name":"DNI","value":"97111064-H"},"picture":{"large":"https://randomuser.me/api/portraits/men/65.jpg","medium":"https://randomuser.me/api/portraits/med/men/65.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/65.jpg"},"nat":"ES"}]
# ,"info":{"seed":"1934b3808d5cc6aa","results":1,"page":1,"version":"1.3"}}

#complextup: Tuple[int, str, List[Dict[str, [str, Dict[str, str]]], Dict[str, [str, Dict[str, str]]], Dict[str, [str, Dict[str, str]]], Dict[str, [str, Dict[str, [str, bool]]]]]]] = (1,...

print("Complex Tuple2 - tuple(familyid:int,familyname:str,familymembers:list[dict{k:v,k:v,k:dict{k:v,k:v}}])")
#Understanding the complex type:
#StructType in spark
#Tuple(int,str,list(
# dict(str:str,str:str,str:dict(str:str,str:str))))
# dict(str:str,str:str,str:dict(str:str,str:str)))
# dict(str:str,str:str,str:dict(str:str,str:str,str:str)))
# dict(str:str,str:str,str:dict(str:str,str:str,str:bool)))
complextup=(1,
            "Madison's Family",
            [{"gender":"male","Relation":"self","personalinfo":{"title":"Ms","name":"Madison"}},
             {"gender":"female","Relation":"spouse","personalinfo":{"title":"Mrs","name":"Elisa"}},
             {"gender":"female","Relation":"daughter","personalinfo":{"title":"Miss","name":"Hanna","hobby":"book reading"}},
             {"gender":"male","Relation":"son","personalinfo":{"title":"Master","name":"Dave","schooling":True}}])

print("id is ",complextup[0])
print("Family name is ",complextup[1])
print("gender of first list element is ",complextup[2][0]["gender"])
print("relation of first list element is ",complextup[2][0]["Relation"])
print("personalinfo of the first list element is ",complextup[2][0]["personalinfo"])
print("personalinfo title of the first list element is ",complextup[2][0]["personalinfo"]["title"])
print("personalinfo name of the second list element is " ,complextup[2][1]["personalinfo"]["name"])
print("personalinfo hobby of the third list element is " ,complextup[2][2]["personalinfo"]["hobby"])
print("personalinfo schooling info of the fourth list element is " ,complextup[2][3]["personalinfo"]["schooling"])

#Simple use case of our real life:
#Wanted to recap Conditional structure, Operators(all operators - assignment, relational, logical/bitwise, arithmetic, unary, binary, ternary), Collection Types
# Swiggy Offer Usecase: Offer with max discount of 100 rupees or 10% which ever is lower.
# eg. If I buy products for 1500 rupees, 10% is 150 but max offer that can be given is 100
# otherwise If I buy products for 500 rupees, 10% is 50 max offer that can be given is 50
# Use appropriate collection type to assign & access percentage, minimum eligibility for offer as 500 rupees and maximum cutoff as 100 rupees
company_fixed_value_march={"max_off":100,"off_pct":10,"min_puchase":500}
cart_amt=300

#Psedo code
#1. Whether the min_purchase is meeting the offer requirement
#if cart_amt > min_purchase - offer required..
#2. Check whether cart_amt>min_purchase -> then eligibility starts to apply offer (write inside nested condition)
# off applied on the cart_amt is greater than max_off provided then conclude to reduce max_off on the cart_amt
#3. else reduce off_pct calculated on the cart_amt
#4. else - no offer required : final amt =cart_amt

#if cart_amt > min_purchase -> continue the program
    # nested if condition cart_amt is greater than max_off
    # nested else reduce off_pct calculated on the cart_amt
# else no eligibility

