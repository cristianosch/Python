
'''
for numero1 in range(1,6):
  print('Produto' + str(numero1))
  for numero2 in range(5):
    print(numero1, numero2)

  
# Imprimir a palavra F A N T A S T I C O

palavra = 'Fantastico'
for spaco in palavra:
    print(f'{spaco}', end= ' ')

''' 

# Defindo a função 'def' exercicio de repetição

'''
def boas_vindas():
  print('Ola Marcos!')
  print('Temos 5 laptops em estoque')

boas_vindas()

print('Ola Nome!')
print('Ola Nome!')
print('Ola Nome!')
print('Ola Nome!')

boas_vindas()

'''
# Functions (Funções)
# DRY - Don't repeat yourself
'''
def somar_dois_numeros():
  numero1 = 10
  numero2 = 5
  resultado = numero1 + numero2
  print(resultado)

def somar_dois_numeros1():
  numero1 = 30
  numero2 = 2
  resultado = numero1 + numero2
  print(resultado)


somar_dois_numeros()
somar_dois_numeros1()

'''
'''

Ao inves de criar um para cada compile
Marcos, Ronaldo e Linda. Atribuimos uma 
função para simplificar.
'''
def boas_vindas(nome, quantidade):
  print(f'Olá {nome}.')
  print(f'Temos {str(quantidade)} laptops em estoques')

boas_vindas('Marcos', 5)
boas_vindas('Ronaldo', 4)
boas_vindas('Linda', 2) 






 








  

   