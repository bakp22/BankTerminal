from Bank import NewUser


user = None
account = None


def main():
    global user, account
    

state = True
while (state):
    print("Hello! Welcome to the Bank of America. ")
    print("1. Create a new Bank of America account")
    print("2. Deposit money")
    print("3. Withdraw Money")
    print("4. Access your Bank of America account")

    # handle user input
    option = input("Please choose an option: ")

    if option == "1":
        result, acc = NewUser.create_account()
        user = result
        account = acc 

        # user.new_anme = Beren Akpinar
        # user.new_accountID


        answer = input("Would you like to see the home screen again? y/n ")
        if answer == "y":
            continue
        elif answer == "n":
            state = False
        else:
            print("invalid response!")
   

            
    elif option == "2":
        test = input("What is your Account ID? ")
        
        if test == user.new_accountID:
            deposit = int(input("How much would you like to deposit? "))
            user.new_balance += deposit
            print(f"Your new Bank of America Balance is ${user.new_balance:.2f}")

            # ASK TO VISIT HOME SCREEN
            answer = input("Would you like to see the home screen again? y/n ")
            if answer == "y":
                continue
            elif answer == "n":
                state = False
            else:
                print("invalid response!")

        else:
            print("Incorrect ID")
            state = False


    
    elif option == "3":
        test = input("What is your Account ID? ")
        
        if test == user.new_accountID:
            withdraw = int(input("How much would you like to withdraw? "))
            user.new_balance -= withdraw
            print(f"Your new Bank of America Balance is ${user.new_balance:.2f}")

            # ASK TO VISIT HOME SCREEN
            answer = input("Would you like to see the home screen again? y/n ")
            if answer == "y":
                continue
            elif answer == "n":
                state = False
            else:
                print("invalid response!")
        else:
            print("Incorrect ID")
            state = False
    

    elif option == "4":
        test = input("What is your Account ID? ")
        
        if test == user.new_accountID:
            acc.balance = user.new_balance
            print(acc)

            # ASK TO VISIT HOME SCREEN
            answer = input("Would you like to see the home screen again? y/n ")
            if answer == "y":
                continue
            elif answer == "n":
                state = False
            else:
                print("invalid response!")
        else:
            print("Incorrect ID")
            state = False
    


main()