#O último teorema de Fermat diz que não existem números inteiros a, b e c 
# tais que a**n + b**n == c**n para quaisquer valores de n maiores que 2.

#Escreva uma função chamada check_fermat que receba
#  quatro parâmetros – a, b, c e n – e verifique se o teorema de Fermat
# se mantém. Se n for maior que 2 e a**n + b**n == c**n o programa deve 
# imprimir, “Holy smokes, Fermat was wrong!” Senão o programa deve exibir
#  “No, that doesn’t work.”

#Escreva uma função que peça ao usuário para digitar valores para
#  a, b, c e n, os converta em números inteiros e 
# use check_fermat para verificar se violam o teorema de Fermat.



def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("holy smokes, fermat was wrong")
    else:
        print("no, that doesn’t work")

def test_fermat():
    try:
        a = int(input("Digite um valor inteiro para a: "))
        b = int(input("Digite um valor inteiro para b: "))
        c = int(input("Digite um valor inteiro para c: "))
        n = int(input("Digite um valor inteiro para n (maior que 2): "))
        check_fermat(a, b, c, n)
    except ValueError:
        print("por favor, insira apenas números inteiros")
              
test_fermat()