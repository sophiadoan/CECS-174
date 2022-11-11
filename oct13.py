# user_input = input('Enter phone number:\n')
# phone_number = ''

# for character in user_input:
#     if ('0' <= character <= '9') or (character == '-'):
#         phone_number += character
#     elif ('a' <= character <= 'c') or ('A' <= character <= 'C'):
#         phone_number += '2'
#     elif ('d' <= character <= 'f') or ('D' <= character <= 'F'): 
#         phone_number += '3'   
#     elif ('g' <= character <= 'i') or ('G' <= character <= 'I'): 
#         phone_number += '4'   
#     elif ('j' <= character <= 'l') or ('J' <= character <= 'L'): 
#         phone_number += '5'   
#     else:
#        phone_number += '?'   

# print(f'Numbers only: {phone_number}')

# empanada_cost = 3
# taco_cost = 4

# user_money = int(input('Enter money for meal: '))

# max_empanadas = user_money // empanada_cost
# max_tacos = user_money // taco_cost

# meal_cost = 0
# for num_tacos in range(max_tacos + 1):
#     for num_empanadas in range(max_empanadas + 1):
#         meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

#         # Find first meal option that exactly matches user money
#         if meal_cost == user_money:
#             break

#     # Find first meal option that exactly matches user money
#     if meal_cost == user_money:
#         break

# if meal_cost == user_money:
#     print(f'${meal_cost} buys {num_empanadas} empanadas and {num_tacos} tacos without change.')
# else:
#     print('You cannot buy a meal without having change left over.')

# stop = int(input())
# result = 0
# for a in range(3):
#     print(a, end=': ')
#     for b in range(2):
#         result += a + b
#         if result > stop:
#             print('-', end=' ')
#             continue
#         print(result, end=' ')
#     print()

# for x in range(7, 200, 7):
#     if (x % 7 == 0):
#         print(x)

x = 0
while x <= 200:
    if (x % 7 == 0):
        print(x)
    x += 7