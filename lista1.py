'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome

print("greicielle")

#2. Faça um programa que imprima o produto dos valores 30 e 27.

print(30*27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.

print((5 + 8 + 12) / 3)

#4. Faça um programa que leia e imprima um número inteiro.

numero = int(input("Digitar numero inteiro: "))
print(" O número digitado é:", numero)

#5. Faça um programa que leia dois números reais e os imprima.

numero1 = float(input("Digite o primeiro número real: "))
numero2 = float(input("Digite o segundo número real: "))
print("Os números digitados são:", numero1, "e" , numero2)

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.

numero = int(input("Digite um número inteiro: "))
antecessor = numero - 1
sucessor = numero + 1
print("O número antecessor é:", antecessor)
print("O sucessor é:", sucessor)


#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.

nome = input("Digitar nome do cliente: ")
endereco = input("Digitar o endereço do cliente: ")
telefone = input("Digitar o telefone do cliente: ")

print("f\nDados do cliente: ")
print("Nome:", nome)
print("Endereço:", endereco)
print("Telefone:", telefone)

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles. 

numero1 = int(input("Digite primeiro número inteiro: "))
numero2 = int(input("Digitar segundo número inteiro: "))
subtracao = numero1 - numero2
print("A subtração é:", subtracao )

#9. Faça um programa que leia um número real e imprima ¼ deste número.


numero_real = float(input("Digite número real: "))
percentual = numero_real / 100
print(f"O percentual do número é: {percentual}")
      

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.

numero1 = float(input("Digite o primeiro número real: "))
numero2 = float(input("Digite o segundo número real: "))
numero3 = float(input("Digite o terceiro número real: "))
media = (numero1 + numero2 + numero3) / 3
print("A média é:", media)




#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.

numero1 = float(input("Digite o primeiro número real: "))
numero2 = float(input("Digite o sugundo número real: "))
adicao = numero1 + numero2
subtracao = numero1 - numero2
multiplicao = numero1 * numero2
divisao = numero1 / numero2
print("Adição:", adicao)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicao)
print("Divisão:", divisao)




#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.

numero = float(input("Digitar o número real: "))
quadrado = numero ** 2
print("O quadrado do número é:", quadrado)



#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.


saldo = float(input("Digite o saldo da conta: "))
reajuste = saldo * 0.02
novo_saldo = saldo + reajuste 
print("O novo saldo é:", novo_saldo)






#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
perimetro = (base * 2) + (altura * 2)
area = base * altura
print(" O perimetro do retângulo é:", perimetro)
print(" A área do retângulo é:", area)



#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.

valor_produto = float(input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto que deseja: "))
valor_desconto = valor_produto * (percentual_desconto / 100)
valor_final = valor_produto - valor_desconto
print("O valor do desconto é:", valor_desconto)
print("O valor final do produto é:", valor_final)




#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

salario = float(input("Digitar salário ataul: "))
percentual_reajuste = float(input("Digite o percentual do reajuste: "))
reajuste = salario * (percentual_reajuste / 100)
novo_salario = salario + reajuste
print(" Seu novo salário é:", novo_salario)




#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5


celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (9 * celsius + 160) / 5
print("A temperatura em Fahrenheit é:", fahrenheit)





#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem

tempo = float(input("Digite o tempo da viagem: "))
velocidade_media = float(input("Digite a velocidade em Km/h: "))
distancia = tempo * velocidade_media
litros_consumidos = distancia / 12
print("Distância percorrida é:", distancia, "km")
print("Litros de combustível consumidos:", litros_consumidos, "L")






#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.


valor_prestacao = float(input("Digite o valor da prestação vencida: "))
taxa_juros = float(input("Digite a taxa de juros (ex:0.02 para 2% ao mês): "))
periodo_atraso = float(input("Digite o período de atraso (em meses, dias): "))
juros_cobrados = valor_prestacao * taxa_juros * periodo_atraso
valor_final = valor_prestacao + juros_cobrados
print(f"\njuros a serem cobrados pelo período de atraso: R${juros_cobrados}")
print(f"valor da prestação acrescido dos juros: R${valor_final}")

      



      

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.

valor_dolar = float(input("Digite o valor do dólar (US$): "))
cotacao_dolar = float(input("Digite a cotação do dólar para real (R$): "))
valor_real = valor_dolar * cotacao_dolar
print(f"O valor de US${valor_dolar:} convertido para real é de R${valor_real}")






