
# global variables (since they are in function and also called in main program)

item_price = 0
payment_due = 0
total_change = 0

nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

def stock_contents():
    print_stock = f'''Welcome to the vending machine change maker program \nChange maker initialized. \nStock contains:
    \t{nickels} nickels \n\t{dimes} dimes \n\t{quarters} quarters \n\t{ones} ones \n\t{fives} fives
    '''
    return print_stock

def get_price(input_price):
    global item_price
    while True:
        if input_price == 'q':
            break 
        else:
            input_price = float(item_price)
            input_price = round(input_price * 100)
        if input_price < 0: # FIX ME: looping the error message 
            print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
            item_price = input("Enter the purchase price (xx.xx) or 'q' to quit: ") # what if item_price is another letter? error message?

        elif ((input_price % 5) != 0):
            print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
            item_price = input("Enter the purchase price (xx.xx) or 'q' to quit: ") # what if item_price is another letter? error message?

        else:
            return (input_price / 100)

def dollars_and_cents(item_price):
    item_price *= 100
    dollars = item_price // 100
    cents = item_price % 100
    money = f"{dollars} dollars and {cents:.0f} cents"
    return money

def collect_deposit(input_deposit):
    global payment_due 
    global fives 
    global ones
    global quarters
    global dimes
    global nickels
    payment_due *= 100
    if input_deposit == 'c':
        return False
    elif input_deposit == 'n':
        payment_due -= 5
        nickels += 1
    elif input_deposit == 'd':
        payment_due -= 10
        dimes += 1
    elif input_deposit == 'q':
        payment_due -= 25
        quarters += 1
    elif input_deposit == 'o':
        payment_due -= 100
        ones += 1
    elif input_deposit == 'f':
        payment_due -= 500
        fives += 1
    payment_due /= 100
    return dollars_and_cents(payment_due)  


def calculate_change(payment_due):
    global quarters
    global dimes 
    global nickels
    change = 0
    payment_due *= -100 #convert to cents (negative to make neg payment due -> pos change)
    payment_due = int(round(payment_due))
    
    quarters_needed, leftover = divmod(payment_due, 25)
    dimes_needed, leftover2 = divmod(leftover, 10)
    nickels_needed = leftover2 // 5

    if quarters_needed == 0 and dimes_needed == 0:
        change = f"{nickels_needed} nickels"
    elif dimes_needed == 0 and nickels_needed == 0:
        change = f"{quarters_needed} quarters"
    elif quarters_needed == 0:
        change = f"{dimes_needed} dimes\n{nickels_needed} nickels"
    elif dimes_needed == 0:
        change = f"{quarters_needed} quarters\n{nickels_needed} nickels"
    else:
        change = f"{quarters_needed} quarters\n{dimes_needed} dimes\n{nickels_needed} nickels"

    change = f"\t{quarters_needed} quarters\n\t{dimes_needed} dimes\n\t{nickels_needed} nickels"
    return change

def calculate_refund(payment_due):
    global item_price
    
    refund = float(item_price) - float(-1 * payment_due) # not correct
    global quarters
    global dimes 
    global nickels
    refund = int(round(refund))
    quarters_needed, leftover = divmod(refund, 25)
    dimes_needed, leftover = divmod(leftover, 10)
    nickels_needed = leftover // 5

    refund = f"\t{quarters_needed} quarters\n\t{dimes_needed} dimes\n\t{nickels_needed} nickels"
    return refund

#FIX ME: make sure stock is enough, use the quarters needed or quarters we have, whichever is bigger 
#FIX ME: when 'c' entered, change is the amount entered... 

# main program
if __name__ == "__main__":
    # print("Welcome to the vending machine change maker program \nChange maker initialized.") 
    # print(stock_contents())
    # item_price = input("Enter the purchase price (xx.xx) or 'q' to quit: ") # what if item_price is another letter? error message?
    print("Welcome to the vending machine change maker program \nChange maker initialized.") 
    print(stock_contents())
    item_price = input("Enter the purchase price (xx.xx) or 'q' to quit: ") # what if item_price is another letter? error message?
# FIX ME: input item_price gets executed twice if item_price != 'q' -- should only go once but i need the loop 
    while item_price != 'q':
        #item_price = input("Enter the purchase price (xx.xx) or 'q' to quit: ") # what if item_price is another letter? error message?
        payment_due = get_price(item_price)

    
        print("\nMenu for deposits: \n  \'n\' - deposit a nickel \n  \'d\' - deposit a dime \n  \'q\' - deposit a quarter")
        print("  \'o\' - deposit a one dollar bill \n  \'f\' - deposit a five dollar bill \n  \'c\' - cancel the purchase")

        print(f"\nPayment due: {(dollars_and_cents(payment_due))}")
        while True:
            input_deposit = input("Indicate your deposit: ") 
            if input_deposit == 'n' or 'd' or 'q' or 'o' or 'f': 
                collect_deposit(input_deposit)
                #print(f"\nPayment due: {(dollars_and_cents(payment_due))}")

                if payment_due < 0:
                    print(f"Please take the change below. ")
                    print(calculate_change(payment_due))
                    print(stock_contents())
                    break
                elif payment_due == 0:
                    print("No change.")
                elif input_deposit == 'c':
                    print(f"Please take the change below. ")
                    print(calculate_refund(payment_due))
                    print(stock_contents())
                    break
                else:
                    print(f"Payment due: {dollars_and_cents(payment_due)}")
            else:
                print(f"Illegal selection: {input_deposit}")
                print(f"Payment due: {collect_deposit(input_deposit)}")
        item_price = input("Enter the purchase price (xx.xx) or 'q' to quit: ") # what if item_price is another letter? error message?

    
   # print(stock_total_money())

