#%%
idades = [17,32,56,87]
print(idades)

#%%
idades.append(32)
print(idades)



#%%
idades = []

while True:
    idade = input("Entre com a idade: ")
    
    if idade == "":
        break
    
    idades.append(int(idade))
    
    print(idades)
    
    media = sum(idades) / len(idade)
    minimo = min(idades)
    maximo = max(idades)
    qtde = len(idades)

