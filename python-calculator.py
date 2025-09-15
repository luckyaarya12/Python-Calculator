# Simple Calculator
# Menu

while True:
    print('Choose Operations 👇🏻')
    print('1.Addition ➕')
    print('2.Subtraction ➖')
    print('3.Multiplication ✖️')
    print('4.Division ➗')
    print('5.Percentage 📊')
    print('6.Exponentiation 🔼')
    print('7.Remainder ➗')
    print('8.FloorDivsion 🧮')
    print('9.SquareRoot √')
    print('10.Exit the Calculator 🚪')
    print()

    choice = input('👉 Operation Number(1-10):  ')
    
    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print('❌ Invalid Operation Number, Please Select Between 1 to 10 👇🏻')
    
    elif choice == '10':
        print('🚪 Exiting the Calculator. Thank You!')
        break

    # squareroot
    elif choice == '9':
        num = float(input('Enter the Number: '))
        print('SquareRoot:', round(num ** 0.5, 2))

    # addition
    elif choice == '1':
        a = float(input('Enter the First Number : '))
        b = float(input('Enter the Second Number : '))
        add = a + b
        print('Addition:', add)

    # subtraction
    elif choice == '2':
        a = float(input('Enter the First Number : '))
        b = float(input('Enter the Second Number : '))
        sub = a - b
        print('Subtraction:', sub)

    # multiplication
    elif choice == '3':
        a = float(input('Enter the First Number : '))
        b = float(input('Enter the Second Number : '))
        mul = a * b
        print('Multiplication:', mul)

    # division
    elif choice == '4':
        a = float(input('Enter the First Number : '))
        b = float(input('Enter the Second Number : '))
        if b != 0:
            div = a / b
            print('Division:', round(div, 2))
        else:
            print('Division is not allowed by zero')

    # percentage
    elif choice == '5':
        a = float(input('Enter the First Number : '))
        b = float(input('Enter the Second Number : '))
        if b != 0:
            per = a / b * 100
            print('Percentage:', round(per, 2))
        else:
            print('Division is not allowed by zero')

    # exponentiation
    elif choice == '6':
        a = float(input('Enter the First Number : '))
        b = float(input('Enter the Second Number : '))
        ex = a ** b
        print('Exponentiation:', ex)

    # remainder/modulo
    elif choice == '7':
        a = float(input('Enter the First Number : '))
        b = float(input('Enter the Second Number : '))
        if b != 0:
            rem = a % b
            print('Remainder:', rem)
        else:
            print('Division is not allowed by zero')

    # floordivision
    elif choice == '8':
        a = float(input('Enter the First Number : '))
        b = float(input('Enter the Second Number : '))
        if b != 0:
            fdiv = a // b
            print('Floordivision:', fdiv)
        else:
            print('Division is not allowed by zero')
