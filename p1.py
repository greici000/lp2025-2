# Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota da prova 2 de um aluno.
# O programa deve imprimir o nome, a nota da prova 1, a nota da prova 2, a média das notas e uma das mendagens:
# "Aprovado," "Reprovado" ou "em Prova final".
def q1():
    nome = input('Digite o nome do aluno') 
    n1 = float(input('digite a primeira nota  prova 1: ')) # o float( tipo real) input(espera que o usuario digite um texto)
    n2 = float(input('Digite a segunda nota prova 2: '))

    media = (n1 + n2) / 2 # media = (variavel) e nota1(n1) + nota2(n2) para somar as notas e divide por 2 (/2)
    print('Resultado de {nome}') # pega o resultado da variavel nome.
    print('Média Final: {media:.2f}') #pega o resuldado da variavel media (.2f) define o numero de casas decimais que serao exibidas (duas casas) f significa que é do tipo float
    if media >= 7:
        print("Aluno: APROVADO!")
    elif media < 3:
        print("Aluno: REPROVADO.")
    else:
        print("Aluno: EM PROVA FINAL.")

# Crie um programa que permita entrar com o nome, a nota da prova 1 e da prova 2 de 15 alunos.
# Ao final, imprima uma listagem, contendo: nome, nota prova 1, nota prova 2, e média de cada aluno.
# Ao final, imprimir a média geral da turma.
def q2():
    Num_ALUNOS = 15
    
    soma_das_medias = 0.0

    for i in range(num_alunos):
        nome = input(f' Aluno {i+1} - Nome: ')
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))
        media = (n1 + n2) /2
        soma_das_medias += media
        print(f'{nome}: Média={media:.2f}')
    print(f'\nMédia Geral da Turma: {media_das_somas/num_alunos:.2f}')
# Crie um programa que leia asnotas de 'N' alunos de uma turma (onde 'N' é um numero fornecido pelo usuario.)
# Ao final, o programa deve calcular: a media da turma, o percentual de reprovados(considerando
# reprovação se a nota for inferior a 7.0).
def q3():
    print("--- Análise de Notas por Turma ---")
    num_alunos = int(input("Número de alunos da turma (0 para sair): "))
    if num_alunos <= 0: return

    soma_notas_turma = 0.0
    aprovados = 0
    for i in range(num_alunos):
        nota = float(input(f"Aluno {i+1} - Nota: "))
        soma_notas_turma += nota
        if nota >= 7.0:
            aprovados += 1
            
    media_turma = soma_notas_turma / num_alunos
    reprovados = num_alunos - aprovados
    percentual_reprovados = (reprovados / num_alunos) * 100
    
    print(f"Média da turma: {media_turma:.2f}")
    print(f"Percentual de reprovados: {percentual_reprovados:.2f}%")

# Faça um programa que calcule o valor de uma prestação em atraso. para isso, o programa deve ler o 
# valor da prestação vencida, a taxa periódica de juros e o peíodo de atraso. 
# Ao final, o programa deve imprimir o valor da prestação atrasada, o periodo de atraso,
# os juros que serão cobrados pelo período de atraso, e o valor da prestação acrescido dos juros 
def q4():
    valor_prestacao = float(input("Valor da prestação vencida: R$ "))
    taxa_juros = float(input("Taxa de juros (ex: 0.02 para 2%): "))
    periodo_atraso = float(input("Período de atraso: "))
    
    juros_cobrados = valor_prestacao * taxa_juros * periodo_atraso
    valor_final = valor_prestacao + juros_cobrados
    
    print(f"Juros cobrados: R${juros_cobrados:.2f}")
    print(f"Valor final: R${valor_final:.2f}")

# A campanhia de Emprétimos xxx só concede empréstimo se o valor da prestação não ultrapassar 
# 30% do salário bruto do proponente. Faça um programa que leia o sálario bruto e o valor da 
# prestação e, ao final, imprima se o empréstimo pode ou não ser concedido.
def q5():
    salario = float(input('Salário bruto: R$ '))
    prestacao = float(input('Valor da Prestação: R$ '))
    prestacao_maxima = salario * 0.3
    if prestacao > prestacao_maxima:
        print('Empréstimo não autorizado')
    else:
        print('Empréstimo autorizado')
    
