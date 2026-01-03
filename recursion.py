# Write a recursive function to calculate the sum of first n natural numbers.
        
# def cal_sum(n):
#     if n == 0:
#         return 0
#     else:
#      return cal_sum(n-1)+n

# sum = cal_sum(5)
# print(sum)

#Question 2: Write a Python function that uses recursion to calculate the nth Fibonacci number.
'''def fibonacci(n):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)
   
print(fibonacci(5))'''


''' fibonacci(5) = fibonacci(4) + fibonacci(3)
             = fibonacci(3) + fibonacci(2) + fibonacci(2) + fibonacci(1)
             = fibonacci(2) + fibonacci(1) + fibonacci(1) + fibonacci(0) + fibonacci(1) + fibonacci(0)
             = 1 + 1 + 1 + 0 + 1 + 0
             = 5 '''

# Write a Python function that uses recursion to print table .

'''def multi_table(num,i):
    if i > 10:
        return
    else:
        print(num*i)
        return multi_table(num,i+1)
    
multi_table(10,1)'''


#factorial

'''
def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
result = factorial(5)
print(result)'''