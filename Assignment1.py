# #Q1
# print("Anything you find cool")

# #Q2.1
# a=12
# b=24
# print(a+b)

# #Q2.2
# a="Pine"
# b="apple"
# print(a+b)

# #Q2.3
# c=6
# d=" monkeys"
# print(str(c)+d)

# #Q3.1
# x=int(input("Enter the number: "))
# if(x>0):
#     print("number is positive")
# elif(x<0):
#     print("number is negative")
# else:
#     print("number is zero")

# #Q3.2
# y=int(input("Enter the number: "))
# if(y%2==0):
#     print("Number is even")
# else:
#     print("number is odd")

#Q4.1
# for i in range(1,11):
#     print(i)

# #Q4.2
# count=1
# while(count<11):
#     print(count)
#     count+=1

# #Q4.3
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

# Q5.1
# list1=[]
# print("Enter the numbers of the list: ")
# for i in range(0,5):
#     a=int(input())
#     list1.append(a)
# print(f"The minimum number is: {min(list1)}")
# print(f"The maximum number is: {max(list1)}")

#Q5.2
# dict={1:"english",2:"hindi",3:"maths"}
# print(dict)
# print(dict[1])

#Q5.3
# x=[2,6,3,9,4,1]
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)

#Q5.4
# d1={'k1':"first",'k2':"second",'k3':"third"}
# d2={'k4':"fourth",'k5':"fifth",'k6':"sixth"}
# d3=d1|d2
# print(d3)

#Q6.1
# x=input("Enter the string: ")
# count=0
# for i in range(len(x)):
#     if(x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u'):
#         count+=1
# print(f"The total number of vowels in this string is {count}")

#Q6.2
# x=input("Enter the string: ")
# y=x[::-1]
# print(y)

#Q6.3
# a=input("Enter the string: ")
# b=a[::-1]
# if(a==b):
#     print("the given string is a palindrome")
# else:
#     print("not a palindrome")

#Q7.1
# f=open("def.txt","w+")
# st="good morning"
# f.write(st)
# f.seek(0)
# data=f.read()
# print(data)

#Q7.2
# f=open("def.txt","a")
# a=" how are you? "
# f.write(a)
# f.close()
# f=open("def.txt","r")
# data=f.read()
# print(data)

#Q7.3
# f=open("def.txt","r")
# print(f"The number of lines in the file is: {len(f.readlines())}")
# f.close()

#Q8.1
# a=int(input("enter numerator: "))
# b=int(input("enter denominator: "))
# try:
#     if(b==0):
#         raise
#     else:
#         print(a/b)
# except:
#     print("cant divide by zero")

#Q8.2
# try:
#     x=int(input("enter the number: "))
#     print(x+3)
#     print("valid")
# except:
#     print("enter a number please")

#Q8.3
# x=int(input("enter a number to divide 20: "))
# try:
#     print(20/x)
# except:
#     print("cant divide by zero")
# finally:
#     print("done")

#Q9.1
# import random
# l=[]
# for i in range(5):
#     x=random.randint(1,100)
#     l.append(x)
# print(l)

#Q9.2
# import random
# x=random.randint(1,100)
# print(x)
# p=False
# for i in range(2,int(x/2)+1):
#     if(x%i==0):
#         print("not prime")
#         p=True
#         break
#     else:
#         p=False
# if(p==False):
#     print("number is prime")

#Q9.3
# import random
# x=random.randint(1,6)
# ch=int(input(("enter 1 to roll the die: ")))
# if(ch==1):
#     print(x)

#Q9.4
# import random
# l=[1,2,3,4,5]
# random.shuffle(l)
# print(l)

#Q9.5
# import random
# a=[1,"abc",2.34,5,67]
# q=random.choice(a)
# print(q)

#Q9.6
# import random
# pas=["1","2","3","4","5","6","7","8","9","0"]
# password=""
# x=int(input("enter the length of the password that you want: "))
# for i in range(x):
#     a=random.choice(pas)
#     password+=a
# print(f"the generated password is: {password}")

#Q9.7
# import random
# s=["diamonds","spades","hearts","clubs"]
# x=[2,3,4,5,6,7,8,9,10,"king","queen","jack","ace"]
# a=random.choice(s)
# b=random.choice(x)
# print(f"you got {b} of {a}")

#Q11.1
# import math
# x=int(input("enter the number whose square root to be found: "))
# print(math.pow(x,1/2))

#Q11.2
# from datetime import datetime
# a=datetime.now()
# date=a.strftime("%d/%m/%Y")
# time=a.strftime("%H:%M:%S")
# print("current date:",date)
# print("current time:",time)

#Q11.3
# import os
# print(os.listdir())
