'''
Exercícios sobre os comandos de condição em python
'''
def cabecalho(titulo):
    print('========================================')
    print(f'============= {titulo} ===============')
    print('========================================')




def exemploSe():
    idade = int(input('Idade:'))
    if idade >= 18:
        print('Maior de idade')

def exemploSeSenao():
    idade = int(input('Idade:'))
    if idade >= 18:
        print('Maior de idade')    
    else:
        print('Menor de idade')
    print('fim do programa')

def exemploSe_SenaoSe_Senao():
    idade = int(input('Idade:'))
    if idade < 18:
        print('Menor de idade')    
    elif idade < 65:
        print('Maior de idade')
    elif idade < 50:
        print('Pessoa madura')
    else:
        print('Idoso')
    print('fim do programa')

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
     cabecalho('QUESTÃO 1')
   
    valor1 = int(input("Digitar o Primeiro valor: "))
    valor2 = int(input(" Digitar o segundo valor: "))
    soma = valor1 + valor2
    if soma > 10:
        print(f" A soma é :{soma} ")



#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q2():
     cabecalho('QUESTÃO 2')
    valor1 = int(input(" Digite o primeiro valor: "))
    valor2 = int(input(" Digite o segundo valor: "))
    soma = valor + valor2 
    if soma > 20 : 
        resultado = soma + 8 
    else: 
        resultado = soma -5 
    print(f " O resultado final é : {resultado}")

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
     cabecalho('QUESTÃO 3')
    numero= int(input("Digite um número: "))

    if numero % 3 == 0: 
        print("É múltiplo de 3")
    else: 
        print("não é múltiplo de 3")

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q4():
     cabecalho('QUESTÃO 4')
    num = int(entrada('Digite um inteiro: '))
    if num % 5 == 0:
        imprimir('É divisível por 5')
    else:
        imprimir('Não é divisível por 5')

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q5():
     cabecalho('QUESTÃO 5')
    numero = int(input("Digite um número: ")

    if numero % 3 == 0 and numero % 7 == 0
        print(" É divisível por 3 e por 7 ")
                 else: 
                 print( " não é divisível por 3 é por 7 ")

                 
#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q6(): 
     cabecalho('QUESTÃO 6')
    salário = flutuador(entrada('Salário bruto: R$ '))
    prestação = flutuador(entrada('Prestação para autorizar: R$'))
    prestacao_maxima = salário * 0,3
    if prestação > prestacao_maxima:
        imprimir('Empresa não autorizada')
    else: 
        imprimir('Empresa autorizada')
        
                 
#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q7():
     cabecalho('QUESTÃO 7')
    numero = int(input(" Digite um número: "))
    if numero > 20 and numero < 50: 
        print ( " O número está entre 20 e 50.")
    else:
        print ( " O número Não está entre 20 e 50.")

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q8():
     cabecalho('QUESTÃO 8')
    num = int(entrada('Número inteiro: '))
    if num < 20:
        imprimir('É menor do que 20')
    elif num > 20:
        imprimir('É maior que 20')
    else:
        imprimir('É igual a 20')

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q9():
     cabecalho('QUESTÃO 9')
    ano_nasc = int(entrada('Ano de nascimento:'))
    ano_atual = int(entrada('Ano atual: '))
if ano_nasc > ano_atual:
    imprimir('ERRO: Não pode ter nascido no futudo')
else: 
    imprimir(f'Idade:{ano_atual - ano_nasc}anos')

def q91()
dados_str = entrada('Dados de nascimento (dd/mm/aaaa): ')
imprimir(f'Ano atual:{data e hora.tempo de luta(HOJE,"%Y")}')
data_nascimento = data e hora.tempo de folga(dados_str, '%d/%m/%Y')
if data_nascimento > HOJE:
    imprimir('Data de nascimento inválida!')
else:
    imprimir(f'Idade:{int((HOJE - data_nascimento).dias/365)}anos.')
#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
     cabecalho('QUESTÃO 10')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

numeros = [num1, num2, num3]
numero.sort()
imprima('os números em ordem crescente são:', numeros)
        
#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
   cabecalho('QUESTÃO 11')
num1 = int(input('Digite primeiro número: '))
num2 = int(input('Digite segundo número: '))
num3 = int(input('Digite terceiro número: '))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3
#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos
def q12():
     cabecalho('QUESTÃO 12')
    idade = int(input(" Digite a idade: "))
    if idade >= 18 : 
        print(" Maior de idade")
    if idade < 18 : 
        print( " Menor de idade")
    if idade > 65 : 
        print( " Maior de 65 anos")
        

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final
def q13():
     cabecalho('QUESTÃO 13')
    nome = input('Digitar nome do aluno')
    nota1 = int(input('Digitar nota primeiro prova'))
    nota2 = int(input('Digitar nota segunda prova'))
 
    media = (nota1 + nota2 ) / 2
    print(f"NOME: {nota1}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Média: {media}")

if media >= 7:
    print("Aprovado")
elif media < 3:
    print("Reprovado")
else:
    print("Em prova final") 

 


#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
def q14():
     cabecalho('QUESTÃO 14')
    salario = float(input("Digite o valor do salário: R$ "))
    desconto_inss = 0

    if salario <= 600:
        desconto_inss = 0
    elif salario <= 1200:
        desconto_inss = salario * 0.20
    elif salario <= 2000:
        desconto_inss salario * 0.25
    else:
        desconto_inss = salario *0.30

    print(f"Salário: R$ {salario:.2f}")
    print(f"Desconto do INSS: R$ {desconto_inss:.2f}")        

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
def q15():
     cabecalho('QUESTÃO 15')
    valor_compra = float(input("Digitar valor do produto: R$ "))
    lucro = 0
    if valor_compra < 20:
        lucro = valor_compra * 0.45
    else:
        lucro = valor_compra * 0.30

    valor_venda = valor_compra + lucro
    print(f"valor da compra: R$ {valor_copra:.2f}")
    print(f"Valor da venda: R$ {valor_venda:.2f}")

#A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:            
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
def q16():
     cabecalho('QUESTÃO 16')       
    idade = int(input("Digite a idade do nadador; "))
    if idade >= 5 and idade <= 7:
        print("Categoria: Infantil A")
    elif idade >= 8 and idade <= 10:
        print("Categoria: Infantil B")
    elif idade >= 11 and idade <= 13:
        print("Categoria: Juvenil A")
    elif idade >= 14 and idade <= 17:
        print("Categoria: Juvenil B")
    elif idade >= 18:
        print("Categoria: Sênior")
    else:
        print("Idade não se encaixa em nem uma das categorias dísponivel")



#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00
def q17():
    cabecalho('QUESTÃO 17')
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digitar a iadde: "))

    valor = 0
    if idade <= 10:
        valor = 30.00
    elif idade <= 29:
        valor = 60.00
    elif idade <= 45:
        valor = 120.0
    elif idade <= 59:
        valor = 150.00
    elif idade <= 65:
        valor = 250.00
    else:
        valor = 400.00
    print(f"\nNome: {nome}")
    print(f"Valor a pagar: R$ {valor:.2f}")


#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
def q18():
     cabecalho('QUESTÃO 18')
    mes = int(input("Digite um número inteiro entre 1 e 12: "))
    
    if mes == 1:
        print("Janeiro")
    elif mes == 2:
        print("Fevereiro")
    elif mes == 3:
        print("Março")
    elif mes == 4:
        print("Abril")
    elif mes == 5:
        print("Maio")
    elif mes == 6:
        print("Junho")
    elif mes == 7:
        print("Julho")
    elif mes == 8:
        print("Agosto")
    elif mes == 9:
        print("Setembro")
    elif mes == 10:
        print("Outubro")
    elif mes == 11:
        print("Novembro")
    elif mes == 12:
        print("Dezembro")
    else:
        print("Não existe mês com este número.")

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".
def q19():
     cabecalho('QUESTÃO 19')
    ponto1 = int(input("Digite os pontos do jogador 1: "))
    ponto2 = int(input("Digite os pontos do jogador 2: "))
    ponto3 = int(input("Digite os pontos do jogador 3: "))
    
    pontos = [ponto1, ponto2, ponto3]
    pontos.sort(reverse=True)
    
    print("Pontos em ordem decrescente:", pontos)
    
    soma_pontos = sum(pontos)
    
    if soma_pontos > 100:
        media = soma_pontos / 3
        print(f"Média aritmética: {media:.2f}")
    else:
        print("Equipe desclassificada")
#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio
def q20():
     cabecalho('QUESTÃO 20')
    saldo_medio = float(input("Digite o saldo médio do cliente: R$ "))
    
    credito = 0
    if saldo_medio > 3000:
        credito = saldo_medio * 0.50
    elif saldo_medio > 1000:
        credito = saldo_medio * 0.40
    elif saldo_medio > 500:
        credito = saldo_medio * 0.30
    
    print(f"\nSaldo Médio: R$ {saldo_medio:.2f}")
    print(f"Valor do Crédito: R$ {credito:.2f}")

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
def q21():
     cabecalho('QUESTÃO 21')
    nome_livro = input("Nome do livro: ")
    tipo_usuario = input("Tipo de usuário (professor ou aluno): ")
    
    dias_emprestimo = 0
    if tipo_usuario.lower() == 'professor':
        dias_emprestimo = 10
    elif tipo_usuario.lower() == 'aluno':
        dias_emprestimo = 3
    else:
        print("Tipo de usuário inválido.")
        return 
    
    print("\n--- Recibo de Empréstimo ---")
    print(f"Nome do livro: {nome_livro}")
    print(f"Tipo de usuário: {tipo_usuario}")
    print(f"Total de dias: {dias_emprestimo}")


#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.
def q22():
     cabecalho('QUESTÃO 22')
    percurso_km = float(input("Digite o percurso em quilômetros: "))
    tipo_carro = input("Digite o tipo do carro (A, B ou C): ").upper()
    
    consumo_litros = 0
    if tipo_carro == 'A':
        consumo_litros = percurso_km / 12
    elif tipo_carro == 'B':
        consumo_litros = percurso_km / 9
    elif tipo_carro == 'C':
        consumo_litros = percurso_km / 8
    else:
        print("Tipo de carro inválido.")
        return
    
    print(f"\nO consumo estimado de combustível é de {consumo_litros:.2f} litros.")



#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

def q23():
     cabecalho('QUESTÃO 23')
    prato_calorias = {'Vegetariano': 180, 'Peixe': 230, 'Frango': 250, 'Carne': 350}
    sobremesa_calorias = {'Abacaxi': 75, 'Sorvete diet': 110, 'Mousse diet': 170, 'Mousse chocolate': 200}
    bebida_calorias = {'Chá': 20, 'Suco de laranja': 70, 'Suco de melão': 100, 'Refrigerante diet': 65}

    print("Pratos: Vegetariano, Peixe, Frango, Carne")
    prato_escolhido = input("Escolha um prato: ")

    print("Sobremesas: Abacaxi, Sorvete diet, Mousse diet, Mousse chocolate")
    sobremesa_escolhida = input("Escolha uma sobremesa: ")

    print("Bebidas: Chá, Suco de laranja, Suco de melão, Refrigerante diet")
    bebida_escolhida = input("Escolha uma bebida: ")
    
    total_calorias = 0
    
    
    if prato_escolhido in prato_calorias:
        total_calorias += prato_calorias[prato_escolhido]
    else:
        print(f"Prato '{prato_escolhido}' inválido.")
        return

    
    if sobremesa_escolhida in sobremesa_calorias:
        total_calorias += sobremesa_calorias[sobremesa_escolhida]
    else:
        print(f"Sobremesa '{sobremesa_escolhida}' inválida.")
        return


    if bebida_escolhida in bebida_calorias:
        total_calorias += bebida_calorias[bebida_escolhida]
    else:
        print(f"Bebida '{bebida_escolhida}' inválida.")
        return
    
    print(f"\nO total de calorias da sua refeição é de {total_calorias} calorias.")

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

def q24():
     cabecalho('QUESTÃO 24')
    placa = input("Digite a placa do carro (ex: ABC1234): ")
    if len(placa) < 1:
        print("Placa inválida.")
        return

    ultimo_digito = int(placa[-1]) 
    
    meses_emplacamento = {
        0: 'Dezembro',
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro'
    }

    if ultimo_digito in meses_emplacamento:
        mes = meses_emplacamento[ultimo_digito]
        print(f"O emplacamento deve ser renovado em {mes}.")
    else:
        print("Placa inválida (último dígito não é um número).")

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos
def q25():
     cabecalho('QUESTÃO 25')
    indice = float(input("Digite o índice de poluição: "))

    if indice >= 0.5:
        print("Intimação: 1º, 2º e 3º grupos")
    elif indice >= 0.4:
        print("Intimação: 1º e 2º grupos")
    elif indice >= 0.3:
        print("Intimação: 1º grupo")
    else:
        print("Índice de poluição aceitável. Nenhuma intimação necessária.")

menu = '''
[1] - Ler dois números inteiros
[2] - Ler dois números inteiros e fazer a adição
[3] - É multiplo de 3 ou não é multiplo de 3
[4] - É divisivel por 5 ou não
[5] - É divisivel por e 3 e por 7
[6] - Emprestimo consedido ou não
[7] - O número esta compreendido entre 20 e 50
[8] - Maior que 20, igual a 20, menor que 20
[9] - Imprimir idade 
[10] - Ler número inteiro é exibir em ordem crescente
[11] - Ler 3 número e imprimir maior deles
[12] - Ler idade 
[13] - Resultado da prova 
[14] - Calcular o desconto do INSS com base no sálario
[15] - Calcula o valor da venda do produto com base no persentual de lucro
[16] - Classifica nadador por catecoria de acordo com a idade
[17] - Calcula o valor do plano de saúde com base na idade
[18] - Identifica o nome do mês a parti de um número
[19] - Calcula a média dos pontos de uma equipe e verifica se foi classificada
[20] - Calcula o valor de um crédito especial com base no saldo médio
[21] - Gera um recibo de empréstimo de livro com base no tipo do usuário
[22] - Estima o consumo de um combustível com base no percurso e tipo de carro
[23] - Calcula o total de calorias de uma refeição com base nas escholhas do usuário
[24] - Imforma o mês de renovação do emplacamento a partir do último dígito da placa
[25] - Imprime intimações para indústrias com base no ídice de poluição

Digite a opção a ser executada: 
'''

opcao = input(menu)
eval(f'q{opcao}()')