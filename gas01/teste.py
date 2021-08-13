
import mysql.connector

def dia():
    lista = []
    valor = 0
    i = 0

    while True:
        while True:
            try:
                num = int(input("Qual é o preço do botijão de gás(em número inteiro e sem R$)? "))
                if num == 90 or num == 95 or num == 100 or num == 0:
                    lista.append(num)
                    i = i + 1
                    valor = num + valor
                    break
                else:
                    print("Valor inválido")
            except:
                print("Por favor escreva um número válido")


        if num==0:
            break
    print('='*100)
    print(f"Quantidade de botijões de gás vendidos no dia: {i}")
    print()
    print(f"Valor total dos botijões de gás vendidos no dia: R${valor}")
    print()
    for c, v in enumerate(lista):

        print(f'{c + 1}º Botijão de gás : {v}')
    print('='*100)
def mes():
    valor=0
    while True:
        try:
         num=int(input("Digite o valor do ganho de cada dia "))
         valor=num+valor
         if num == 0:
             break
        except:
            print("Digite um número válido")



    print(f"O valor total adquirido no mês foi de: R${valor} ")
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO info (numgas,preço) VALUES(%i,%i)"
    dados = (int(valor))
    cursor.execute()
    banco.commit()
d = input('Digite se deseja saber o ganho no dia ou no mês ').strip().upper()
if d in 'DIA':
        dia()
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="info")
if d in 'MÊS' or 'MES':
        mes()
        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="info")

