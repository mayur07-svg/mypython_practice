#PYTHON SERIES

  #expression exicution...

# a,b=4,2
# txt ="@s"
# print(a*txt*b)

# c,d= 15,-7
# e=5.4
# txt2="@"
# print((c+d)*txt2)
# print(a*b+c*d)
# print(e/a)    #output as float..
# print(e*a)

# # # floor function
# print(a//c)
# print(d//c)
# print(c//d)
# print(c/d)

# name = "mayur"
# dgt = 56
# print((name+txt))

# # #write code about trafic rule 

# light = input("enter colour name ")
# if(light == "green"):
#     print("Go")
# elif(light=="red"):
#     print("stop")
# elif(light=="yellow"):
#     print("look at!")
# else:
#     print("light is broke")
    

 # STRING CONCEPT 
 
# str="i am learning python programing language from apna college,"
# str1="sharada mam teach us."
# print(str+str1)
# print(str[5])

# #SLICING. acessing part of string.
# print(str[5:16])
# print(str[3:13])
# print(str[:13])
# print(str[1:len(str)])

# #string function.
# str2=" hello guys'i am coder  now i am learn pyhton"

# print(str.endswith("der")) #returns true if string ends with substr
# print(str.capitalize()) #capitalizes 1st char
# print(str.replace("python","javascript")) #replaces all occurrences of old with new
# print(str.find("hello"))  #counts the occurrence of substr in string
# print(str.count("l"))  #counts the occurrence of substr in string


#  #Q7 WAP to input user’s first name & print its length.
 
# firstname = input("enter the name")
# print(len(firstname))

#Q8WAP to find the occurrence of ‘$’ in a String.

#list in python ("it is matuable")
marks = [87,95,89,90,99,97,]
print(marks)
print(len(marks))

#list slicing
 
print(marks[0])
print(marks[4])
print(marks[0:5])#ending idx is not included
print(marks[0:])
print(marks[:4])
print(marks[-3:-1])#ending idx is not included

#list method
list = [18,92,89,86]
list_add= list.append(98) #adds one element at the end.
print(list_add)# none as optput.
print(list)
list.sort() #sorts in ascending order.
print(list)
list.sort(reverse=True) #sorts in decending order.
print(list)
print(list.count(18))
list.reverse() #reverses list
print(list)
list.insert(2,99)
print(list)
 
#  SET IN PYHTON 

s1 = {12,45,8,9,56,1,3,5}
s2 = {"banana","orange","graphes","watermelon"}
# print(s1[2]) indexing does not posible in set to access the element.
# for i in s1
#     print(i)     # they give output in accending order
    
    # method 
    # 1> discart(); it remove specific element from the set.ifd same operation perform again it does not give error.
# s2.discard("graphes")
# print(s2)
# print(s2.discard("graphes"))


# # 2> remove() it remove specific element from the set.ifd same operation perform again it does give error.
# s1.discard(45)
# print(s1)

# #3 pop() it remove random element from the set.it does not need argument.
# s1.pop()
# print(s1)

# # 4 clear() it remove all element from the set.
# s1.clear()
# print(s1)
#  ADDING ELEMENT THE SET.


# 1> add() it is use to add single element in the set to anywhere.
# s1.add(89)
# print(s1)

# # 2> update() it is use to add multiple element in the set.
# s1.update([62,86,75])
# print(s1)
  
# FUNCTION IN SET.
# 1> UNION()         Combination of two set.
# 2>INTERSECTION()   it return common value from the both set.
# 3>ISSUPER SET()    it return only boolen value
# 4>ISSUBSET()       if all element of s2 are present in s1 then s2 is sunset of s1.
# 5>ISDISJOINT()       which have no commen element .

# set1 = {21,56,3,4,8,9} 
# set2 = {1,5,31,40,8,9,3} 
# set3 = {3,4,9}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.issuperset(set3))
# print(set3.issubset(set1))
# print(set1.isdisjoint(set3))
  
  
# TUPLE IN PYHTON

tup_1 = (1,2,5,9,8,3)
# print(tup_1[1])
# print(tup_1[1+2])

# accesing element using for loop.

l1 = len(tup_1)
for i in range(0,l1):
    print(tup_1[i])

print(tup_1[:])
print(tup_1[1:6])
print(tup_1[:6])
print(tup_1[4:])
print(tup_1[::5]) # five element skip from the tuple
print(tup_1[:-2])

 