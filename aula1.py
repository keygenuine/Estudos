
#FORMAT
""" 
a = 'eu'
b = 'sou'
c = 'a mosca'
raulSeixas = '{} {} {}'
print (raulSeixas.format(a,b,c))
""" 

#IF ELSE
"""
if entrada == 'azul':
    print ('Voce entrou na matrix')
elif entrada == 'vermelha':
    print ('Voce saiu da matrix')
else:
    print('Você não encontrou o Morpheus')
"""

# OPERADORES
"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""

# OPERADOR AND
"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')   
print (True and True and False)

"""

# OPERADOR OR
"""
print (False or True or False)

senha = input ('Senha: ') or 'Sem senha'
print (senha)
#OPERADOR NOT
senha = input ('Senha: ')
if senha != '123456' 
        print ('Senha incorreta.')
if not senha: 
        print ('Voce nao digitou nada')  
"""

# OPERADOR IN E NOT IN
"""
nome = 'Douglas'
entrada = int(input('escolha um numero: '))
if entrada < 7:
 print (nome [entrada])
 print ('o' not in nome)
else:
 print ('Numero excede ')

nome = input ('Digite seu nome: ')
encontrar = input ('Digite oque deseja encontrar: ')
if encontrar in nome:
    print (f'{encontrar} está em {nome}')
else:
    print (f'{encontrar} não está em {nome}')
"""

# INTERPOLAÇÃO DE STRINGS % % % %
"""
nome = 'Douglas'
preco = 999.00
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print (variavel)
print ('O hexadecimal de %d é %04x' % (192,192))
"""

##FATIAMENTO DE STRINGS
"""
            #123456789# 
variavel = '#Olá mundo#'
print(len(variavel))
print(variavel [4:])
print(variavel [4:6])

numero_str = input(
    'Vou dobrar o número que vc digitar: '
)
print (numero_str.isdigit())
numero_float = float(numero_str)
print (f'O dobro de {numero_str} é {numero_float * 2:.2f}')
"""

##TRY EXCEPT
"""
numero_str = input(
    'Vou dobrar o numero que voce digitar: '
)
try:
    numero_float = float(numero_str)
    print ('FLOAT:', numero_float)
    print (f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print ('Isso não é um número')        
"""

##FLAGS, IS, IS NOT e NONE
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print ('Faça algo')
else:
    print('Nao faça aquilo')

if passou_no_if is None:
    print('Não passou no if')    
"""

#WHILE
"""
condicao = 0

while condicao < 3:
        nome = input('Qual o seu nome? ')
        print (f'Seu nome é {nome}')
        if nome == 'Sair' or 'sair':
            break
print('You broke the system')              
"""
#WHILE IF
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    print(contador)

    if contador == 40:
        break
"""

#WHILE + (laços internos)
"""
qtd_linhas = 5
qtd_colunas = 3

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
print ('ACABOU')
"""

##CALCULADORA COM WHILE
"""
#OPERAÇÕES
# try:
       Primeiro_numero = float (input('Digite um numero '))    
       Segundo_numero = float(input("Digite o segundo numero "))
except:
       print("EROU")
       excep = True
if excep is True:
       print('er')
       continue
print("Escolha um operador")
Operador = str(input('[A]dicão, [S]ubtraçao, [D]ivisão: ') )
if Operador == 'A':
       Resposta = Primeiro_numero + Segundo_numero
print(f'{Resposta}')              
"""       

##Laço de repetição FOR
"""
# texto = 'Python'

# novo_texto = ''
# for letra in texto:
#     novo_texto += f'*{letra}'
#     print(letra)
# print(novo_texto + '*')
"""

# range(start,stop,step)
"""
 numeros = range (10)

 for numero in numeros:
        print(numeros)
"""

#Como o for funciona por baixo dos panos? 
# (next, iter, iterável e iterador)
"""texto = 'Douglaas' #iteravel
iterador = iter(texto) #iterator

#Funcionamento do 'for' abaixo.

while True:
    try:
       print (next(iterador))
    except StopIteration:
       break
       
for letra in texto:
   print(letra)
""" 

#Listas
"""
append, insert, pop, del, clear, extend, +

#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
"""

#'For' em listas
"""
for in com listas

lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))



