from typing import List
checked_in = []
checked_out = []
check_in_out = 2
choice = 0
child_name_chkr = ""
roll_length = 0
rate = 0
final_pay = 0



while choice != 5:
    print("-----------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()
     # this checks a child in and the surrounding processes
    if choice == 1:
        print("you have chosen to drop off a child")
        child_name_chkr = input("input the child's name: ")
        if child_name_chkr in checked_in or child_name_chkr in checked_out:
            if child_name_chkr in checked_in:
                print("this child is already checked in")
                print("enter another child's name or choose 'pick up a child'")
            if child_name_chkr in checked_out:
                checked_out.remove(child_name_chkr)
                checked_in.append(child_name_chkr)
                print("your child is now checked in")
        else:
            print("welcome to the daycare, we hope you enjoy our service")
            checked_in.append(child_name_chkr)
    elif choice == 2:
         # this checks a child out and the surrounding processes
        print("you have chosen to pick up a child")
        child_name_chkr = input("input the child's name: ")
        if child_name_chkr in checked_in or child_name_chkr in checked_out:
            if child_name_chkr in checked_in:
                checked_out.append(child_name_chkr)
                checked_in.remove(child_name_chkr)
                print("your child is now checked out")
            if child_name_chkr in checked_out:
                print("this child is already checked out")
                print("enter another child's name or choose 'pick up a child'")
        else:
            print("your child is not signed into our roll")
     #this calcutates the price
    elif choice == 3:
        roll_length = len(checked_in)
        rate = int(input("what is the current hourly rate? (numbers only): "))
        hours = int(input("how long are the children being looked after for? (numbers only): "))
        final_pay = roll_length * rate * hours
        print("the final pay for all the students for the allotted time is", final_pay)
    elif choice == 4:
        print("you have selected 'print roll'")
        print("logged in roll:")
        print(checked_in)
        print("currently logged out children:")
        print(checked_out)
    else:
        exit("Goodbye")
