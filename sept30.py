'''Program that calculates savings and interest'''

# initial_savings = 5000
# interest_rate = 0.03

# print(f'Initial savings of ${initial_savings}')
# print(f'at {interest_rate*100:.0f}% yearly interest.\n')

# years = int(input('Enter years: '))
# print()

# savings = initial_savings
# i = 1  # Loop variable
# while i <= years:  # Loop condition
#     print(f' Savings at beginning of year {i}: ${savings:.2f}')
#     savings = savings + (savings*interest_rate)
#     i = i + 1  # Increment loop variable

# print('\n')


# target = int(input())
# n = int(input())
# step = 3
# while n >= target:
#     print(n * 2)
#     n -= step

# PYTHON RANDOM MODULE random(), randint(), choice, shuffle()
import random
print(random.random()) #floating point value between 0.0 and 0.1
print(random.randint(5, 10))
a = [2, 5, 88, -9]
print(random.choice(a)) 
print(random.choice("computer"))
random.shuffle(a)
print(a)


# repeat = True
# while repeat:
#     again = input("do you want to play again, enter y or n ")
#     if again == 'n'.lower():
#         repeat = False
#     else:
#         print("let us play again")
# print("you choose to exit Goodbye...")

# print("{:0>4}".format(5)) #formats 5 with 4 digits total(w the leading 0's)