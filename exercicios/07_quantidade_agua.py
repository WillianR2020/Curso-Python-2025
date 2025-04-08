



texto = """
 Escolha a sua água para comprar 
 (1) Água mineral natural 
 (2) Água mineral com gás
"""

opção = input(texto)
valor_item = 0
if opção == "1":
   valor_item = 1,5
elif opção == "2":
    valor_item = 2,5
else: 
    print("entre com a porra da opção correta")

qtde = input ("Quantas garrafas?")
qtde = int(qtde)
valor_total = valor_item * qtde
print("Sua conta deu: R$", valor_total)