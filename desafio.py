# Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas 
# para um número de ponto flutuante e prevenção de valores negativos para salário e bônus, você pode 
# modificar o código diretamente. Isso envolve adicionar verificações adicionais após a tentativa de 
# conversão para garantir que os valores sejam positivos.

nome = input('Qual o seu nome? ').strip().capitalize()

if any(caracter.isdigit() for caracter in nome):
    resposta = input('Você inseriu dígitos no seu nome, tem certeza que está correto? (S/N) ').lower()
    if resposta == 'n':
        exit()
elif len(nome) == 0:
    print('Você não digitou nada')
    exit()
        
try:
    salario = float(input('Qual o seu salário mensal? '))
    bonus = float(input('E o seu bônus recebido? '))
except ValueError:
    print('Insira um valor numérico.')
    exit()

if salario <= 0 or bonus <= 0:
    print('O valor do salário e/ou bônus não pode ser zero ou negativo.')
    exit()

kpi_bonus = 1000 + salario * bonus
kpi_bonus = round(kpi_bonus,2)

print(f'Olá, {nome}! O valor do seu bônus foi de {kpi_bonus} reais!')