indice = 0 
lista = ['Maria', 'Helena', 'Luiz']
for nome in lista:
       indice += 1 
       print(f'{indice-1} {lista[indice -1]}')


"""
#Aula 87
#Listas 
"""
nome1, *_ = ['maria','joao','bruxa']
print (nome1, _,)
"""

#Aula 88 
#Tuplas
"""
nomes = 'MARIA', 'JOAO', 'BRUXA'
# nomes[1] = 'maria' #Não funciona pois tupla é imutavel
print (nomes[1])


nomes = ['maria','joao','bruxa']
nomes =tuple(nomes)#Converte nomes para tupla
print(nomes[-1])
nomes[1] = 'joaum'

"""
#Aula 89
#Enumerate - enumera iteráveis em indices
"""
lista = ['maria','joao','bruxa']
lista.append('jhow')
print(next(enumerate(lista)))#Exibe somente com next
#Caso contrario gera a posicão na memoria
lista_enumerada = enumerate(lista)
for item in lista_enumerada:
    print(item)#Aqui seria como se 'For' estivesse dando next
    
lista_enumerada = enumerate(lista, start=1)
print(lista_enumerada)
"""

# EXERCICIO LISTA DE SUPERMERCADO
"""
#insere um elemento
lista= []
lista.append("arroz")

controle = input("ESCOLHA A OPÇÃO:\n [i]inserir [d]deletar [l]listar : ")
while controle != 'sair':
#funcão inserir
    if controle == 'i':
        produto = input ('digite o nome do produto: ')     
        lista.append(produto)
        controle = input("digite [i] para continuar ou [d]deletar [l]listar ")
#função deletar
    elif controle == 'd':
        try:
            indice = int(input("digite o indice do produto a deletar ou [l]listar [i]inserir: "))
            deletador = indice     
            lista.pop(indice)
        except:
            controle = input("ESCOLHA A OPÇÃO:\n [i]inserir [d]deletar [l]listar : ")
    elif controle == 'l':
            lista_enumerada = enumerate(lista)           
            for indice in lista_enumerada:
                print(indice)
                print("agora escolha outra opção ou [sair]")
                controle = input("ESCOLHA A OPÇÃO:\n [i]inserir [d]deletar [l]listar : ")    
"""
# append, insert, pop, del, clear, extend, +
""" 
#CONJUNTO          
lista = []
lista.append(0)
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(6)
lista.append(7)
lista.append(8)
lista.append(9)
lista.append(10)
print(lista)

#insert
posicao_para_inserir= 4
valor_a_inserir = 333333
lista.insert(posicao_para_inserir, valor_a_inserir)
print(lista)

#pop
posicao_para_excluir = 4
lista.pop(posicao_para_excluir)
print(lista)

#del
posicao_para_deletar = 2
del lista[posicao_para_deletar]
print(lista)

#extend
lista.extend('2')
lista.extend('2')
print(lista)

#clear
lista.clear()
print(f'{lista} limpou')

"""
#QUANTOS % PORCENTO % PRECISO PRA RECUPERAR?
"""
validador = input("[P]erda ou [G]anho: ")
if validador == "P" or "p":
    setador = "S"   
    while setador == "S" or "s":
        #valor de compra___ input (R$)
        valor_compra =int(input("Digite o valor de compra: "))
        print(f'o valor de compra é: R${valor_compra}')

        #percentual perda___ input (%)
        percentual_perda =int(input("Digite o percentual de perda: "))
        print(f'o valor percentual de perda é: {percentual_perda}%')

        #valor de perda___ output (R$)
        valor_final =(valor_compra / 100) * percentual_perda
        print(f'O Valor de perda é: R${round(valor_final,2)}')

        #valor que restou na carteira__output (R$)    
        delta_compra_perda =  valor_compra - valor_final
        print(f'O Valor restante é: R${delta_compra_perda}')



"""
        
#QUANTO PRECISO INVESTIR PARA QUE COM O MESMO PERCENTUAL DE PERDA, SE GANHAR, CONSIGA RECUPERAR O DINHEIRO?




    
