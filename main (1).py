import random #First step is to import random library in order to use the built in random functions in python. 

print('Hello. Welcome to your personal ATM machine.') #Print statement to introduce the program to the user. 
print()
pin = int(input('Enter your pin number: '))

#The code above asks for user input for their pin in order to start the ATM process. The input has to be an integer.   
print()
print('What would you like to do today?')
choice = input('Check Balance, Deposit, Withdraw, Transfer --> ') #Then you would ask the user out of the four options at the ATM, what they would like to do with their balance. 

choice1 = choice.casefold() #String method: casefold() is used in order to standardize the user input. Since the user can enter the input capitalized or lowercased, it wouldn't matter because the casefold() method would automatically translate the user input into lowercase letters.

checking_balance = random.randint(0,5000) 
saving_balance = random.randint(0,5000)
#This code above uses the random methods to generate the random amount of money for checkings and savings.

if choice1 ==  "check balance": #if statement plus the relation operator "==" is used here to figure.
  #Program asks for user input of either checking or savings.
  balance_type = input("Checking or Savings? -->  ")
  #Input is immediately translated into lowercase letters via the casefold() function.
  balance_type = balance_type.casefold()
  #Checks if balance_type is equal to the input, 'checking'.
  if balance_type == "checking":
    #If so, then the program prints out the checking balance of the user.
    print("Checking Balance: $", checking_balance)
  else:
    #If not, then the program prints out the saving balance of the user.
    print("Savings Balance: $", saving_balance)
    
elif choice1 ==  "deposit":#This is elif statement would run the code if the user desires to deposit money.
  balance_type = input("Checking or Savings? -->  ") #This asks the user if they would like to choose checking or savings to deposit money.
  balance_type = balance_type.casefold() #string manipulation to uniform the input.
  if balance_type == "checking": #relational operator.
    print("Checking Balance: $", checking_balance)
    deposit_amount = int(input("Enter an amount: $"))
    new_balance = checking_balance + deposit_amount
    print("New Checking Balance: $", new_balance)
  else:
    print("Savings Balance: $", saving_balance)
    deposit_amount = int(input("Enter an amount: $"))
    new_balance = saving_balance + deposit_amount
    print("New Checking Balance: $", new_balance)

#elif statement plus the relation operator "==" is used here to figure out if choice1 equals the input, 'withdraw.'
elif choice1 == 'withdraw':
  #choice2 will equal the input, 'checking'or 'savings'.
  choice2 = input('Checking or Savings? --> ')
  #choice2 will be reassigned through the casefold() function.
  choice2 = choice2.casefold()
  #nested if-elif-else statement.
  if choice2 == 'checking':
    #prints a random checking balance to the user.
    print("('Checking Balance: $'", checking_balance, ")")
    #amount will equal an integer input for whatever amount of money the user wants to withdraw.
    amount = int(input('Enter an amount: '))
    #withdrawed equals the checking balance subtracted by what the user inputs as 'amount'. The "-" sign is an operator.
    if amount <= checking_balance:
      withdrawed = checking_balance - amount
    #The new checking balance will be printed out.
      print("('New Checking Balance: $',", withdrawed, ")")
    #elif user inputs 'savings' as choice2.
    if amount > checking_balance:
      withdrawed = checking_balance - amount
    #The new checking balance will be printed out.
      print("('New Checking Balance: $',", withdrawed, ")")
      print("YOu do not have enough money in your account.")

  elif choice2 == 'savings':
    #The program will print a random savings balance.
    print("(Savings Balance: $',", saving_balance, ")")
    #amount will equal an integer input for whatever amount of money the user wants to withdraw.
    amount = int(input('Enter an amount: '))
    #withdrawed equals the savings balance subtracted by the amount. Again, the operator, "-", is used.
    withdrawed = saving_balance - amount
    #The new savings balance will be printed out with 'withdrawed' serving as the new value.
    if amount <= saving_balance:
      withdrawed = saving_balance - amount
    #The new saving balance will be printed out.
      print("('New saving Balance: $',", withdrawed, ")")
    #elif user inputs 'savings' as choice2.
    if amount > saving_balance:
      withdrawed = saving_balance - amount
    #The new saving balance will be printed out.
      print("('New Savings Balance: $',", withdrawed, ")")
      print("You do not have enough money in your account.")
  else:
    #if anything else is inputted, an error message will be printed out.
    print('You have made a typing error. Please rerun the program.')

#elif statement plus the relation operator "==" is used here to figure out if choice1 equals the input, 'transfer.'
elif choice1 == 'transfer':
  #pin2 is an integer input that asks the user to enter their pin again.
  pin2 = int(input('Enter your pin number again: '))
  if pin2 == pin:
      #If the user prints their pin again correctly, the program will ask for a transfer from either their checking or savings.
    choice3 = input("From Checking or Savings? --> ")
    #The string manipulation casefold() is once again used to convert user input into lowercase letters uniformly. 
    choice3 = choice3.casefold()
    if choice3 == 'checking':
      #if user inputs 'checking' for choice3, their checking and savings balance will be printed out.
      print("('Checking Balance: $',", checking_balance, ")")
      print("('Savings Balance: $',", saving_balance, ")")
      #amount will equal an integer input for whatever amount of money the user wants to transfer from their checking balance.
      amount = int(input('Enter an amount: '))
      #'transfer_c' will equal the user's checking balance subtracted by the amount. The minus sign serves as the operator in the equation.
      transfer_c = checking_balance - amount
      #'transfer_s' will equal the user's savings balance with 'amount'. The plus sign serves as the operator.
      transfer_s = saving_balance + amount #transfers that amount into savings
      #The new checking and savings balance will be printed out.
      print("('New Checking Balance: $',", transfer_c, ")")
      print("('New Savings Balance: $',", transfer_s, ")")
    if choice3 == 'savings':
      #if user inputs 'savings' for choice3, their checking and savings balance will be printed out.
      print("('Checking Balance: $',", checking_balance, ")")
      print("('Savings Balance: $',", saving_balance, ")")
      #The program will ask for an integer input and will store it inside 'amount'.
      amount = int(input('Enter an amount: '))
      transfer_c = checking_balance + amount #Addition operator used to add the amount into checking.
      transfer_s = saving_balance - amount
      
      print("('New Checking Balance: $',", transfer_c, ")") #Prints out the updated checking balance.
      print("('New Savings Balance: $',", transfer_s, ")") #Prints out the updated savings balance.
    else:
      print('You have made a typing error. Please rerun the program.') #Else statement prints out error message if user inputs anything other than 'checking' or 'savings'.
  else:
    #If anything else besides the user's correct pin is inputted, an error message will be printed.
    print("You have made a typing error. Please rerun the program.")
else:
  print('You have made a typing error. Please rerun the program.') #Else statement applied in order to inform user of a mistake if the user entered the incorrect input/data type, it will ask user to restart the program. 

#Division of Responsibility:
  #check balance = Bree

  #deposit = Bree

  #withdraw = Edwin

  #transfer = Edwin