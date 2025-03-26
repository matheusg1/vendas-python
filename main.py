import os
import pandas as pd
import plotly.express as px

diretorio = 'data/Vendas/'
lista_arquivos = os.listdir(diretorio)

tabela_total = pd.DataFrame()

for x in lista_arquivos:
    if "vendas" in x.lower():
        diretorioArquivo = f"{diretorio}{x}"
        tabela = pd.read_csv(diretorioArquivo)
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=False)

tabela_produtos = tabela_total.groupby("Produto").sum()

tabela_produtos = (tabela_produtos[["Quantidade Vendida"]]
                    .sort_values(by="Quantidade Vendida", ascending=True))

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]

tabela_faturamento = tabela_total.groupby("Produto").sum().sort_values(by="Faturamento", ascending=False)
#print(tabela_faturamento)

tabela_lojas = tabela_total.groupby("Loja").sum().sort_values(by="Faturamento", ascending=False)

tabela_lojas = tabela_lojas[["Faturamento"]]

#print(tabela_lojas)

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento")

grafico.show();