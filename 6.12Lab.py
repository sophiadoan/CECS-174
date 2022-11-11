def days_in_feb(user_year):
    leapyear = False
    if user_year % 400 == 0:
       leapyear = True
    elif user_year % 4 == 0 and user_year % 100 != 0:
        leapyear = True
    if leapyear == True:
        febdays = 29
    else:
        febdays = 28 
    return febdays

if __name__ == '__main__':
    year = int(input())
    print(f'{year} has {days_in_feb(year)} days in February.')