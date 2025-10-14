'''
Lista de Exercícios referentes a estruturas de iteração (repetição)
'''

def exemploPara():
    for contador in range(10):
        print(contador, end=' ')
    print('')
    for contador in range(1,10):
        print(contador, end=' ')
    print('')
    for contador in range(1,10,2):
        print(contador, end=' ')

def exemploEnquanto():
    contador = 0
    while contador < 10:
        contador += 1               # equivale a contador = contador + 1
        if contador == 7:
            break                   # interrompe o laço
        if contador == 3:
            continue                # salta para a próxima iteração
        print(contador, end=' ')    # imprime sem quebra de linha

#1.Faça um programa que imprima todos os números de 1 até 100.
def q1():
    for numero in range(100):
        print(numero+1, end=' ')

#2. Faça um programa que imprima todos os números pares de 100 até 1.
def q2():
    for numero in range(100,1,-2):
        print(numero, end=' ')

#3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.
def q3():
    for numero in range(5,501,5):
        print(numero, end=' ')

#4. Faça um programa que permita entrar com o nome, a idade e o sexo de 20
#pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
#e tiver mais de 21 anos.
def q4():
    MAX = 20
    for pessoa in range(MAX):
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        sexo = input('Sexo(M/F): ')
        if sexo.upper() == 'M' and idade >= 21:
            print(nome)

#5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
#sucessivas, crie um programa que calcule o produto de dois números inteiros
#lidos. Suponha que os números lidos sejam positivos.
def q5():
    num1 = int(input('Multiplicador: '))
    num2 = int(input('Multiplicando: '))
    soma = 0
    for _ in range(num1):
        soma = soma + num2
    print(f'{num1}*{num2}={soma}')

#6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
#Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
#a partir da soma dos anteriores. Exemplo:
#• 1 + 1 = 2, terceiro termo;
#• 1 + 2 = 3, quarto termo, etc.
# 1 1 2 3 5 8 13 21
def q6():
    ant = 0  
    atu = 1  
    for _ in range(20):
        print(atu, end=' ')
        prox = ant + atu  
        ant = atu
        atu = prox

#7. Crie um programa que permita entrar com o nome, a nota da
#prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
#nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
#imprimir a média geral da turma.
def q7():
    resultado = "NOME\tN1\tN2\tMEDIA\n"
    MAX = 3
    media_turma = 0
    for _ in range(MAX):
        nome = input('Nome: ')
        n1 = round(float(input('Nota 1: ')),1)
        n2 = round(float(input('Nota 2: ')),1)
        media = round((n1 + n2) / 2,1)
        media_turma += media
        resultado += f'{nome}\t{n1}\t{n2}\t{media}\n'
    print(resultado)
    print(f'Média da Turma: {round(media_turma/MAX,1)}')

#8. Faça um programa que permita entrar com o nome e o salário bruto de 10 pessoas.
#Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
#calculado conforme a tabela a seguir:
#Salário IRPF
#Salário menor que R$1300,00 Isento
#Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
#Salário maior ou igual a R$2300,00 15% do salário bruto
def q8():
    num_de_pessoas = 10
    print('Cálculo do imposto de renda (IRPF) para 10 pessoas')
    for i in range(num_de_pessoas):
        nome = input(f'pessoa {i + 1}: Digitar o nome:')
        salario_bruto = float(input(f"Pessoa {i + 1}: Digitar o salário bruto: R$ "))
        aliquota = 0.0
        if salario_bruto < 1300.00:
            aliquota = 0.0
        elif salario_bruto < 2300.00:
            aliquota = 0.10
        else:
            aliquota = 0.15
        valor_irpf = salario_bruto * aliquota
        print("-" * 30)
        print(f'Nome: {nome}')
        print(f'Salário Bruto: R$ {salario_bruto:.2f}')
        if aliquota == 0.0:
            print('IRPF: ISENTO')
        else:
            print(f'Alíquota: {aliquota * 100:.0f}%')
            print(f'Valor do IRPF a ser pago: R$ {valor_irpf:.2f}')
        print("-" * 30)



