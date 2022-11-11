code = input(("Enter the customer's code: "))
begmeter = int(input("Enter the customer's beginning meter reading: "))
endmeter = int(input("The customer's ending meter reading: "))


if endmeter >= begmeter: # if endmeter = beg meter, should cost be 0?? 
    gallons = (endmeter - begmeter) / 10 
elif endmeter < begmeter:
    gallons = ((endmeter + 1_000_000_000) - begmeter) / 10

if code.lower() == 'r': 
    cost = 5 + (0.0005 * gallons)
elif code.lower() == 'c': 
    if gallons <= 4_000_000:
        cost = 1000
    if gallons > 4_000_000:
        cost = 1000 + (0.00025 * gallons)
elif code.lower() == 'i': 
    if gallons <= 4_000_000:
        cost = 1000
    elif gallons <= 10_000_000:
        cost = 2000
    else: 
        cost = 2000 + (0.00025 * gallons)
else: 
    gallons = 0
    cost = 0

if 0 > (begmeter or endmeter) or (begmeter or endmeter)> 999999999: # making sure meter is w/in bounds
    gallons = 0
    cost = 0 

print(f"Customer code: {code}")
print(f"Beginning meter reading: {begmeter:0>9}".format(begmeter))
print(f"Ending meter reading: {endmeter:0>9}".format(endmeter))

if gallons == 0 and cost == 0:
    print("Invalid entry")
    print(f"Gallons of water used: {gallons:.1f}")
    print(f"Amount billed: ${cost:.2f}")

else:
    print(f"Gallons of water used: {gallons:.1f}")
    print(f"Amount billed: ${cost:.2f}") 

