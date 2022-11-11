firstint = int(input())
secondint = int(input())

if firstint > secondint:
    print("Second integer can't be less than the first.")
if firstint<= secondint:
    while firstint <= secondint:
        print(firstint, end = ' ')
        firstint += 5
    print()




# i = 0
# if firstint <= secondint:
#     while i <= 5:
#         firstint += 5
#         i += 1
#         print(firstint, end=' ')
# else:
#     print("Second integer can't be less than the first.")