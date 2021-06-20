velocidade = 90

if velocidade > 110:
  print('Acima da velociade Permitida')
  print('Favor Reduzir a Velocidade')
  
elif velocidade < 60:
    print('Favor dirigir acima de 80km/h')  

else:
  print('velocidade OK')  

print('FIM!')

#Exercicio de fixação

salario = 700

if salario < 500:
  print('Você não pagara todas as contas esse mês')

elif salario == 600: 
  print('Você recebeu apenas para pagar as contas do mês')

else:
   print('Esse mês está tudo ok')  

#Aula

renda_acima_5mil = True
nome_limpo = False

if renda_acima_5mil and nome_limpo:
  print('Financiamento Aprovado')

else:
  print('Financiamento não Negado')  


#Aula - Ternary Operator (Operador Ternário)

idade = 17

if idade >= 16:
  resultado = print('Voto Permitido')

else:
  resultado = print('Voto não permitido')    

print(resultado)

#Segundo exemplo com a mesma condição

age = 13

condição = 'Voto Permitido' if age >= 16 else 'Voto não Permitido'

print(condição)

#Exercicio de fixação

manuel = 13 #para nao colocar idade atribui um nome

dirigir = 'Pode dirigir' if manuel >= 18 else 'Você ainda nao pode dirigir'

print(dirigir)








