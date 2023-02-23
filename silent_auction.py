def check_input (question):
    error = "That was not a valid number"
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print (error)


    def welcome (text, symbol) :
        print(symbollen(text) )
        print(text)
        print(symbol * len (text) )
        print()
# Main routine
bid = 8.0
highest = 0.0
welcome = ("Baker's fantastic Auctions ", "")
item = input ( "what is the auction for? ")
reserve= check_input ("what is the reserve price? ")
print()
print("The auction for the ", item, " has started ! ")
while bid == -1:
    print("The highest bid so far is $", highest)
    bid_check_input = ("What is your bid? (-1 to quit) $")
    if bid > highest:
        highest = bid
    elif bid == -1:
        break
    else:
        print("\nSorry, that bid was not high enough")
if highest == reserve:
    print()
    print("-")
    print("The {item} sold at auction for $", highest)
    ("============================================")
else:
    print()
    print("-============================")
    print("The ", item, " was not sold because the")
    f" reserve of ${reserve: .2f} was not met\n"
    f"The highest bid was only ${highest:.2f}"
