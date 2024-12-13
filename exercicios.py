# #### Inteiros (`int`)

# # 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# numero_1 = int(input('Insira um número inteiro: '))
# numero_2 = int(input('Insira outro número inteiro: '))
# resultado = numero_1 + numero_2
# print(f'Soma dos dois números inteiros: {resultado}')
# print()

# # 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero = int(input('Insira um número inteiro: '))
# resultado = numero % 5
# print(f'Resto da divisão do número inteiro por 5: {resultado}')
# print()

# # 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# numero_1 = int(input('Insira um número inteiro: '))
# numero_2 = int(input('Insira outro número inteiro: '))
# resultado = numero_1 * numero_2
# print(f'Multiplicação dos dois números inteiros: {resultado}')
# print()

# # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# numero_1 = int(input('Insira um número inteiro: '))
# numero_2 = int(input('Insira outro número inteiro: '))
# resultado = numero_1 // numero_2
# print(f'Divisão inteira dos dois números inteiros: {resultado}')
# print()

# # 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero = int(input('Insira um número inteiro: '))
# resultado = numero ** 2
# print(f'Quadrado do número inteiro: {resultado}')
# print()

# #### Números de Ponto Flutuante (`float`)

# # 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero_1 = float(input('Insira um número flutuante: '))
# numero_2 = float(input('Insira outro número flutuante: '))
# resultado = numero_1 + numero_2
# print(f'Soma dos dois números flutuantes: {resultado}')
# print()

# # 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero_1 = float(input('Insira um número flutuante: '))
# numero_2 = float(input('Insira outro número flutuante: '))
# resultado = (numero_1 + numero_2) / 2
# print(f'Média dos dois números flutuantes: {resultado}')
# print()

# # 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# numero_1 = float(input('Insira a base da potência: '))
# numero_2 = float(input('Insira o expoente da potência: '))
# resultado = numero_1 ** numero_2
# print(f'{numero_1} elevado a {numero_2}: {resultado}')
# print()

# # 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# temperatura_celsius = float(input('Insira a temperatura, em Celsius: '))
# temperatura_fahrenheit = (temperatura_celsius * (9/5)) + 32
# print(f'{temperatura_celsius}°C = {temperatura_fahrenheit:.2f}°F')
# print()

# # 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math
# raio = float(input('Insira o raio do círculo: '))
# area = math.pi * raio**2
# print(f'Área do círculo, de raio {raio}: {area:.2f}')
# print()

# #### Strings (`str`)

# # 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# string = str(input('Insira uma string: '))
# string_maiuscula  = string.upper()
# print(f'String maiúscula: {string_maiuscula}')
# print()

# # 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = str(input('Insira seu nome completo: '))
# nome_minusculo  = nome.lower()
# print(f'Nome minúsculo: {nome_minusculo}')
# print()

# # 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = str(input('Insira uma frase: '))
# frase_sem_espaco  = frase.strip()
# print(f'Frase formatada: {frase_sem_espaco}')
# print()

# # 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = str(input('Insira uma data (formato "dd/mm/aaaa"): '))
# data = data.split('/')
# dia = data[0]
# mes = data[1]
# ano = data[2]
# print(f'Dia: {dia}')
# print(f'Mês: {mes}')
# print(f'Ano: {ano}')
# print()

# # 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# string_1 = str(input('Insira uma string: '))
# string_2 = str(input('Insira outra string: '))
# string_concatenada  = string_1 + string_2
# print(f'String concatenada: {string_concatenada}')
# print()


# #### Booleanos (`bool`)

# # 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# bool_1 = input('Insira um booleano (True ou False): ')
# bool_2 = input('Insira outro booleano (True ou False): ')
# def convert_bool(string):
#     if string == "True":
#         return True
#     else:
#         return False
# operacao_and = convert_bool(bool_1) and convert_bool(bool_2)
# print(f'Operação AND: {operacao_and}')
# print()

# # 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# bool_1 = input('Insira um booleano (True ou False): ')
# bool_2 = input('Insira outro booleano (True ou False): ')
# operacao_or = convert_bool(bool_1) or convert_bool(bool_2)
# print(f'Operação OR: {operacao_or}')
# print()

# # 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# bool_input = input('Insira um booleano (True ou False): ')
# bool_output = not convert_bool(bool_input)
# print(f'Booleano invertido: {bool_output}')
# print()

# # 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# num_1 = input('Insira um número: ')
# num_2 = input('Insira outro número: ')
# if num_1 == num_2:
#     print('Os números são iguais')
# else:
#     print('Os números são diferentes')
# print()

# # 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# num_1 = input('Insira um número: ')
# num_2 = input('Insira outro número: ')
# if num_1 != num_2:
#     print('Os números são diferentes')
# else:
#     print('Os números são iguais')
# print()

# #### try-except e if

# # 21: Conversor de Temperatura
# try:
#     temperatura_celsius = float(input("Insira a temperatura em Celsius: "))
#     temperatura_fahrenheit = (temperatura_celsius * (9/5)) + 32
#     print(f'A temperatura é Fahrenheit é {temperatura_fahrenheit}°F')
# except ValueError:
#     print('Insira um valor numérico.')
# print()

# # 22: Verificador de Palíndromo
# try:
#     frase = (input("Insira uma frase: "))
#     if isinstance(frase, str):
#         frase_ao_contrario = frase.replace(' ', '')[::-1]
#         if frase == frase_ao_contrario:
#             print(f'A frase "{frase}" é um palíndromo')
#         else:
#             print(f'A frase "{frase}" NÃO é um palíndromo')
# except not isinstance(frase, str):
#     print('Insira uma string.')
# print()

# # 23: Calculadora Simples
# try:
#     num_1 = float(input("Insira um número: "))
#     operador = input('Insira um operador (+, -, *, /): ')
#     num_2 = float(input("Insira outro número: "))
#     if operador == '+':
#         print(f'{num_1} {operador} {num_2} = {num_1 + num_2}')
#     elif operador == '-':
#         print(f'{num_1} {operador} {num_2} = {num_1 - num_2}')
#     elif operador == '*':
#         print(f'{num_1} {operador} {num_2} = {num_1 * num_2}')
#     elif operador == '/':
#         print(f'{num_1} {operador} {num_2} = {num_1 / num_2}')
#     else:
#         print('Operador inválido')
# except ZeroDivisionError:
#     print('Divisão por zero')
# except ValueError:
#     print('Insira um valor numérico')
# print()

# 24: Classificador de Números
try:
    num = float(input("Insira um número: "))
    if num > 0:
        info_1 = 'positivo'
    elif num < 0:
        info_1 = 'negativo'
    else:
        info_1 = 'zero'
    
    if num % 2 != 0:
        info_2 = 'ímpar'
    elif num == 0:
        info_2 = 'apenas'
    else:
        info_2 = 'par'
    
    print(f'O número {num} é {info_1} e {info_2}')
    
except ValueError:
    print('Insira um valor numérico')
print()

# 25: Conversão de Tipo com Validação
try:
    lista_texto = input("Insira uma lista de números inteiros separados por vírgula: ")
    lista_texto = lista_texto.split(',')
    lista_num = []
    for elemento in lista_texto:
        lista_num.append(int(elemento))
    print(lista_num)
except ValueError:
    print('Todos os valores da lista devem ser números inteiros')
print()