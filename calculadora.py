from funcao import Calculadora

calc = Calculadora()
while True:
    calc.print_menu()
    choice = input('Escolha sua opção: ')
    if choice == '5':
        break
    num1 = float(input('Primeiro numero : '))
    num2 = float(input('Segundo numero: '))

    if choice == '1':
        x = (calc.add(num1, num2))
        print(f'O resultado é {x}')
    elif choice == '2':
        x = (calc.subtract(num1, num2))
        print(f'O resultado é {x}')
    elif choice == '3':
        x = (calc.multiply(num1, num2))
        print(f'O resultado é {x}')
    elif choice == '4':
        x = (calc.divide(num1, num2))
        print(f'O resultado é {x}')
    else:
        print('Opção invalida')