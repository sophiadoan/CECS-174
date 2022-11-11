# caffeine half life


caffeine_mg = float(input())

n = 0 
numberofhalflives = (2 ** n) 

n = 1
first_halflife = caffeine_mg * (1/(2 ** n))
print(f"After 6 hours: {first_halflife:.2f} mg")

n = 2
second_halflife = caffeine_mg * (1/(2 ** n))
print(f"After 12 hours: {second_halflife:.2f} mg")

n = 4
third_halflife = caffeine_mg * (1/(2 ** n))
print(f"After 24 hours: {third_halflife:.2f} mg")

