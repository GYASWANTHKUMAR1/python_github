customerNames = ['Jane Smith', 'Iason Jordan', 'David Morgan', 'Brain John', 'Jack Swift']
customerPins = ['0123', '2575', '7275', '2312', '5049']
customerBalances = [10000, 20000, 20000, 40000, 10000]

deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0  # Variable to track total custmors


# This statement below helps the program to run continuously.
while True:
    # os.system("cls")  # Uncomment if you want to clear the screen on every loop (Windows specific)
    print("=====================================")
    print(" ----Welcome to Times Bank----       ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance  >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*************************************")
    
    # The below statement takes the choice number from the user.
    choiceNumber = input("Select your choice number from the above menu : ")

    if choiceNumber == "1":
        print("Choice number 1 is selected by the customer")
        NOC = float(input("Number of Customers : "))  # Take number of customers
        
        i += NOC
        if i > 5:
            print("\nCustomer registration limit reached!")
            i -= NOC
        else:
            while counter_1 <= i:
                name = input("Input Fullname : ")
                pin = input("Please input a pin of your choice : ")
                balance = 0
                deposition = float(input("Please input a value to deposit to start an account : "))
                balance += deposition
                customerNames.append(name)
                customerPins.append(pin)
                customerBalances.append(balance)

                print("\nName =", customerNames[counter_2])
                print("Pin =", customerPins[counter_2])
                print("Balance =", customerBalances[counter_2], "-/Rs")
                counter_1 += 1
                counter_2 += 1
                print("\nNew account created successfully!")
                print("\nYour name is available on the customer list now : ")
                print(customerNames)
                print("\nNote! Please remember the Name and Pin")
                print("========================================")
        
        mainMenu = input("Press Enter to go back to the main menu or exit...")

    elif choiceNumber == "2":
        print("Choice number 2 is selected by the customer")
        j = 0
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            while k < len(customerNames) - 1:
                k += 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j += 1
                        print("Your Current Balance:", customerBalances[k], "-/Rs")
                        balance = customerBalances[k]
                        withdrawal = float(input("Input value to Withdraw : "))
                        if withdrawal > balance:
                            deposition = float(input("Please deposit a higher value because your balance is not enough : "))
                            balance += deposition
                            print("Your Current Balance:", balance, "-/Rs")
                            balance -= withdrawal
                            print("\n----Withdraw Successful!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, "-/Rs\n\n")
                        else:
                            balance -= withdrawal
                            print("\n----Withdraw Successful!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, "-/Rs\n\n")
            
            if j < 1:
                print("Your name and pin do not match!\n")
                break
        mainMenu = input("Press Enter to go back to the main menu or exit...")

    elif choiceNumber == "3":
        print("Choice number 3 is selected by the customer")
        n = 0
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            while k < len(customerNames) - 1:
                k += 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n += 1
                        print("Your Current Balance: ", customerBalances[k], "-/Rs")
                        balance = customerBalances[k]
                        deposition = float(input("Enter the value you want to deposit : "))
                        balance += deposition
                        customerBalances[k] = balance
                        print("\n----Deposition successful!----")
                        print("Your New Balance: ", balance, "-/Rs\n\n")
            
            if n < 1:
                print("Your name and pin do not match!\n")
                break
        mainMenu = input("Press Enter to go back to the main menu or exit...")

    elif choiceNumber == "4":
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        while k < len(customerNames):
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], "-/Rs")
            print("\n")
            k += 1
        mainMenu = input("Press Enter to go back to the main menu or exit...")

    elif choiceNumber == "5":
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system!")
        print("\nCome again")
        print("Bye bye")
        break

    else:
        print("Invalid option selected. Please try again!")
        mainMenu = input("Press Enter to go back to the main menu or exit...")