#9. No dia da estreia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados.
def q9():
    num_de_espectadores = 20
    
    soma_idade_excelente = 0
    quantidade_excelente = 0
    quantidade_regular = 0
    quantidade_bom = 0
    print('Pesquisa de Opinião  "Procurando Dory" para 20 pessoas')
    for i in range(num_de_espectadores):
        print(f'\n Espectador {i + 1} de {num_de_espectadores}')
        idade = int(input('Digite a idade: '))
        while True:
            opiniao = input('Digite a opinião (3-excelente; 2-bom; 1-regular):')
            if opiniao in ('1','2','3'):
                break
            print('Opinião inválida. Digite 1, 2 ou 3')
        if opiniao == '3':
            quantidade_excelente += 1
            soma_idade_excelente += idade
        elif opiniao == '2':
            quantidade_bom += 1
        elif opiniao == '1':
            quantidade_regular += 1
        print('\n' + '=' * 50)
        print('RESULTADOS DA PESQUISA')
        print('=' * 50)
        if quantidade_excelente > 0:
            media_idade = soma_idade_excelente / quantidade_excelente
            print(f'A média das idades das pessoas que rspondeiram excelente: {media_idade:.1f} anos')
        else:
            print('Nenhuma pessoa respondeu "Excelente" ')
        print(f'A quantidades de pessoas que respondeiram regular:{quantidade_regular}')
        if num_de_espectadores > 0:
            porcentagem_bom = (quantidade_bom / num_de_espectadores) * 100
            print(f'A porcentagem de pessoas que responderam bom: {porcentagem_bom:.2f}%')
        else:
            print('Não houve espectadores para análise.')

#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos times;
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.
def q10():
    PAISES=3
    JOGADORES=3
    soma_peso = 0
    soma_idade = 0
    for pais in range(PAISES):
        print(f'País: {pais}')
        soma_peso_pais = 0
        soma_idade_pais = 0
        for _ in range(JOGADORES):
            idade = int(input('Idade: '))
            peso = int(input('Peso: '))
            soma_peso_pais += peso
            soma_idade_pais += idade
            soma_peso += peso
            soma_idade += idade
        print(f'Idade média: {soma_idade_pais/JOGADORES}')
        print(f'Peso médio: {soma_peso_pais/JOGADORES}')
    print(f'Idade média geral: {soma_idade/JOGADORES*PAISES}')
    print(f'Peso médio geral: {soma_peso/JOGADORES*PAISES}')

#11. Construa um programa que leia vários números e informe quantos números
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
#deverá cessar sua execução.
def q11():
    conatdo = 0
    while True:
        numero = random.randrange(201)
        print(numero, end=' ')
        contador +=1 if numero >= 100 and numero <= 200 else 0
        if numero == 0:
            break
        print(f'\nqtde de números entre 100 e 200: {contador}')

#12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
#ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
#ano, fazer um programa que calcule e imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.
def q12():

    populacao_a = 5000000
    taxa_a = 0.03
    populacao_b = 7000000
    taxa_b = 0.02
    anos = 0
    print("--- Simulação de Crescimento Populacional ---")
    while populacao_a <= populacao_b:
        populacao_a *= (1 + taxa_a)
        populacao_b *= (1 + taxa_b)

        if populacao_a <= populacao_b:
            anos += 1
        else:
            anos += 1
            break

    print(f"Resultado: {anos+ 1} anos")
    print(f"População final após {anos +1} anos")
    print(f"País A: {int(populacao_a):,} habitantes") 
    print(f"País B: {int(populacao_b):,} habitantes")


def q112():
    paísA = 5_000_000
    paísB = 7_000_000
    ano = 0
    while paísA < paísB:
        ano += 1
        paísA += 1.02
        paísB += 1.03
    print (f'se passaram {ano} anos para o país A ultrapassar o país B')
    print(f'população do pais A: {paísA}')
    print(f'população do país B: {paísB}')   
