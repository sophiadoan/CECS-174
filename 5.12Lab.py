integer = int(input())

if 11 <= integer <= 100:
    while (integer % 11) != 0:
        print(integer)
        integer -= 1
    else:
        print(integer)
else: 
    print("Input must be 11-100")