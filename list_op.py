'''num_list = []
num1 = int(input("enter the number "))
num2= int(input("enter the number "))
num3= int(input("enter the number "))
num4= int(input("enter the number "))

num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)
print(num_list[len(num_list)-1])'''

#programmer 

'''new_list = []

while True:
    user_input = input("enter the number (type 'stop' for finish)")
    if user_input.lower() == "stop":
        break
    try:
        num = int(user_input)
        new_list.append(num)
        new_list.sort()
        
    except  ValueError:
        print("please enter valid number")
    print(new_list)
gt_num = new_list[len(new_list)-1]
print(f"{new_list[len(new_list)-1]} is grether number ")

    
'''

n_list = []
n = int(input("enter the number of element you want to store"))
for i in range(1,n):
    num_input = int(input("enter number"))
    n_list.append(num_input)
    n_list.sort()
    
print(n_list)
gt_num = n_list[len(n_list)-2]
print(f"{gt_num} is second grether number")
    

