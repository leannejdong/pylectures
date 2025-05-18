def add(n1, n2):
    return n1+n2
    
def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2 == 0:
        return "Cannot divide by zero!"
    else:
        return n1/n2
    
def calculator_interface():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
    choice = input("Enter your choice (1-5): ")

    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))
        elif choice == '3':
            print(num1, "*", num2, "=", subtract(num1,num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print("Thank you for using my calculator!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
        
if __name__ == "__main__"
    calculator_interface()
    
      

