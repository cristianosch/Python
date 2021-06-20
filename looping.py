# For Loops ( Looping) 

palavra = 'Google'

for letra in palavra:
  print(letra) 
   

compra_confirmada = True
dados_compra = 'Compra no valor de 12.50€ e entrega confirmada'

for enviar in range(3):
  if compra_confirmada:
    print (dados_compra)
    print ('Detalhes enviado para o seu email')
    break

  else:
    print('Falha na compra') 
    

