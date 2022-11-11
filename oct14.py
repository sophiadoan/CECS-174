'''function is a piece of code w 3 things:
1. a name
2. a list of parameters
3. a return value (optional) computed based on the parameters
defining a function w out calling it -> func won't work'''

'''
# function, method, subroutine...

def absolute_value(num):
    if num < 0: 
        return -num
    else:
        return num

#null function, returns nothing
def absolute_value(num):
    if num < 0: 
        print(f"the absolute value of {num} is {abs_number}")
    else:
        print(f"the absolute value of {num} is {abs_number}")


#call the function
number = int(input("enter a number "))
abs_number = absolute_value(number)
print(f"the absolute value of {number} is {abs_number}") '''

#return smth vs output statement

# def is_factor(dividend, divisor):
#     if dividend % divisor == 0: 
#         #print(f"{divisor} is a factor of {dividend}")
#         return True
#     else:
#         #print(f"{divisor} is not a factor of {dividend}")
#         return False
# a = int(input("pls enter a value "))
# b = int(input("pls enter a value "))
# print(a, b)



# factor = is_factor (a, b) 
# if factor: 
#     print(f"{b} is a factor of {a}")
# else:
#     print(f"{b} is not a factor fof {a}")


print(605 - ((605//100)*100))
# a 2-digit // 10 is 1 digit; a 3 digit // 10 is 2 digits 
# a 2- digit // 100 is 0; a 3 digit //100 is 1 digit
