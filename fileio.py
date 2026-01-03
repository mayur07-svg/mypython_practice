
with open("practice.txt","w") as f:
    f.write("hey every \n we are learning file i/o \n")
    f.write("using java \n i like programing in java")


with open("practice.txt","r") as f:
    data = f.read()
    new_data = data.replace("java","python")
    print(new_data)

#overwrite 

    with open("practice.txt","w") as f:
        f.write(new_data)

# found "learning" word in file (function)
def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
     data = f.read()
    if data.find(word) != -1: # word in data
     print("found")
    else:
     print("not found")

check_for_word()

def check_for_line():
    word = "learning"
    data = True #initilize
    line_no = 1
    with open("practice.txt", "r") as f:
        while data: #valid value  empty
            data = f.readline()
            if(word in data):
               print(line_no)
               return
            line_no += 1

    return-1
    
print(check_for_line())


count_even = 0
count_odd = 0
with open("number.txt","r") as f:
      data = f.read()
      print(data)
      for i in data:
         if(i % 2 == 0):
           count_even += 1
         else:
           count_odd += 1
print("total even number",count_even)
print("total odd number",count_odd)



