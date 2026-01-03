#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.'''

''' movies=[] 
favmovie1 = input("enter your first favorite movie")
favmovie2 = input("enter your first favorite movie")
favmovie3 = input("enter your first favorite movie")
movies.append(favmovie1)
movies.append(favmovie2)
movies.append(favmovie3) '''

# '''another way '''
'''
movielist = [favmovie1,favmovie2,favmovie3]
print(movielist)
print(movielist[2])
print(movies)'''

# dictonary and set 
# Store following word meanings in a python dictionary :
# table : “a piece of furniture”  “list of facts & figures” cat : “a small animal”

'''dict_1 = {
     "table": ["a pice of table","list of fact& figures"],
     "cat" : "a small animal"}
 print(dict_1) '''

#

#You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students. python ,java,c++,python,javascript,java,python,java,c++,c

'''subject = {"python","java","c++","pyhton","javascript","java","python","java","c++","c"}
print(subject)
print(len(subject))
print("number of classroom need for student ",len(subject)) '''


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

'''
subject = {}
eng_marks = int(input("enter the marks of english"))
subject.update({"english": eng_marks})
che_marks = int(input("enter the marks of chemistry"))
subject.update({"chemistry":che_marks})
phy_marks = int(input("enter the marks of physicd")) 
subject.update({"physics":phy_marks})
another way 
 subject["eng_marks"] = eng_marks
 subject["che_marks"] = che_marks
 subject["phy_marks"] = phy_marks
print(subject) '''


# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
'''
valus = {9 ,9.0,"9.0"}
print(valus) 
# want to given values print separate. first we can store consider as string 
#use build in data type
valus = {
    ("float",9.0),
    ("int",9)
}
print(valus) '''
 

# num2 = int(input("enter the number "))
# factorial = 1
# for i in range(1 , num2+1):
#     factorial*=i
#     i +=1
# print(factorial)
    

# SWAP OF TWO VARIBLE (exchange)

# '''a = int(input("enter the number 1"))
# b = int(input("enter the number 1"))
# a = a+b
# b = a-b
# a = a - b
# print("A",a , "B",b)'''

# def swap_variables(a, b):
#     temp = a
#     a = b
#     b = temp
#     return a, b

# a = float(input("Enter the first variable: "))
# b = float(input("Enter the second variable: "))

# print("Before swapping:")
# print("a =", a)
# print("b =", b)

# a, b = swap_variables(a, b)

# print("After swapping:")
# print("a =", a)
# print("b =", b)


# Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 


# tuple_t1 = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# i = 0
# x =4

# while(i < len(tuple_t1)):
#     if tuple_t1[i] == x:
#      print("x at index",i)
#      break
#      i +=1


#practice loop
# fruits = ["apple","banana" ,"orange" ," graphes", " cherry" ,"strawberries"]
# for i in fruits:
#     print(i.upper())
#     print(i.lower())


# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 150:
#         continue
#     print(i)


#Write a Python program to count the total number of digits in a number using a while loop.

'''number = 545986
count = 0
while number != 0:
      number //= 10 # number = number // 10 
      count += 1

print(count)'''

# print("the count number is",len(str(number)))

"""n = 123
count = 0
Loop iteration 1:
n = 123 // 10 = 12
count = 1
Loop iteration 2:
n = 12 // 10 = 1
count = 2t
Loop iteration 3:
n = 1 // 10 = 0
count = 3
Loop exits since n = 0
count = 3 is returned as the total number of digits."""


''' system_info

import sys
print(sys.version)
print(sys.version_info)

import datetime
now = datetime.datetime.now()
'''

#** Write a Python program to display the first and last colors from the following list.


'''color_list = ["red","balck","green","blue"]
print("%s %s" % (color_list[0], color_list[-1]))
'''
#this

'''for i in color_list:
    if i ==color_list[0]:
        print(i)
    if i == color_list[len(color_list)-1]:
        print(i)
'''

# DICTIONARY IN PYTHON 

# info = {
#     "name":"lucus",
#     "age":17,
#     "city":"newyork",
#     "country":"usa"
# }
# new = info.get() 
# print(new)
     
# 1 import module as m  ''' import module and call .'''

'''import module as m
print(m._sum_())
'''
#2 import module

'''import module
print(module._sum_())
print(module._mul_())
'''
#3 from import module _sum_

from module import _mul_ , _sum_
print(_mul_())
print(_sum_())