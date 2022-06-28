import pandas as pd 
import matplotlib.pyplot as mp


df = pd.read_excel("C:/Users/ariell/Desktop/Painel_Covid19/Painel_Covid-19/Covid19BrasilAlbania20202022.xlsx")
##df = pd.read_excel("Covid19BrasilAlbania20202022.xlsx")
##eu testei o código no jupyter e no vscode, no vscode eu precisei colocar o caminho completo do
##arquivo pois não encontrou mesmo estando no mesmo repositório"""

##comandos para tratar os dados que aprendi na aula ao vivo
df["Média Móvel"] = df.iloc[:,5].rolling(window=5).mean() 
df["data"] = df["data"].astype(str)
df.rename(columns={'Time' : 'Data Albânia'}, inplace= True)
df["Data Albânia"] = df["Data Albânia"].astype(str)
df["Média Móvel Albânia"] = df.iloc[:,10].rolling(window=5).mean()



multigraphic = mp.figure(figsize=(30, 10)) #armazenando em uma variável para poder usar recurso "subplot"
multigraphic.suptitle('Gráficos Covid-19 Brasil e Albânia', fontsize = '30')


multigraphic.add_subplot(211) ## subplot para poder plotar 2 gráficos juntos
mp.xticks(range(0,854,90), rotation = 22) #o parâmetro 90, é para plotar as datas a cada 90 dias
mp.ylabel("Óbitos por dia")
mp.xlabel("Data (Casos a cada 90 dias)")
mp.bar(df['data'], df.iloc[:,5], color = 'yellow', label= 'Óbitos por dia no Brasil')
mp.plot(df['data'], df['Média Móvel'], color = "green", label = 'Média Móvel Brasil')
mp.legend()

multigraphic.add_subplot(212)
mp.xticks(range(0,854,90), rotation = 22)
mp.ylabel("Óbitos por dia")
mp.xlabel("Data (Casos a cada 90 dias)")
mp.bar(df['Data Albânia'], df.iloc[:,10], color = 'red', label= 'Óbitos por dia na Albânia')
mp.plot(df['Data Albânia'], df['Média Móvel Albânia'], color = "black", label = 'Média Móvel Albânia')
mp.legend()

##multigraphic.show() no vscode esse comando está retornando um erro e o coma ndo
# abaixo foi a solução que encontrei (no jupyter roda normal)
multigraphic.savefig('demo.png', bbox_inches='tight') #o gráfico plotado é salvo como png no mesmo diretório
#no jupyter aparece na tela normalmente com o "multigraphic.show()"