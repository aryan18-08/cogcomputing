#Q1
# l=[10,20,30,40,50,60,70,80]
# l.append(200)
# l.append(300)
# l.remove(20)
# l.remove(30)
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)

#Q2
# scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
# a=max(scores)
# print(f"highest score is: {a} and its index is: {scores.index(a)}")
# b=min(scores)
# print(f"lowest score is: {b} and it occurs {scores.count(b)} times")
# s2=scores[::-1]
# print(list(s2))
# try:
#     a=scores.index(76)
#     print(a)
# except:
#     print("it is not present in the list")

#Q3
# import random
# x=[]
# for i in range(100):
#     a=random.randint(100,900)
#     x.append(a)
# d=0
# e=0
# f=0
# for i in x:
#     if(i%2==0):
#         d+=1
#         print(i)
# print(f"total even numbers are: {d}")
# for i in x:
#     if(i%2!=0):
#         e+=1
#         print(i)
# print(f"total odd numbers are: {e}")
# flag=False
# for i in x:
#     for j in range(2,int(i/2)+1):
#         if(i%j==0):
#             flag=True
#             break
#         else:
#             flag=False
#     if(flag==False):
#         f+=1
#         print(i)
# print(f"total prime numbers are: {f}")

#Q4
# A = {34, 56, 78, 90}
# B = {78, 45, 90, 23}
# print(A.union(B))
# print(A.intersection(B))
# print(A.difference(B))
# print(B.difference(A))
# print(A.issubset(B))
# print(B.issuperset(A))
# x=int(input("enter a score: "))
# if(x in A):
#     A.remove(x)
#     print(f"after removing the set A is: {A}")
# else:
#     print("this score is not present in A")

#Q5
# data = {"city": "New York", "population": 8419600, "area": 468.9}
# data["location"]=data.pop("city")
# print(data)