#13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
#de consumo. Para cada consumidor, são digitados os seguintes dados:
#• número do consumidor
#• quantidade de kWh consumidos durante o mês
#• tipo (código) do consumidor
#1-residencial, preço em reais por kWh = 0,3
#2-comercial, preço em reais por kWh = 0,5
#3-industrial, preço em reais por kWh = 0,7
#Os dados devem ser lidos até que seja encontrado o consumidor com número 0
#(zero). O programa deve calcular e imprimir:
#• O custo total para cada consumidor
#• O total de consumo para os três tipos de consumidor
#• A média de consumo dos tipos 1 e 2
def q13():
    print('Cálculo de consumo de Energia Elétrica')
    print('Insira 0 no "Número do consumidor" para finalizar a leitura.\n')
    PRECOS = {
        1: 0.30,
        2: 0.50,
        3: 0.70
    }

    dados_consumo = {
        1: {'total_kwh': 0, 'contador': 0, 'nome': 'Residencial'},
        2: {'total_kwh': 0, 'contador': 0, 'nome': 'Comercial'},
        3: {'total_kwh': 0, 'contador': 0, 'nome': 'Indrustrial'},
    }

    while True:
        try:
            num_consumidor = int(input("Número do consumidor (0 para sair):"))
            if num_consumidor == 0:
                break
            consumo_kwh = float(input('Quantidade de kwh consumidos: "'))
            tipo_consumidor = int(input('tipo de consumidor (1,2 o 3)'))
            if tipo_consumidor not in PRECOS or consumo_kwh < 0:
                print("\nERRO: Tipo ou consumo inválido. Tente novamente.\n")
                continue

            preco_unitario = PRECOS[tipo_consumidor]
            custo_total = consumo_kwh * preco_unitario

            print(f'CUSTO TOTAL para o consumidor {num_consumidor}: R$ {custo_total:.2f\n}')

            dados_consumo[tipo_consumidor]['tatal_kwh'] += consumo_kwh
            dados_consumo[tipo_consumidor]['contador'] += 1
        except ValueError:
            print('\nErro: Entrada inválida. Digite números.\n')
    print('\n' + '='*40)
    print('RESUMO DOS DADOS GERAIS')
    print('='*40)

    print('Média de consumo (tipos 1 e 2):')
    for tipo in [1,2]:
        dados = dados_consumo[TIPO]
        nome = dados['nome']
        if dados['contador'] > 0:
            media = dados['total_kwh'] / dados['contador']
            print(f' -{nomes}: {media:.2f} kwh (baseado em {dados['contador']}clientes)')
        else:
            print(f' -{nome}: Não houve registros para cálculo.')
#14. Faça um programa que leia vários números inteiros e apresente o fatorial de cada
#número. O algoritmo encerra quando se digita um número menor do que 1.n
def q14():  
    print('Calculo fatorial')
    print('Digitar numero inteiro. Se você digitar um numero menor que 1 o programa se encerra')
    
    while True:
        try :
            numero = int(input('Digite um número inteiro: '))
        except ValueError:
            print('Entrada inválida. digite um número inteiro.')
            continue
        if numero < 1:
            print("Encerrando o cálculo numero menor que 1 digitado")
            break
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        print(f'O FATORIAL de {numero}! é: {fatorial}\n')


        
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1)


def q114():
    n = 1
    while n != 0:
        n = int(input("Digite o número para cálcular: "))
        print(fatorial(n))


#15. Faça um programa que permita entrar com a idade de várias pessoas e
#imprima:
#• total de pessoas com menos de 21 anos
#• total de pessoas com mais de 50 anos
def q15():
    print('Contagem por idade')
    print('Para encerrar o programa digite 0 ou um numero negativo.')

    cont_menor_21 = 0
    cont_maior_50 = 0

    while True:
        try:
            idade = int(input('Digite a idade: '))
        except ValueError:
            print("Entrada inválida. digite um numero inteiro.")
            continue
        if idade <= 0:
            break
        if idade < 21:
            cont_menor_21 += 1
        elif idade > 50:
            cont_maior_50 += 1
    print('\n Resultados')
    print(f'Total de pessoas com menos de 21 anos: {cont_menor_21}')
    print(f'Total de pessoas com mais de 50 anos: {cont_maior_50}')


