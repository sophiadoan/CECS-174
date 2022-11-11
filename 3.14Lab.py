#leap year

# is_leap_year = False
   
input_year = int(input())

if input_year % 400 == 0:
    print(input_year, "- leap year")
elif input_year % 4 == 0 and input_year % 100 != 0:
    print(input_year, "- leap year")
else:
    print(input_year, "- not a leap year")

# is there a way to do this using booleans and def function? 

# bools = ('not a leap year','a leap year')

# input_year = 2002
# is_leap_year = True
# print(f"{input_year} is {bools[is_leap_year]}")

# input_year = 2016
# is_leap_year = False
# print(f"{input_year} is {bools[is_leap_year]}")

