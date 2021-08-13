lista=[]
valor=0
i=0

while True:
 while True:
  try:
    num = int(input("Qual é o preço do botijão de gás(em número inteiro e sem R$)? "))
    if num == 90 or num == 95 or num == 100 or num==0:
     lista.append(num)
     i=i+1
     valor=num+valor
     break
    else:
        print("Valor inválido")
  except:
    print("Por favor escreva um número válido")


 b=input("Deseja continuar?\nDigite qualquer tecla para continuar\nDigite 0 ou Enter para parar ")
 if b in '0':
     break
print(f"Quantidade de botijões de gás vendidos no dia: {i}")
print(f"Valor total dos botijões de gás vendidos no dia: R${valor}")
for c,v in enumerate(lista):
    print(f'{c+1}º Botijão de gás : {v}')


