
#%%
lista = [2, 132, "will", ["ds", "de", "da"],True,]
lista [2]


lista = [2, 132, "will", ["ds", "de", "da"],True,]
lista [2]

#%%
#pares de chave/valor 

dados_will = {"sobrenome":"Rocha",
              "nome":"Will",
                "filhos":True,
                 "formacao":["analise de dados", "ciencia dos dados"],
       "cargos": [
        {
            "nome": "ds jr.",
            "empresa": "tapps"
        },
        {
            "nome": "ds pl.",
            "empresa": "sas"
        },
        {
            "nome": "ds sr.",
            "empresa": "boticario"
        },
        {
            "nome": "ds espec.",
            "empresa": "via varejo"
        }
    ]
}
     

                
print(dados_will)
#%%
print(dados_will["formacao"[-1]])
#%%
dados_will["cargos"][-1]["empresa"]

# %%
dados_will["estado civil"] = "casado"

#%%

print("chaves", dados_will.keys())
print("valores", dados_will.values())
print("items", dados_will.items())
#%%

for i in dados_will:
    print(i,"->", dados_will)