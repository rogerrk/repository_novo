# mentorama exercicios
# Roger R. Kechichian (rogerrk@outlook.com)


# 1 Faça um programa que imprima seu nome completo na tela
import math

print("Roger Ribeiro Kechichian")


# 2 Escreva um programa que exiba o resultado de 5a x 3b onde a=2 e b=5
a = 2
b = 5
print((5 * a) * (3 * b))


# 3 Modifique o programa anterior, inserindo uma terceira variavel c=5 e impriima a soma das 3 variaveis
a = 2
b = 5
c = 5
print(a + b + c)


# 4 Escreva um programa que leia dois numeros e que pergunte qual operação voce deseja realizar.
# Voce deve poder calcular a soma, subtração, multiplicação e divisão. Exiba o resultado da operaçãoda.
a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))

soma = "soma"
subtração = "subtração"
multiplicação = "multiplicação"
divisão = "divisão"

operação = input("Qual operação voce deseja?: ")

if operação == "soma":
    print(a + b)

elif operação == "subtração":
    print(a - b)

elif operação == "multiplicação":
    print(a * b)

elif operação == "divisão":
    print(a / b)


# 5 Escreva um programa em Python para contar até 10
# 5a usando a instrução while
contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 1


# 5 Escreva um programa em Python para contar até 10
# 5b usando a instrução for e a função range
contador = 1
for elemento in range(1, 11):
    print(contador)
    contador = contador + 1


# 6 Escreva um programa para contar quantos números pares e ímpares existentes entre 1 e 10
# bem como a soma deles.
# 6a usando while
n = 1
somap = 0


while n <= 10:
    n += 1
    if n % 2 == 0:
        print(n)
        somap += n
print(somap)

y = 0
somai = 0

while y < 10:
    y += 1
    if y % 2 == 1:
        print(y)
        somai += y
print(somai)

print(somap + somai)


# 6b usando for, range e sum
par = []
impar = []

for p in range(1, 11):
    if p % 2 == 0:
        par += [p]
        print(p)

print(sum(par))

for i in range(1, 10):
    if i % 2 == 1:
        impar += [i]
        print(i)

print(sum(impar))

print(sum(par + impar))


# 7 Escreva um programa para resolver equações do segundo grau representadas por
# ax2+bx+c usando a Fórmula de Bhaskara
# 7a sem usar modulo math

a = float(input("Digite um número para A:  "))
b = float(input("Digite um número para B:  "))
c = float(input("Digite um número para C:  "))

delta = b ** 2 - 4 * a * c
print("delta = ", delta)

raizdelta = delta ** 0.5
print("raiz de delta = ", raizdelta)

r1 = (-b + raizdelta) / (2 * a)
print("r1 = ", r1)

r2 = (-b - raizdelta) / (2 * a)
print("r2 = ", r2)

# 7 Escreva um programa para resolver equações do segundo grau representadas por
# ax2+bx+c usando a Fórmula de Bhaskara
# 7b usando modulo math
import math

a = float(input("Digite um número para A:  "))
b = float(input("Digite um número para B:  "))
c = float(input("Digite um número para C:  "))


def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    print("Delta =  ", delta)
    if delta < 0:
        return None

    else:
        raizes = []
        m1 = math.sqrt(delta)
        r1 = (-b + m1) / (2 * a)
        raizes.append(r1)

        r2 = (-b - m1) / (2 * a)
        raizes.append(r2)

        print("R1 =  ", r1)
        print("R2 =  ", r2)
        return raizes


resultado = bhaskara(a, b, c)

# 8.Vamos reescrever o programa acima criando uma função bhaskara que recebe como
# parâmetros os coeficientes a, b e c e retorna as raízes da equação.
import math

a = float(input("Digite um número para A:  "))
b = float(input("Digite um número para B:  "))
c = float(input("Digite um número para C:  "))


def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    print("Delta =  ", delta)
    if delta < 0:
        return None

    else:
        raizes = []
        m1 = math.sqrt(delta)
        r1 = (-b + m1) / (2 * a)
        raizes.append(r1)

        r2 = (-b - m1) / (2 * a)
        raizes.append(r2)

        print("R1 =  ", r1)
        print("R2 =  ", r2)
        return raizes


resultado = bhaskara(a, b, c)


# Responda as questões a seguir:
# a)O que significam palavras reservadas em Python? (Palavras reservadas definem as regras e a estrutura da linguagem e não podem ser usadas como nomes de variáveis)
# a.1.Quais são as palavras reservadas no código acima? (def, return, if, import, else, none)
# b)Qual a função de cada uma dessas palavras reservadas no código?
# def: A palavra reservada def, na primeira linha, explicita a definição da função naquele ponto. ... Para executar a função, de forma semelhante ao que ocorre em outras linguagens, devemos simplesmente chamar seu nome e passar os parâmetros esperados entre parênteses, conforme o código a seguir.
# return: É uma instrução especial que você pode usar dentro de uma função ou método para enviar o resultado da função de volta ao chamador.
# if: O if é uma estrutura de condição que permite avaliar uma expressão e, de acordo com seu resultado, executar uma determinada ação.
# import: É uma linha com o caminho completo para o arquivo python que contem o módulo que se deseja importar, sem o sufixo py.
# else: O comando else é utilizado para executar um bloco de código, caso o resultado da expressão informada na instrução if seja falso. Lembrando que else só pode ser utilizada em conjunto com o if.
# none: None é nada, é a falta de valor.

# c)Implemente a função acima e mostre na tela,
# o resultado da equação de segundo grau.
# a=1,b=-5,c=6 (Delta = 1, R1 = 3.0, R2 = 2.0)
# a=1,b=0,c=-9 (Delta = 36, R1 = 3.0, R2 = -3.0)
# a=5,b=-45,c=0 (Delta = 2025, R1 = 9, R2 = 0)
# a=1,b=-1,c=-12 (Delta = 49, R1 = 4, R2 = -3)
# a=1,b=-6,c=10 (Delta = -4)


# 9 Considerando a string s = 'Mentorama' escreva um programa que:
# a) converta a string para maiúsculo, em seguida
# b) imprima-a de trás para frente
# c) imprima somente as vogais

s = "Mentorama"
maiuscula = s.upper()
invertida = maiuscula[::-1]


def vogais(string):
    for letra in string:
        if letra in "AEIOU":
            print(letra, end="  ")


print("a)", maiuscula)
print("b)", invertida)
print("c)", vogais(maiuscula))


# 10 Escreva um programa que recebe como entrada do usuario o nome "João"
# sobrenome " da Silva", idade " 25", Cidade " São Paulo", ddd "11", telefone "3333-3333",
# e faça as seguintes instruções:
# imprima na tela o nome completo em uma unica linha,
# imprima na tela o telefone com ddd em uma unica linha,
# imprima na tela a idade,
# imprima na tela a cidade,

nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = input("Idade: ")
cidade = input("Cidade: ")
ddd = input("DDD: ")
telefone = input("Telefone: ")

usuario = [nome, sobrenome, idade, cidade, ddd, telefone]

if "João" in usuario:
    print("Nome: ", nome + " " + sobrenome),   print("Telefone: ", "(", ddd, ")", telefone)
    print("Idade: ", idade)
    print("Cidade: ", cidade)

else:
    print("Usuário incoreto, tente outra vez!")
