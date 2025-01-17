from acc import BankAcc


def main():
    myAcc = BankAcc(accNumber="12 3456 5555 9090 1111 0000 7722")
    print("Initial Account Balance:")
    myAcc.displayInfo()
    print()

    myAcc.deposit(25.30)
    print("Account Balance After Deposit:")
    myAcc.displayInfo()
    print()

    myAcc.withdraw(31.70)
    print("Account Balance After First Withdrawal:")
    myAcc.displayInfo()
    print()

    myAcc.withdraw(14)
    print("Final Balance:")
    myAcc.displayInfo()


if __name__ == "__main__":
    main()
