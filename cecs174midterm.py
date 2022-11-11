

# # Your code goes here.
# # You must use the variables as named below.

treat_price = float(input()) * 100 # replace the right-hand side with the correct instructions
# multiply by 100 first, floating point precision limitation 
nickels = treat_price // 5 # replace the right-hand side with the correct instructions
pennies = (treat_price) - (nickels * 5) # replace the right-hand side with the correct instructions
# pennies = treat_price % (nickels * 5)

# Print output as required in the problem.
print(f"You need {int(nickels)} nickels and {int(pennies)} pennies to buy a treat.")

# x = 4 - 10 -18 % 4 - 11 // 3 * 4
# print(x)

# count = 8
# var = 16
# print(count, " x ", var, "=", var /count)

print(1 // .05) # why is this 19 when 1 / 0.05 is 20? 