# Faça um programa que calcule o reajuste do salário de um funcionário.
# Para isso, o programa deverá ler o salário atual do funcionario e ler o 
# percentual de reajuste. Ao final imprimir o valor do novo salário.
def q6():
    salario = float(input("Salário atual: R$ "))
    percentual_reajuste = float(input("Percentual do reajuste: "))
    reajuste = salario * (percentual_reajuste / 100)
    novo_salario = salario + reajuste
    print(f"Seu novo salário é: R$ {novo_salario:.2f}")

# Crie umprograma que possa ler um conjunto de pedidos de compra e calcule o valor total da compra.
# Cada pedido é composto pelos seguintes campos: número de pedido, data do pedido(dia,mês,ano)
# preço unitário, quantidade. O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
# como número do pedido.
def q7():
    total_compra_geral = 0.0
    print("Digite 0 como número do pedido para encerrar.")
    while True:
        num_pedido = int(input("\nNúmero do pedido (0 para sair): "))
        if num_pedido == 0:
            break
        preco_unitario = float(input("Preço unitário: "))
        quantidade = int(input("Quantidade: "))
        
        valor_pedido = preco_unitario * quantidade
        total_compra_geral += valor_pedido
        print(f"Pedido {num_pedido} - Valor Total: R$ {valor_pedido:.2f}")

#Faça um programa que leia dois números reais e calcule as quatro operações básicas entre estes
# dois números: adição, subtração, multiplicação e divisão. Ao final, o programa deve imprimir
# os resultados dos calcúlos.
def q8():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    adicao = numero1 + numero2
    multiplicao = numero1 * numero2
    print(f"Adição: {adicao}")
    print(f"Multiplicação: {multiplicao}")

# Faça um programa que efetue a apresentação do valor da conversão em real(R$) de um valor lido 
# em dólar(U$$). O programa deve solicitar a cotação do dalar atual para realizar o cálculo.
def q9():
    valor_dolar = float(input("Valor do dólar (US$): "))
    cotacao_dolar = float(input("Cotação do dólar para real (R$): "))
    valor_real = valor_dolar * cotacao_dolar
    print(f"O valor de US${valor_dolar:.2f} é R${valor_real:.2f}")

# uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores de consumo.
# para cada consumidor, são digitados os segintes dados: número do consumidor, quantidade de kWh 
# consumidos durante o mês, tipo (código) do consumidor (1- residencial, 2-comercial, 3-industrial)
# Os dados devem ser lidos até que seja encontrado o consumiidor com número 0(zero).
# O programa deve calcular e imprimir o custo total de cada consumidor.
def q10():
    PRECOS = {1: 0.30, 2: 0.50, 3: 0.70}
    print("Insira 0 no 'Número do consumidor' para finalizar.")
    while True:
        num_consumidor = int(input("\nNúmero do consumidor (0 para sair): "))
        if num_consumidor == 0:
            break
        consumo_kwh = float(input('Quantidade de kwh consumidos: '))
        tipo_consumidor = int(input('Tipo de consumidor (1, 2 ou 3): '))
        
        if tipo_consumidor in PRECOS:
            custo_total = consumo_kwh * PRECOS[tipo_consumidor]
            print(f'CUSTO TOTAL: R$ {custo_total:.2f}')
        else:
            print("Tipo de consumidor inválido.")


# Construa um programa que leia vários números e informe quantos números entre 100 e 200(inclusive)
# foram digitados. Quando o valor 0(zero) for lido, o algoritimo deverá cessar sua exeção.
def q11():
    contador = 0
    print("Digite 0 para encerrar.")
    while True:
        numero = int(input('Digite um número inteiro: '))
        if numero == 0:
            break
        if 100 <= numero <= 200:
            contador += 1
            
    print(f'Quantidade de números entre 100 e 200: {contador}')


# Faça um programa que leia um número inteiro entra 1 e 12 (referente a um mês do ano) e imprima
# na tela o nome do mês correspondente. Se o número digitado não estiver neste intervalo, o programa de ve imprimir "Mês Invalido!"
def q12():
    mes = int(input('Digite o número do mês: '))
    if mes == 1:
        print('Janeiro')
    elif mes == 2:
        print('Fevereiro')
    # ... continua até 12
    else:
        print('Mês Inválido!')



questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')