#16. Sabendo-se que a unidade lógica e aritmética calcula a divisão por meio de subtrações
#sucessivas, criar um algoritmo que calcule e imprima o resto da divisão de
#números inteiros lidos. Para isso, basta subtrair o divisor ao dividendo, sucessivamente,
#até que o resultado seja menor do que o divisor. O número de subtrações
#realizadas corresponde ao quociente inteiro e o valor restante da subtração corresponde
#ao resto. Suponha que os números lidos sejam positivos e que o dividendo
#seja maior do que o divisor.
#Exemplo:
#  10 / 5
#  10 é o Dividendo
#  5 é o Divisor
#  2 é o Quociente (resultado inteiro da divisão)
#  0 é o Resto da Divisão
def q16():
    print(" Divisão por Subtrações Sucessivas")
    
    try:
        dividendo = int(input("Digite o Dividendo (maior que o divisor): "))
        divisor = int(input("Digite o Divisor (positivo): "))
    except ValueError:
        print("Entrada inválida. Digite números inteiros.")
        return

    if divisor <= 0:
        print("Erro: O divisor deve ser positivo.")
        return
    if dividendo < divisor:
        print("Erro: O Dividendo deve ser maior ou igual ao Divisor para este método.")
        return
        
    quociente = 0
    resto = dividendo 
    
    while resto >= divisor:
        resto -= divisor    
        quociente += 1      
    
    print(f"\nDivisão de {dividendo} por {divisor}:")
    print(f"Quociente (Número de subtrações): {quociente}")
    print(f"Resto da Divisão: {resto}")



#17. Crie um programa que possa ler um conjunto de pedidos de compra e
#calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#• número de pedido
#• data do pedido (dia, mês, ano)
#• preço unitário
#• quantidade
#O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
#como número do pedido.
def q17():
    print("--- Cálculo do Valor Total de Compras ---")
    print("Digite 0 como número do pedido para encerrar.")

    total_compra_geral = 0.0
    
    while True:
        try:
            
            num_pedido = int(input("\nNúmero do pedido (0 para sair): "))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue
            
    
        if num_pedido == 0:
            break
            
        
        
        try:
            
            preco_unitario = float(input("Preço unitário: "))
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Valores inválidos para preço ou quantidade. Pedido ignorado.")
            continue
        
        
        valor_pedido = preco_unitario * quantidade
        
        
        total_compra_geral += valor_pedido
        
        print(f"Pedido {num_pedido} - Valor Total: R$ {valor_pedido:.2f}")
            
    print("\n Resultado Final")
    print(f"O valor total de todas as compras foi: R$ {total_compra_geral:.2f}")


    
#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça um programa que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
#número da conta.
def q18():
    print("--- Cálculo do Faturamento da Pousada ---")
    print("Digite 0 como número da conta para encerrar.")
    
    total_faturado_pousada = 0.0
    
    while True:
        try:
            
            num_conta = int(input("\nNúmero da Conta (0 para sair): "))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue
            
        
        if num_conta == 0:
            break
            
        
        nome = input("Nome do Cliente: ")
        try:
            num_dias = int(input("Número de dias hospedados: "))
        except ValueError:
            print("Entrada inválida para número de dias. Cliente ignorado.")
            continue

        
        if num_dias < 10:
            taxa_servico = 15.00
        else:
            taxa_servico = 8.00
            
        
        custo_diarias = num_dias * 30.00
        custo_servicos = num_dias * taxa_servico
        conta_cliente = custo_diarias + custo_servicos
        
        
        total_faturado_pousada += conta_cliente
        
        print(f"\nResumo da Conta {num_conta} - {nome}:")
        print(f"Total de Diárias ({num_dias} dias): R$ {custo_diarias:.2f}")
        print(f"Total de Serviços: R$ {custo_servicos:.2f}")
        print(f"CONTA FINAL: R$ {conta_cliente:.2f}")
            
    print("\n--- Faturamento Total da Pousada ---")
    print(f"O total faturado pela pousada foi: R$ {total_faturado_pousada:.2f}")



