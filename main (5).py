# Functions (Funções)
# DRY - Don't repeat yourself
# Parametro --> Argumento
# Default = Aquele que você define o valor no parametro
# Non-Default = Aquele que você não define o valor do parametro

'''
No exemplo abaixo NOME é o Non-Default, pq o valor dele ainda
será atribuido posteriormente podendo ser trocado a atribuição.

Já em QUANTIDADE ele está Default (definido) ou seja seu Valor 
sera sempre o mesmo até que voce troque. 

Deve-se respeitar as ordens, o NON-DEFAULT deve ser atribuido antes

def boas_vindas( nome, quantidade = 6):
  print(f'Olá{nome}.')
  print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos')# Não sera necessario chamar a quantidade 

'''

# Realizam uma tarefa
# Calcula e retorna o valor

def cliente1(nome):
  print(f'Olá {nome}')

def cliente2(nome):
  return f'Olá {nome}' 
  # Em return ele armazena informação e sé escreve se for chamado  

x = cliente1 ('Maria')
y = cliente2 ('José')

print(x)
print(y)

# Fixando Exercicio

def restaurante(nome):
  print(f'Bem vindos ao {nome} o melhor restaurante da cidade ')

def espera(itens):
  return f'Neste momento temos {itens} clientes em espera'

z = restaurante ('Bon Appetit')  
h = espera (6)

print(z)
print(h)

# Criar uma função que soma vários números.



