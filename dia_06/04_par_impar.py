#Faça um programa que receba um número.
#  Verifique se o número informado é par ou ímpar.
#  Exiba o resultado da seguinte maneira:

#	O número x é impar
#ou
#	O número x é par
#%%

def par_impar(numero:int):
    if numero % 2 == 0:
        print("é par!")

    else:
        print("é impar")


    numero = input("entre com um numero: ")
    numero = int(numero)
    
    par_impar(numero)

#%%

def par_impar(numero:int):
    if numero % 2 == 0:
        return "par"

    else:
        return "impar"


    numero = input("entre com um numero: ")
    numero = int(numero)
    
    print("o valor",numero,"é",resultado)
