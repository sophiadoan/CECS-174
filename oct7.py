
# # #validate entry positive vals only
# # num = int(input("please enter a + value... ")) #initialize loop variant
# # while num < 0: #testing loop variant
# #     num = int(input("please enter a + value... ")) #updating




# # #calculating avg
# # total = 0
# # numQ = 10
# # count = 1
# # while count <= 10:
# #     q = int(input("please enter a grade: "))
# #     while q < 0 or q > 10:
# #         q = int(input("please enter a grade within the range 0-10: "))
# #     total += q
# #     count += 1
# #     # if q > 0:
# #     #     count += 1
# #     #     total += q 
# #     # else: 
# #     #     q = print("invalid input")
# # avg = total / numQ 
# # print("Average ", avg)

# # calculating a factorial value

# # num = int(input("please enter a + value "))
# # while num < 0:
# #     num = int(input("please enter a + value "))
# # mul = 1
# # count = 1
# # while count <= num:
# #     mul *= count
# #     count += 1
# # print(mul)



# # h = 0
# # while h < 24:
# #     m = 0
# #     while m < 60:
# #         s = 0 
# #         while s < 60:
# #             print(f"{h}:{m}:{s}")
# #             s += 1 
# #         m + 1
# #     h += 1
# myList = [2, 5, 4, 3]
# #for i in myList:
# #for i in 3, 6, 2, 7: #iterable
# # for i in "myList":

# for i in range ():
#     print(i, end = ' ')
#     print()

# #for loop used for counting
# fact = 1
# for i in range(1, 6): # 1, 2, 3, 4, 5
#     fact *= i
# print(fact)

# i = 33 
# while i >23:
#     print(i, end = ' ')
#     i -= 1
# print()


# for h in range(24):
#     for m in range (60):
#         for s in range(60):
#             print(f"{h}:{m}:{s}")

# for i in range(5):
#     if i == 3:
#         continue #skip one iteration 
#         #break -- exit the loop
#     print(i, end = ' ')

# a=0 
# while a < 5:       
#     b=0 
#     while b < 5: 
#             print('*', end='') 
#             b += 1  
#     print()  
#     a += 1  

# word = input('Enter a word: ') 
# for letter in word: 
#      print(letter) 

# for c in 'ABCDEF': #WHY C??
#      print('[', c, ']', end='', sep='') 
# print() 

# word = input('Enter text: ') 
# vowel_count = 0  
# for c in word: 
#      if c == 'A' or c == 'a' or c == 'E' or c == 'e' \
#         or c == 'I' or c == 'i' or c == 'O' or c == 'o': 
#         print(c, ', ', sep='', end='')  # Print the vowel 
#         vowel_count += 1                # Count the vowel 
# print(' (', vowel_count, ' vowels)', sep='') 

# #  Get the number of rows and columns in the table 
# size = int(input("Please enter the table size: ")) 
# #  Print a size x size multiplication table 
# for row in range(1, size + 1): 
#      for column in range(1, size + 1): 
#          product = row*column     # Compute product 
#          print(product, end=' ')  # Display product 
#      print()                      # Move cursor to next row 

# #  Get the number of rows and columns in the table 
# size = int(input("Please enter the table size: ")) 
#  #  Print a size x size multiplication table 
# for row in range(1, size + 1): 
#      for column in range(1, size + 1): 
#          product = row*column                    # Compute product 
#          print('{0:4}'.format(product), end='')  # Display product 
#      print() # Move cursor to next row  

# sum = 0 
# done = False 
# while not done: 
#      val = int(input("Enter positive integer (999 quits):")) 
#      if val < 0: 
#          print("Negative value",  val,  "ignored") 
#          continue  # Skip rest of body for this iteration 
#      if val != 999: 
#          print("Tallying", val) 
#          sum += val 
#      else: 
#          done = (val == 999)   # 999 entry exits loop 
# print("sum =", sum) 
 
# for i in range(10): 
#      print(i, end=' ')   # Print i as served by the range object 
#      if i == 5: 
#          i = 20   # Change i inside the loop? 
#      print('({})'.format(i), end=' ') 
# print() 

'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
# print('Two-letter domain names:')

# letter1 = 'a'
# letter2 = '?'
# number = 0
# while letter1 <= 'z':  # Outer loop
#     letter2 = 'a'
#     while letter2 <= 'z':  # Inner loop
#         print(f'{letter1}{letter2}.com')
#         letter2 = chr(ord(letter2) + 1)
#     while letter2 <= 'z':
#         print(f'{letter1}{number}.com')
#         number += 1
#     letter1 = chr(ord(letter1) + 1)


num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

number = 1

for r in range(num_rows):
    letter = 'A'
    for c in range(num_cols):
        print(f"{number}{letter}", end=' ')
        letter = chr(ord(letter) + 1)  
    number += 1          
print()