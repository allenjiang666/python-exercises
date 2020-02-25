print("\n~~~ Welcome to your terminal checkbook! ~~~\n\n")

print("What would you like to do?\n\n")

print("1) view current balance\n2) record a debit (withdraw)\n3) record a credit (deposit)\n4) exit")

choice = int(input("Your choice? "))


if choice == 1:
    print("Your current balance is $")
elif choice == 2:
    print("How much is the debit? $")
elif choice == 3:
    print("How much is the credit? $")
elif choice == 4:
    print("Thanks, have a great day!")
else:
    print("Invalid input")
