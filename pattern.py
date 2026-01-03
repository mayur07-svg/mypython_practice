#PATTERN
#Q1
# num  = int(input("enter the number of raw"))
'''for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
        
    print()'''  #NEXT LINE This will not return any value, but it will produce an empty line in the console. The function itself returns None.

'''num = int(input("enter the number of row"))
for i in range(num):
    for i in range(num,num+i+1):
        print("*",end=" ")
    print() '''
#Q 2

'''for i in range(1,num+1): 
    for j in range(1,num - i +1): 
        print("*",end=" ")
    print()
'''
 
#Q4
'''k = 1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("*", end=" ")
    k = k+2
    print()'''

# Q5

'''for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
'''
#Q6

'''for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()'''

#Q 7

'''for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    for j in range(0,num-i):
        print(end=" ")
    
    print()'''

#ANOTHER WAY

'''
for i in range(0,num):
    for j in range(0,num-i):
        print("*",end=" ")
    for j in range(0,i+1):
        print(end=" ")
    print()'''

#Q7
'''for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

for i in range(num,0,-1):
    for j in range(0,num-i+1):
        print(end=" ")
    for j in range(0,i-1):
        print("*",end=" ")
    print()'''


# ALPHABET PATTERN 
#Q A
'''for row in range(7):
    for col in range(5):
        if ((col == 0 or col == 4) and row != 0) or ((row ==0 or row ==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()'''

#Q B

'''for row in range(7):
    for col in range(5):
        if (col == 0 or col == 3) or ((row == 0 or row == 3 or row == 6) and (col<4 and col > 0)):
            print("*",end="")
        else:
            print(end=" ")
    print()'''

#Q3 C
 
'''for row in range(7):
    for col in range(5):
        if (col == 0 and (row != 0 and row !=6) ) or (col == 3 and (row != 1 and row !=2 and row != 3 and row != 4 and row !=5)) or (row == 0 or row == 6) and (col>0 and col<5):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
      
#4 D FOR PERFECT D HERE IS MISTAKAE I WILL CHECK IT.

'''for row in range(7):
    for col in range(5):
        if(col == 0) or (col == 4 and(row != 0 and row != 6)) or (row == 0 or row == 6 and (col > 0 and col < 4)):
            print("*",end="")
        else:
            print(end=" ")
    print()'''


#E
'''for row in range(7):
    for col in range(5):
        if(col == 0)or (col == 4 and(row != 1 and row != 2 and row != 4 and row != 5)) or (row == 0 or row == 3 or row == 6 and(col>0 and col < 4)):
            print("*",end="")
        else:
            print(end=" ")

    print()
'''
#F
'''for row in range(7):
    for col in range(5):
        if(col == 0)or (col == 4 and(row != 1 and row != 2 and row != 4 and row != 5 and row != 6)) or (row == 0 or row == 3 and(col>0 and col < 4)):
            print("*",end="")
        else:
            print(end=" ")

    print()'''

#G  after 
# for row in range(6):
#     for col in range(4):
#         if(col == 0) or (col == 2 or col == 3 and (row != 1 and row != 2)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

#H
 
'''for row in range(5):
    for col in range(4):
        if (col == 0 or col == 3) or (row == 2 and (col > 0 and col < 3)):
            print("*",end="")
        else:
            print(end=" ")
    print()'''

#J

'''for row in range(6):
    for col in range(5):
        if (col == 2) or (row == 0 and (col != 2)) or (row == 5 and (col !=3 and col != 4))or (row == 4 and (col !=1 and col !=3 and col != 4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
'''

#K
'''for row in range(7):
   for col in range(5):
    if (col == 0) or (col > 0 and (row == 0 or row == 6) and col != 1 and col != 2 and col != 3) or (col > 0 and (row == 1 or row == 5) and  col != 2 and col != 1 and col != 4) or (col > 0 and (row == 2 or row == 4) and  col != 1 and col != 3 and col != 4) or (col>0 and (row ==3 and col != 2 and col != 3 and col != 4)):
        print("*",end="")
    else:
        print(end= " ")
   print()'''

#L
'''for row in range(5):
    for col in range(4):
        if (col == 0) or col > 0 and (row == 4):
            print("*",end=" ")
        else:
            print(end=" ")
    print() '''


#M
# for row in range(7):
#     for col in range(6):
#         if (col == 0 or col == 6) or (col > 0 and col < 5  and (row == 1 and col != 2 and col != 3 and col != 4)) or (col > 0 and col < 5  and (row == 2 and col != 1 and col != 3 and col != 5)) or (col > 0 and  col < 5 and ( col != 1 and col != 2 and col != 4 and col  != 5)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


#O

for row in range(6):
    for col in range(5):
        if (col == 0 or col == 4 and (row>0 and row<5 )) or (row == 0 or row == 5 and (col > 0 and col < 5)):
            print("*",end="")
        else:
            print(end=" ")
    print()