import shelve 

def display_menu():
    print(" ---------------")
    print("|  *CALCULATOR* |")
    print("|  ____________ |")
    print("|  1.ADDITION   |")
    print("|  2.SUBSTRACT  |")
    print("|  3.MULTIPLY   |")
    print("|  4.DIVIDE     |")
    print("|  5.HISTORY    |")
    print("|  6.EXIT       |")
    print(" ----------------")
    print()

def get_input():
    while True:
        try:
            num=int(input("Choose the option"))
            if 1<= num <=6: 
                return num 
            else:
                print("Choose the valid option from 1 to 6")
        except ValueError:
            print("Invalid input. Please enter a valid number")        

def ADDITION():
    num1=float(input("Choose the 1st number"))
    num2=float(input("Choose the 2nd number"))
    result = num1 + num2
    print(f"result: {num1:.2f} + {num2:.2f} = {result:.2f}")
    return result

def SUBSTRACT():
    num1=float(input("Choose the 1st number"))
    num2=float(input("Choose the 2nd number"))
    result = num1 - num2
    print(f"result: {num1:.2f} - {num2:.2f} = {result:.2f}")
    return result

def MULTIPLY():
    num1=float(input("Choose the 1st number"))
    num2=float(input("Choose the 2nd number"))
    result = num1 * num2
    print( f"result: {num1:.2f} * {num2:.2f} = {result:.2f}")
    return result

def DIVIDE():
    num1=float(input("Choose the 1st number"))
    num2=float(input("Choose the 2nd number"))
    if num2==0:
        print("Division by zero is not allowed")
        return None
    else:    
        result = num1 / num2
        print(f"result: {num1:.2f} / {num2:.2f} = {result:.2f}")
        return result

def HISTORY():
    with shelve.open('history.db') as db:
        if 'history' not in db or not db['history']:
            print("No previous calculations")
        else:
            print("Calculation History")
            for idx, item in enumerate(db['history'], start=1):
                print(f"{idx}. {item}")

def main():
    display_menu()
    while True:
        choice = get_input()
        if choice == 1:        
            return ADDITION()
        elif choice == 2:
            return SUBSTRACT()
        elif choice == 3:
            return MULTIPLY()
        elif choice == 4:
            return DIVIDE()
        elif choice == 5:
            HISTORY()
            continue
        elif choice == 6:
            print("Thank you:)")
            break
        else:
            print("Invalid input. Please enter a valid number between 1-6")
            continue

        if result is not None:
            with shelve.open('histry.db', writeback=True) as db:
                if 'history' not in db:
                    db['history'] = []
                db['history'].append(f"{result:.2f}")

        print()

if __name__=="__main__":
    main()                                         

