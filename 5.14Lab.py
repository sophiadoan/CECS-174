# count = 1

# #largest int


# while count <= 5:
#     a = int(input())
#     b = int(input())
#     if b > a:
#         largest = b
#     count += 1
# print(largest)


#smallest int

i = 0
big_num = -100
small_num = 100

while i < 10:
    num = int(input())
    if -100 <= num <= 100 and big_num < num:
        big_num = num
        #i += 1
    elif small_num > num:
        small_num = num
    i += 1
else:
    print(big_num)
    print(small_num)

