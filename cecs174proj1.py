
import math

print(f"{'Richter':20} {'Joules':^20} {'TNT':>20}")
richter = 1
joules_equivalent = math.pow(10, (1.5 * richter) + 4.8)
tnt_tons = joules_equivalent / (4.184 * math.pow(10, 9))
print(f"{richter:<20} {joules_equivalent:^20}              {tnt_tons:>20}")

richter = 5
joules_equivalent = math.pow(10, (1.5 * richter) + 4.8)
tnt_tons = joules_equivalent / (4.184 * math.pow(10, 9))
print(f"{richter:<20} {joules_equivalent:^20}          {tnt_tons:>20}")

richter = 9.1
joules_equivalent = math.pow(10, (1.5 * richter) + 4.8)
tnt_tons = joules_equivalent / (4.184 * math.pow(10, 9))
print(f"{richter:<20}  {joules_equivalent:^20} {tnt_tons:>20}")

richter = 9.2
joules_equivalent = math.pow(10, (1.5 * richter) + 4.8)
tnt_tons = joules_equivalent / (4.184 * math.pow(10, 9))
print(f"{richter:<20}  {joules_equivalent:^20} {tnt_tons:>20}")

richter = 9.5
joules_equivalent = math.pow(10, (1.5 * richter) + 4.8)
tnt_tons = joules_equivalent / (4.184 * math.pow(10, 9))
print(f"{richter:<20}  {joules_equivalent:^20}{tnt_tons:>20}")

input_richter = float(input("Please enter a Richter scale value: "))
richter = input_richter
joules_equivalent = math.pow(10, (1.5 * richter) + 4.8)
tnt_tons = joules_equivalent / (4.184 * math.pow(10, 9))
print(f"Richter scale value: {input_richter}")
print(f"Equivalence in joules: {joules_equivalent}")
print(f"Equivalence in tons of TNT: {tnt_tons}")