#19. Em uma Universidade, os alunos das turmas de informática fizeram uma prova
#de algoritmos. Cada turma possui um número de alunos. Criar um programa que
#imprima:
#• quantidade de alunos aprovados;
#• média de cada turma;
#• percentual de reprovados.
#Obs.: Considere aprovado com nota >= 7.0
def q19():
    print("--- Análise de Notas por Turma ---")
    print("Digite 0 para o número de alunos para encerrar o programa.")

    while True:
        try:
            num_alunos = int(input("\nDigite o número de alunos da turma (0 para sair): "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue
            
        if num_alunos == 0:
            break
            
        if num_alunos < 0:
            print("O número de alunos não pode ser negativo.")
            continue
        
        
        soma_notas_turma = 0.0
        aprovados = 0
        
        
        for i in range(num_alunos):
            print(f"--- Aluno {i+1} ---")
            try:
                nota = float(input("Nota do aluno (0.0 a 10.0): "))
            except ValueError:
                print("Nota inválida. Aluno ignorado.")
                continue

            soma_notas_turma += nota
            
            
            if nota >= 7.0:
                aprovados += 1
                
         
        if num_alunos > 0:
            media_turma = soma_notas_turma / num_alunos
            reprovados = num_alunos - aprovados
            
            
            percentual_reprovados = (reprovados / num_alunos) * 100
            
            print("\n--- Resultados da Turma ---")
            print(f"Quantidade de alunos aprovados: {aprovados}")
            print(f"Média da turma: {media_turma:.2f}")
            print(f"Percentual de reprovados: {percentual_reprovados:.2f}%")
        else:
            print("Turma sem alunos. Pulando os cálculos.")



#20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:
#• Qual o seu time de coração?
#1-Fluminense;
#2-Botafogo;
#3-Vasco;
#4-Flamengo;
#5-Outros
#• Onde você mora?
#1-RJ;
#2-Niterói;
#3-Outros
#• Qual o seu salário?
#Faça um programa que imprima:
#• o número de torcedores por clube;
#• a média salarial dos torcedores do Botafogo;
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#3.12. Exercícios da Aula 73
#Obs.: O programa encerra quando se digita 0 para o time.
def q20():
    print(" Pesquisa de Audiência e Salário ")
    print("Digite 0 para o time do coração para encerrar.")
    
    
    total_entrevistados = 0
    
    
    cont_times = [0, 0, 0, 0, 0]
    nomes_times = ["Fluminense", "Botafogo", "Vasco", "Flamengo", "Outros"]
    
    
    soma_salario_botafogo = 0.0
    cont_botafogo = 0 
    
    
    cont_rj_outros_clubes = 0
    cont_niteroi_fluminense = 0

    while True:
        try:
            
            time = int(input("\nTime (1 a 5, ou 0 para sair): "))
        except ValueError:
            print("Entrada inválida para o time.")
            continue
            
        
        if time == 0:
            break
            
        if time < 1 or time > 5:
            print("Código de time inválido. Tente novamente.")
            continue
            
        
        try:
            
            moradia = int(input("Moradia (1-RJ, 2-Niterói, 3-Outros): "))
            salario = float(input("Salário: "))
        except ValueError:
            print("Entrada inválida para moradia ou salário. Entrevistado ignorado.")
            continue
            
        
        total_entrevistados += 1
        
        
        
        
        cont_times[time - 1] += 1
        
        
        if time == 2:
            soma_salario_botafogo += salario
            cont_botafogo += 1
            
        
        if moradia == 1 and time == 5:
            cont_rj_outros_clubes += 1
            
        
        if moradia == 2 and time == 1:
            cont_niteroi_fluminense += 1

    print("\n--- Resultados da Pesquisa ---")
    
    
    print("Número de torcedores por clube:")
    for i in range(len(cont_times)):
        print(f"  {nomes_times[i]}: {cont_times[i]}")
        
    
    media_botafogo = soma_salario_botafogo / cont_botafogo if cont_botafogo > 0 else 0
    print(f"\nMédia salarial dos torcedores do Botafogo: R$ {media_botafogo:.2f}")
    
    
    print(f"Pessoas moradoras do RJ, torcedores de outros clubes: {cont_rj_outros_clubes}")
    
    
    print(f"Pessoas de Niterói, torcedoras do Fluminense: {cont_niteroi_fluminense}")


#21. Em uma universidade cada aluno possui os seguintes dados:
#• Renda pessoal;
#• Renda familiar;
#• Total gasto com alimentação;
#• Total gasto com outras despesas;
#Faça um programa que imprima a porcentagem dos alunos que gasta acima de
#R$200,00 com outras despesas. O número de alunos com renda pessoal maior
#que a renda familiar e a porcentagem gasta com alimentação e outras despesas
#em relação às rendas pessoal e familiar.
#Obs.: O programa encerra quando se digita 0 para a renda pessoal.

#22. Crie um programa que ajude o DETRAN a saber o total de recursos que foram
#arrecadados com a aplicação de multas de trânsito.
#O algoritmo deve ler as seguintes informações para cada motorista:
#• número da carteira de motorista (de 1 a 4327);
#• número de multas;
#• valor de cada uma das multas.
#Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o
#total de recursos arrecadados (somatório de todas as multas). O programa deverá
#imprimir também o número da carteira do motorista que obteve o maior número
#de multas.
#Obs.: O programa encerra ao ler a carteira de motorista de valor 0.

#23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
#e altura) dos atletas que participaram de uma olimpíada, e informar:
#• a atleta do sexo feminino mais alta;
#• o atleta do sexo masculino mais pesado;
#• a média de idade dos atletas.
#Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
#atleta.
#Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
#como comparação e atribuição de textos.

#24. Faça um programa que calcule quantos litros de gasolina são usados em uma
#viagem, sabendo que um carro faz 10 km/litro. O usuário fornecerá a velocidade
#do carro e o período de tempo que viaja nesta velocidade para cada trecho do
#percurso. Então, usando as fórmulas distância = tempo x velocidade e litros
#consumidos = distância / 10, o programa computará, para todos os valores não negativos
#de velocidade, os litros de combustível consumidos. O programa deverá
#imprimir a distância e o número de litros de combustível gastos naquele trecho.
#Deverá imprimir também o total de litros gastos na viagem. O programa encerra
#quando o usuário informar um valor negativo de velocidade.
#74 Aula 3. Estruturas de Iteração

#25. Faça um programa que calcule o imposto de renda de um grupo de contribuintes,
#considerando que:
#a) os dados de cada contribuinte (CIC, número de dependentes e renda bruta
#anual) serão fornecidos pelo usuário via teclado;
#b) para cada contribuinte será feito um abatimento de R$600 por dependente;
#c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes
#da renda bruta anual;
#d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela
#a seguir:
#Renda Líquida Imposto
#até R$1000 Isento
#de R$1001 a R$5000 15%
#acima de R$5000 25%
#e) o valor de CIC igual a zero indica final de dados;
#f ) o programa deverá imprimir, para cada contribuinte, o número do CIC e o
#imposto a ser pago;
#g) ao final o programa deverá imprimir o total do imposto arrecadado pela
#Receita Federal e o número de contribuintes isentos;
#h) leve em consideração o fato de o primeiro CIC informado poder ser zero.

#26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em um determinado dia. Para cada casa visitada foram fornecidos o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
#naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
#casa não entraria na pesquisa. Criar um programa que:
#• Leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#• Calcule e imprima a porcentagem de audiência em cada canal.
#Obs.: Para encerrar a entrada de dados, digite o número do canal zero.

#27. Crie um programa que calcule e imprima o CR do período para os alunos de
#computação. Para cada aluno, o algoritmo deverá ler:
#• número da matrícula;
#• quantidade de disciplinas cursadas;
#• notas em cada disciplina;
#Além do CR de cada aluno, o programa deve imprimir o melhor CR dos
#alunos que cursaram 5 ou mais disciplinas.
#• fim da entrada de dados é marcada por uma matrícula inválida (matrículas
#válidas de 1 a 5000);
#• CR do aluno é igual à média aritmética de suas notas.

#28. Construa um programa que receba a idade, a altura e o peso de várias pessoas,
#Calcule e imprima:
#• a quantidade de pessoas com idade superior a 50 anos;
#• a média das alturas das pessoas com idade entre 10 e 20 anos;
#• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
#pessoas analisadas.

#29. Construa um programa que receba o valor e o código de várias mercadorias
#vendidas em um determinado dia. Os códigos obedecem a lista a seguir:
#L-limpeza
#A-Alimentação
#H-Higiene
#Calcule e imprima:
#• o total vendido naquele dia, com todos os códigos juntos;
#• o total vendido naquele dia em cada um dos códigos.
#Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.

#30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, V-viúvo
#e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
#• a quantidade de pessoas casadas;
#• a quantidade de pessoas solteiras;
#• a média das idades das pessoas viúvas;
#• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
#analisadas.
#Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a
#idade.

questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')