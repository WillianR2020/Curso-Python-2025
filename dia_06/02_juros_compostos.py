#%%
def juros_compostos(aporte:int, taxa:float, anos:int)->float:
 """juros_composto serve para calcular o retorno financeiro a partir de um aporte. 
 Deve-se considerar o valor, a taca de juros atual e o tempo( em anos ) para calculo do valor a ser retornado.
 aporte: um numero inteiro que represente o valor em reais 
 
 taxa: um numero float entre 0 e 1 que represente o valor da taxa de juros 

 anos: um numero inteiro >=1 que representa o tempo que o investimento terá liquidez.
 
  """
 return aporte * (1 + taxa) ** anos

#%%

juros_compostos(taxa=0.13, anos=5, aporte=1000)

