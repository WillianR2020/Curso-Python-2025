#%%

will = [ "Will", "Rocha", 36, True,"casado",1400.00]

print(will)

# %%
type(will)

# %%

#idade
print(will[2])

#renda 
print(will[5])

print(will[0])

# %%

idades = [28, 42,43, 35,39, 29,38]
print("soma idades:", sum(idades))
print("qtd idades:", len(idades))
print("media idades:", sum(idades)/len(idades))
print("menor idade:",min(idades))
print("maior idades:", max(idades))

# %%

will = [ "Will Rocha",
         36,
         True,
         "casado",
         ["estagiario", "ds jr", "ds pl", "ds sr", "head"],
         [1400 , 2500, 5000, 7500, 1000],
         ["Ana", "Maria","Claudia"]]

print("Tamanho de will", len(will))

print(will[4][0])

exs= will[4]
primeira_ex = exs[0]
print(primeira_ex)

# %%
will[-1] [-2]

#%%

#primeiros 4 elementos 
will[0:4] 

will[4][0:4]

will [4] [-2:]

#will[ start : stop]

# %%

salarios = will[5]
salarios[::2]

