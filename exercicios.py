#### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_1 = int(input('Insira um número inteiro: '))
numero_2 = int(input('Insira outro número inteiro: '))
resultado = numero_1 + numero_2
print(f'Soma dos dois números inteiros: {resultado}')
print()

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = int(input('Insira um número inteiro: '))
resultado = numero % 5
print(f'Resto da divisão do número inteiro por 5: {resultado}')
print()

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_1 = int(input('Insira um número inteiro: '))
numero_2 = int(input('Insira outro número inteiro: '))
resultado = numero_1 * numero_2
print(f'Multiplicação dos dois números inteiros: {resultado}')
print()

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_1 = int(input('Insira um número inteiro: '))
numero_2 = int(input('Insira outro número inteiro: '))
resultado = numero_1 // numero_2
print(f'Divisão inteira dos dois números inteiros: {resultado}')
print()

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input('Insira um número inteiro: '))
resultado = numero ** 2
print(f'Quadrado do número inteiro: {resultado}')
print()

#### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_1 = float(input('Insira um número flutuante: '))
numero_2 = float(input('Insira outro número flutuante: '))
resultado = numero_1 + numero_2
print(f'Soma dos dois números flutuantes: {resultado}')
print()

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_1 = float(input('Insira um número flutuante: '))
numero_2 = float(input('Insira outro número flutuante: '))
resultado = (numero_1 + numero_2) / 2
print(f'Média dos dois números flutuantes: {resultado}')
print()

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_1 = float(input('Insira a base da potência: '))
numero_2 = float(input('Insira o expoente da potência: '))
resultado = numero_1 ** numero_2
print(f'{numero_1} elevado a {numero_2}: {resultado}')
print()

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temperatura_celsius = float(input('Insira a temperatura, em Celsius: '))
temperatura_fahrenheit = (temperatura_celsius * (9/5)) + 32
print(f'{temperatura_celsius}°C = {temperatura_fahrenheit:.2f}°F')
print()

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
raio = float(input('Insira o raio do círculo: '))
area = math.pi * raio**2
print(f'Área do círculo, de raio {raio}: {area:.2f}')
print()

#### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string = str(input('Insira uma string: '))
string_maiuscula  = string.upper()
print(f'String maiúscula: {string_maiuscula}')
print()

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = str(input('Insira seu nome completo: '))
nome_maiusculo  = nome.upper()
print(f'Nome maiúsculo: {nome_maiusculo}')
print()

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = str(input('Insira uma frase: '))
frase_sem_espaco  = frase.strip()
print(f'Frase formatada: {frase_sem_espaco}')
print()

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = str(input('Insira uma data (formato "dd/mm/aaaa"): '))
data = data.split('/')
dia = data[0]
mes = data[1]
ano = data[2]
print(f'Dia: {dia}')
print(f'Mês: {mes}')
print(f'Ano: {ano}')
print()

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string_1 = str(input('Insira uma string: '))
string_2 = str(input('Insira outra string: '))
string_concatenada  = string_1 + string_2
print(f'String concatenada: {string_concatenada}')
print()


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação