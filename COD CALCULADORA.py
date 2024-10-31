#====CALCULADORA BINARIA=======


#BI PARA DECIMAL 
def binario_para_decimal(numero_binario):
    decimal = 0
    expoente = 0
    for digito in reversed(numero_binario):
        decimal += int(digito) * (2 ** expoente)
        expoente += 1
    return decimal

def binario_para_hexadecimal(numero_binario):
    while len(numero_binario) % 4 != 0:
        numero_binario = '0' + numero_binario
#CONVERSOES MANUAIS
    binario_para_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
                        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'} #NAO TEM COMO FUGIR DISSO ENTAO ELE SO CONVERTE E SEPARA 

    numero_hexadecimal = ''
    for i in range(0, len(numero_binario), 4):
        grupo_binario = numero_binario[i:i+4]
        numero_hexadecimal += binario_para_hex[grupo_binario]

    return numero_hexadecimal
#BI PARA OCTAL
def binario_para_octal(numero_binario):
    while len(numero_binario) % 3 != 0:
        numero_binario = '0' + numero_binario
#CONVERSOES MANUAIS
    binario_para_oct = {'000': '0', '001': '1', '010': '2', '011': '3',
                        '100': '4', '101': '5', '110': '6', '111': '7'}# MESMA COISA DO OUTRO

    numero_octal = ''
    for i in range(0, len(numero_binario), 3):
        grupo_binario = numero_binario[i:i+3]
        numero_octal += binario_para_oct[grupo_binario]

    return numero_octal
# DECIMAL PARA OCTAL
def decimal_para_octal(numero_decimal):
    octal = ''
    while numero_decimal > 0:
        resto = numero_decimal % 8
        octal = str(resto) + octal
        numero_decimal //= 8
    return octal
# DECIMAL PARA HEXADECIMAL
def decimal_para_hexadecimal(numero_decimal):
    hexa = ''
    while numero_decimal > 0:
        resto = numero_decimal % 16
        if resto < 10:
            hexa = str(resto) + hexa
        else:
            hexa = chr(55 + resto) + hexa #CONVERSAO PARA LETRAS 
        numero_decimal //= 16
    return hexa
#OCTAL PARA DECIMAL
def octal_para_decimal(numero_octal):
    decimal = 0
    expoente = 0
    for digito in reversed(numero_octal):
        decimal += int(digito) * (8 ** expoente)
        expoente += 1
    return decimal
#OCTAL PARA HEXA
def octal_para_hexadecimal(numero_octal):
    decimal = octal_para_decimal(numero_octal)
    return decimal_para_hexadecimal(decimal)
#HEXADECIMAL PARA DECIMAL
def hexadecimal_para_decimal(numero_hexadecimal):
    decimal = 0
    for digito in numero_hexadecimal:
        if digito.isdigit():
            valor = int(digito)
        else:
            valor = ord(digito.upper()) - 55 #LETRAS PARA NUMEROS PARA AI SIM CONVERTER
        decimal = decimal * 16 + valor
    return decimal
#HEXA PARA OCTAL
def hexadecimal_para_octal(numero_hexadecimal):
    decimal = hexadecimal_para_decimal(numero_hexadecimal)
    return decimal_para_octal(decimal)
#INTEIROS PARA BINARIO
def inteiro_para_binario(numero):
    if numero == 0:
        return '0'
    elif numero < 0:
        return "Número negativo. A conversão para binário não é suportada."

    binario = ''
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero //= 2

    return binario
#VERFICACAO DE NUMEROS 0 E 1 PARA NAO QUEBRAR O CODIGO NOS BINARIO
def verifica_binario(numero_binario):
    for digito in numero_binario:
        if digito not in '01':
            return False
    return True

def verifica_numero_inteiro(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False
#MENU DA CALCULADORA
def menu():
    while True:
        print("\n===== CALCULADORA (PIL) =====")
        print("1. Binário para Decimal")
        print("2. Binário para Hexadecimal")
        print("3. Binário para Octal")
        print("4. Decimal para Octal")
        print("5. Decimal para Hexadecimal")
        print("6. Octal para Decimal")
        print("7. Octal para Hexadecimal")
        print("8. Hexadecimal para Decimal")
        print("9. Hexadecimal para Octal")
        print("10. Inteiro para Binário")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero_binario = input("Digite um número binário: ")
            if verifica_binario(numero_binario): #VERIFICACAO
                print("O número decimal correspondente é:", binario_para_decimal(numero_binario))
            else:
                print("Número binário inválido! Por favor, digite apenas 0 e 1.")#CASO NAO TENHA 0 E 1
        elif opcao == "2":
            numero_binario = input("Digite um número binário: ")
            if verifica_binario(numero_binario): #VERIFICACAO
                print("O número hexadecimal correspondente é:", binario_para_hexadecimal(numero_binario))
            else:
                print("Número binário inválido! Por favor, digite apenas 0 e 1.")#CASO NAO TENHA 0 E 1
        elif opcao == "3":
            numero_binario = input("Digite um número binário: ")
            if verifica_binario(numero_binario): #VERIFICACAO
                print("O número octal correspondente é:", binario_para_octal(numero_binario))
            else:
                print("Número binário inválido! Por favor, digite apenas 0 e 1.")#CASO NAO TENHA 0 E 1
        elif opcao == "4":
            numero_decimal = int(input("Digite um número decimal: "))
            print("O número em octal é:", decimal_para_octal(numero_decimal))
        elif opcao == "5":
            numero_decimal = int(input("Digite um número decimal: "))
            print("O número em hexadecimal é:", decimal_para_hexadecimal(numero_decimal))
        elif opcao == "6":
            numero_octal = input("Digite um número octal: ")
            print("O número decimal correspondente é:", octal_para_decimal(numero_octal))
        elif opcao == "7":
            numero_octal = input("Digite um número octal: ")
            print("O número hexadecimal correspondente é:", octal_para_hexadecimal(numero_octal))
        elif opcao == "8":
            numero_hexadecimal = input("Digite um número hexadecimal: ")
            print("O número decimal correspondente é:", hexadecimal_para_decimal(numero_hexadecimal))
        elif opcao == "9":
            numero_hexadecimal = input("Digite um número hexadecimal: ")
            print("O número octal correspondente é:", hexadecimal_para_octal(numero_hexadecimal))
        elif opcao == "10":
            numero = input("Digite um número inteiro: ")
            if verifica_numero_inteiro(numero):
                print("O número binário correspondente é:", inteiro_para_binario(int(numero)))
            else:
                print("Número inválido! Por favor, digite um número inteiro.")
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")# CASO O PROGRAMA NAO ENCONTRE A OPCAO

menu() #FECHAMENTO DO MENU
