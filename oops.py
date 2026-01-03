"""
class student:

    def __init__(self,name,marks):
        self.name = name #object attribute
        self.marks = marks

    def get_average(self):
        sum = 0
        for val in self.marks:
            sum +=val
        print("hey",self.name,"your average is",sum/3) 

s1 = student("tony stark" ,[99,98,96])
print(s1.name)
print(s1.get_average())
s1.name = "aditya"                                      
print(s1.get_average())

"""
# class Account:
#     def __init__(self,bal,acc):
#         self.bal = bal
#         self.acc = acc

#     def debit(self,dbt_amount):
#         self.bal -= dbt_amount
#         print("Rs.",dbt_amount,"Was debited")
#         print("Total balance = ",self.get_balance())


    
#     def credit(self,crd_amount):
#         self.bal -= crd_amount
#         print("Rs.",crd_amount,"Was credited")
#         print("Total balance = ",self.get_balance())
        

#     def get_balance(self):
#         return self.bal
    


# a1 = Account(20000,1527)
# print(a1.debit(5000))
# print(a1.credit(5609))


# class circle:
#     def __init__(self,r):
#         self.radius = r
    
#     def area(self):
#         areaCircle = 3.14*self.radius*self.radius
#         print(areaCircle)

#     def perimeter(self):
#         perimeterCircle = 2*3.14*self.radius
#         print(perimeterCircle)

# c1 = circle(21)
# c1.area()
# c1.perimeter()

#INHERITANCE 

'''class employees:
    def __init__(self,role,deparment,salary):
        self.role = role
        self.deparment = deparment
        self.salary = salary
    
    def showdetails(self):
        print("role = ",self.role)
        print("dept = ",self.deparment)
        print("salary = ",self.salary)


class engineer(employees):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",3000000)

eng1 = engineer("mayur",20)
eng1.showdetails()
'''


# class order:
#     def __init__(self,item,price):
#         self.items = item                           
#         self.price = price
          

#     def __gt__(self,ord2): # dunder function gt use ( for grether value ) here self.price = ord1.price
#         return self.price > ord2.price #  =  ord1.price > ord2.price 


# ord1 = order("chips",20)
# ord2 = order("cococola",45)

# print(ord1 > ord2)





        

        



        
        
        