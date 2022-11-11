# Here's one for you, nineteen for me

taxincome = int(input("What is your 2019 taxable income? "))

if taxincome <= 9700:
    taxliability = (taxincome * 0.10)
elif taxincome <= 39475:
    taxincomeoverx = taxincome - 9700
    taxliability = 970 + (taxincomeoverx * 0.12)
elif taxincome <= 84200:
    taxincomeoverx = taxincome - 39475
    taxliability = 4543 + (taxincomeoverx * 0.22)
elif taxincome <= 160725:
    taxincomeoverx = taxincome - 84200
    taxliability = 14382 + (taxincomeoverx * 0.24)
elif taxincome <= 204100:
    taxincomeoverx = taxincome - 160725
    taxliability = 32748 + (taxincomeoverx * 0.32)

taxrate = ((taxliability) / taxincome) * 100

print(f"Your tax liability is ${taxliability:,.2f}") # "," format specifier separates integers in group of 3
print(f"Your effective tax rate is {taxrate:.1f}%")
