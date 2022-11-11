nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0
print("Welcome to the vending machine change maker program \nChange maker initialized. \nStock contains:")
print(f"  {nickels} nickels \n  {dimes} dimes \n  {quarters} quarters \n  {ones} ones \n  {fives} fives")
def stock_total_money():
 
  total_money = (nickels * 5) + (dimes * 10) + (quarters * 25) + (ones * 100)+ (fives * 500)
  total_money /= 100
  return total_money
def dollars_and_cents(dollaramount):
  dollaramount *= 100
  dollaramount = float(dollaramount)
  dollars = dollaramount // 100
  cents = dollaramount % 100
  money = f"{dollars:.0f} dollars and {cents:.0f} cents"
  return money
item_price = "empty"
while item_price != "q":
   item_price = (input("\nEnter purchase price (xx.xx) or \'q\' to quit: "))
   if item_price == "q":
    
       continue
   item_price = float(item_price)
   item_price *= 100
   if item_price < 0 or (item_price % 5) != 0:
       print("Illegal price: Must be a non-negative multiple of 5 cents")
       continue
   print("\nMenu for deposits: \n  \'n\' - deposit a nickel \n  \'d\' - deposit a dime \n  \'q\' - deposit a quarter")
   print("  \'o\' - deposit a one dollar bill \n  \'f\' - deposit a five dollar bill \n  \'c\' - cancel the purchase")
 
   dollars = item_price // 100
   cents = item_price % 100
   cancel = item_price
   condition = True
   condition2 = True
   print(f"\nPayment due: {dollars:.0f} dollars and {cents:.0f} cents")
   while condition:
       deposit = input("Indicate your deposit: ")
       if deposit == "n":
           item_price -= 5
           nickels += 1
       elif deposit =="d":
           item_price -= 10
           dimes += 1
       elif deposit == "q":
           item_price -= 25
           quarters += 1
       elif deposit == "o":
           item_price -= 100
           ones += 1
       elif deposit == "f":
           item_price -= 500
           fives += 1
       elif deposit == "c":
           item_price = (item_price - cancel)
           condition = False
           continue
       else:
           print(f"Illegal selection: {deposit}")
       dollars = item_price // 100
       cents = item_price % 100
       if item_price > 0:
           print(f"Payment due: {dollars:.0f} dollars and {cents:.0f} cents")
       else:
           condition = False
           continue
   else:
       item_price /= -1
       while condition2:
           quarters_needed, leftover = divmod(item_price, 25)
           quarter_diff = quarters - quarters_needed
           if quarter_diff < 0:
               leftover += (quarter_diff) * -25
               quarters_needed = int(quarters_needed + quarter_diff)
           dimes_needed, leftover2 = divmod(leftover, 10)
           dime_diff = dimes - dimes_needed
           if dime_diff < 0:
               leftover2 += (dime_diff) * -10
               dimes_needed = int(dimes_needed + dime_diff)
           nickels_needed, leftover3 = divmod(leftover2, 5)
           nickel_diff = nickels - nickels_needed
           if nickel_diff < 0:
               leftover3 += (nickel_diff) * -5
               nickels_needed = int(nickels_needed + nickel_diff)
               condition2 = False
           else:
               refund = 0
               condition2 = False
       else:
           refund = (quarters_needed*.25 + dimes_needed*.10 + nickels_needed*.05)/100
       quarters = (quarters - quarters_needed) * 100
       dimes = (dimes - dimes_needed) * 100
       nickels = (nickels - nickels_needed) * 100
       quarters_needed = int(quarters_needed)
       dimes_needed = int(dimes_needed)
       nickels_needed = int(nickels_needed)
       print("\nPlease take the change below.")
       if refund == 0:
           print("No change due.")
       else:
           if quarters_needed == 0 and dimes_needed == 0 and nickels_needed != 0:
               print(f"\n  {nickels_needed:.0f} nickels")
           elif quarters_needed == 0 and nickels_needed == 0 and dimes_needed != 0:
               print(f"\n  {dimes_needed:.0f} dimes")
           elif dimes_needed == 0 and nickels_needed == 0 and quarters_needed != 0:
               print(f"\n  {quarters_needed:.0f} quarters")
           elif quarters_needed == 0 and dimes_needed != 0 and nickels_needed != 0:
               print(f"\n  {dimes_needed:.0f} dimes \n  {nickels_needed:.0f} nickels")
           elif dimes_needed == 0 and quarters_needed != 0 and nickels_needed != 0:
               print(f"\n  {quarters_needed:.0f} quarters \n  {nickels_needed:.0f} nickels")
           elif nickels_needed == 0 and dimes_needed != 0 and quarters_needed != 0:
               print(f"\n  {quarters_needed:.0f} quarters \n  {dimes_needed:.0f} dimes")
           else:
               print(f"\n  {quarters_needed:.0f} quarters \n  {dimes_needed:.0f} dimes \n  {nickels_needed:.0f} nickels")
       if round(leftover3) != 0:
           left_over_dollars = leftover3//100
           left_over_cents = leftover3 % 100
           print(f"Machine is out of change. \nSee store manager for remaining refund. \nAmount due is: {left_over_dollars} dollars and {left_over_cents} cents")
       total_dollars = (nickels * .5) + (dimes * .10) + (quarters * .25) + (ones * 1)+ (fives * 5)
       total_dollars /= 100
       total_cents = (nickels*5 + dimes*10 + quarters*25) % 100
       quarters = int(quarters /100)
       dimes = int(dimes/100)
       nickels = int(nickels/100)
       print(f"\nStock contains: \n  {nickels} nickels \n  {dimes} dimes \n  {quarters} quarters \n  {ones} ones \n  {fives} fives")
       continue
else:

   print(f"Total: {dollars_and_cents(stock_total_money())}")
