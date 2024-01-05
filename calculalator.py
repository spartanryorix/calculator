def calculator():
    '''(int)->(int)
    Returns a new float value when the user uses addition, subtraction, multiplication or division.
    '''

    print("Select an operation.")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")

    while True:

        choice=input('Enter 1,2,3,4:')

        if choice in ('1','2','3','4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice=='1':
            print(num1+num2)
        elif choice=='2':
            print(num1-num2)
        elif choice=='3':
            print(num1*num2)
        elif choice=='4':
            print(num1/num2)

        next_calculation = input('Want to continue? (yes/no):')
        if next_calculation == "no":
          break
        else:
            None
    


if __name__ == "__main__":
    calculator()
    
        
