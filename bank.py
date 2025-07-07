## Simple Bank System ##
def display_menu():
    print("\nSimple Bank System")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

def check_balance(balance):
    print(f"Na Wetin remain be this: ${balance:}")

def withdraw_money(balance):
    amount = float(input("Enter amount to  withdraw: "))
    if amount > balance:
        print("Comrade you no get up to that amount.")
    if amount < 0:
        print("Comrade ask for your money.")
    else:
       balance = balance - amount
       print(f"You have withdrawn ${amount}. Your new balance is: ${balance}.")
    return balance

def deposit_money(balance):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance = balance + amount
        print(f"You have deposited ${amount}. Odogwu!!!, Your new balance is: ${balance}")
    else:
        print("Comrade you no get up to that amount.")
    return balance
def main():
    balance = 0.0
    name = input("Enter your name: ")
    print(f"Welcome, {name}! ")

    while True:
      display_menu()
      choice = (input("Enter an option: "))

      if choice == '1':
           check_balance(balance)
      elif choice == '2':
           balance = withdraw_money(balance)
      elif choice == '3':
           balance =  deposit_money(balance)
      elif choice == '4':
           print("Thank you for using the Simple Bank System. Goodbye!")
           break
      else:
        print("Invalid choice, please try again.")
        print("Pick a number you see on display.")

if __name__ == "__main__":
    main()

