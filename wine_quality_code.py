"""Avaliando dados
Usando o Pandas, explore winequality-red.csv e winequality-white.csv no notebook Jupyter abaixo 
para responder às perguntas do quiz abaixo do notebook sobre as seguintes características do conjunto de dados:

número de amostras em cada conjunto de dados
número de colunas em cada conjunto de dados
recursos com valores faltantes
linhas duplicadas no conjunto de dados sobre vinho branco
número de valores únicos para qualidade em cada conjunto de dados
densidade média do conjunto de dados sobre vinho tinto
"""

import pandas as pd

df_white = pd.read_csv("winequality-white.csv", delimiter=";")
print("white")
display(df_white.head(2))

df_red = pd.read_csv("winequality-red.csv", delimiter=";")
print("red")
display(df_red.head(2))

"""Appending de dados
Você pode combinar os conjuntos de dados sobre vinho tinto e branco para que sua análise seja mais eficiente. 
Use o NumPy para criar uma nova coluna que preserva as informações de cores e, então, use o Pandas para combinar os dataframes.
"""

# importe o numpy e o pandas
import pandas as pd
import numpy as np

# carregue os conjuntos de dados de vinhos tintos e brancos
red_df = pd.read_csv("winequality-red.csv", delimiter=";")
white_df = pd.read_csv("winequality-white.csv", delimiter=";")

""" Crie colunas de cor
Crie dois vetores de tamanho igual ao número de linhas nos dataframes tinto e branco que repetem o valor “red” or “white”. 
O NumPy oferece uma forma bem fácil de fazer isso. 
Aqui está a documentação para a função [repeat do NumPy](https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html). 
Dê uma olhada e tente você mesmo.
"""
#importe o numpy e o pandas
import pandas as pd
import numpy as np

# carregue os conjuntos de dados de vinhos tintos e brancos
red_df = pd.read_csv("winequality-red.csv", delimiter=";")
white_df = pd.read_csv("winequality-white.csv", delimiter=";")

# crie vetor de cor para o dataframe tinto
color_red = np.repeat("red", red_df.shape[0])
print(color_red)
# crie vetor de cor para o dataframe branco
color_white = np.repeat("white", white_df.shape[0])
print(color_white)

#confira
red_df['color'] = color_red
red_df.head()


#Faça o mesmo para o dataframe branco e use head() para confirmar a mudança.
white_df['color'] = color_white
white_df.head()

"""
Combine dataframes com append
Veja a documentação para a função append do Pandas e veja se você pode usar isso para descobrir como combinar os dataframes. 
(Bonus: Por que não estamos usando o método merge para combinar dataframes?) Se você não entender, vou te mostrar como mais tarde. 
Certifique-se de salvar seu trabalho neste notebook! Você irá voltar para isso mais tarde.
"""

# anexe dataframes
wine_df = white_df.append(red_df)

# exiba o dataframe para ver se tudo deu certo
wine_df.head()

print(" Branco Original:{0} \n Tinto Original:{1}\n Combinado:{2}".format(white_df.shape, red_df.shape, wine_df.shape))


"""
Salve o dataset combinado
Salve seu dataframe recém-combinado como winequality_edited.csv.
 Lembre-se de configurar index=False para evitar salvar com uma coluna não-nomeada!
"""

wine_df.to_csv("winequality_edited.csv", index=False)


"""Anexando dados
Primeiro, importe os pacotes necessários e carregue os arquivos winequality-red.csv e winequality-white.csv.
"""
# importe o numpy e o pandas
import pandas as pd
import numpy as np

# carregue os conjuntos de dados de vinhos tintos e brancos
red_df = pd.read_csv("winequality-red.csv", delimiter=";")
white_df = pd.read_csv("winequality-white.csv", delimiter=";")

"""Crie colunas de cor
Crie dois vetores de tamanho igual ao número de linhas nos dataframes tinto e branco que repetem o valor “red” or “white”.
 O NumPy oferece uma forma bem fácil de fazer isso. Aqui está a documentação para a função repeat do NumPy. 
 Dê uma olhada e tente você mesmo.
"""

# crie vetor de cor para o dataframe tinto
color_red = np.repeat("red", red_df.shape[0])
print(color_red)
# crie vetor de cor para o dataframe branco
color_white = np.repeat("white", white_df.shape[0])
print(color_white)

#Adicione os vetores de cor aos dataframes tinto e branco. 
#Faça isso associando uma nova coluna chamada 'color' ao vetor apropriado. A célula abaixo faz isso para o dataframe tinto.

red_df['color'] = color_red
red_df.head()

#Faça o mesmo para o dataframe branco e use head() para confirmar a mudança.
white_df['color'] = color_white
white_df.head()

"""Combine dataframes com append
Veja a documentação para a função append do Pandas e veja se você pode usar isso para descobrir como combinar os dataframes. 
(Bonus: Por que não estamos usando o método merge para combinar dataframes?) Se você não entender, vou te mostrar como mais tarde.
 Certifique-se de salvar seu trabalho neste notebook! Você irá voltar para isso mais tarde.
"""
# anexe dataframes
wine_df = white_df.append(red_df)

# exiba o dataframe para ver se tudo deu certo
wine_df.head()

print(" Branco Original:{0} \n Tinto Original:{1}\n Combinado:{2}".format(white_df.shape, red_df.shape, wine_df.shape))


"""
Salve o dataset combinado
Salve seu dataframe recém-combinado como winequality_edited.csv. Lembre-se de configurar index=False para evitar 
salvar com uma coluna não-nomeada!
"""
wine_df.to_csv("winequality_edited.csv", index=False)


"""Explorando com informações visuais
Use o notebook abaixo para realizar análises de dados exploratórios em seu dataframe recém-combinado. 
Crie alguns gráficos para responder às perguntas do quiz abaixo do notebook.

Baseado em histogramas de colunas neste conjunto de dados, qual das seguintes variáveis de características aparece distorcida 
para a direita? Acidez fixa, total de dióxido de enxofre, pH, álcool
Baseado em gráficos de dispersão de qualidade em relação a variáveis de características diferentes, qual dos seguintes tem mais 
probabilidade de impactar a qualidade? Acidez volátil, açúcar residual, pH, álcool
"""

#EDA com visualizações
#Crie visualizações para resopnder as perguntas do teste abaixo deste notebook.

# Carregue o conjunto de dados
import pandas as pd
df_wine = pd.read_csv("winequality_edited.csv")
df_wine.head()

df_wine["fixed_acidity"].plot(kind="hist", title="Acidez");

#Histogramas para diversas características

#Acidez
df_wine["fixed_acidity"].plot(kind="hist", title="Acidez");

#Dióxido de Enxofre
df_wine["total_sulfur_dioxide"].plot(kind="hist", title="Dióxido de Enxofre");

#PH
df_wine["pH"].plot(kind="hist", title="pH ");

#Alcool
df_wine["alcohol"].plot(kind="hist", title="Álcool");

#Diagrama de dispersão da qualidade associada a diversas características

#Plot1
df_wine.plot(kind='scatter', x='volatile_acidity', y='quality');

#PLot2
df_wine.plot(kind='scatter', x='residual_sugar', y='quality');

#Plot3
df_wine.plot(kind='scatter', x='pH', y='quality');

#Plot4
df_wine.plot(kind='scatter', x='alcohol', y='quality');



"""Desenhando conclusões usando Groupby
No notebook abaixo, você investigará duas questões sobre esses dados usando a função groupby do Pandas. 
Seguem algumas dicas para responder a cada pergunta:

P1: Existe um certo tipo de vinho (tinto ou branco) associado a uma melhor qualidade?
Para esta pergunta, compare a qualidade média do vinho tinto à qualidade média do vinho branco, com o groupby. 
Faça esse grupo por cor e, depois, encontre a qualidade média de cada grupo.

P2: Qual nível de acidez (valor de pH) recebe a classificação média mais alta?
Essa pergunta é mais complicada porque, ao contrário da cor, que possui categorias claras pelas quais você pode agrupar 
(tinto ou branco), pH é uma variável quantitativa, sem categorias claras. 
No entanto, existe uma solução simples para isso. Você pode criar uma variável categórica de uma variável quantitativa 
criando suas próprias categorias. A função Cut do Pandas permite que você “corte” os dados em grupos. 
Usando essa função, crie uma nova coluna chamada nível_acidez com essas categorias.

Níveis de acidez:
Alto: Abaixo de 25% dos valores de pH
Moderadamente alto: 25% a 50% dos valores de pH
Médio: 50% a 75% dos valores de pH
Baixo: 75% ou mais dos valores de pH
Aqui, os dados estão sendo divididos nos percentuais 25, 50 e 75. Lembre-se, você pode obter esses números com a função describe() 
do Pandas! Depois de criar essas quatro categorias, você será capaz de usar groupby para conseguir a classificação de qualidade média 
para cada nível de acidez.
"""

#Tirando conclusões usando groupby

# Carregue o arquivo `winequality_edited.csv`
import pandas as pd
df_wine = pd.read_csv("winequality_edited.csv")

#Será que o tipo de vinho está associado a uma qualidade superior?
# Encontre a qualidade média de cada tipo de vinho (tinto e branco) com groupby
df_wine.groupby(['color']).mean()['quality']

#Qual o nível de acidez que recebe a maior avaliação média?

# Observe os seguintes valores de pH com Pandas describe: min, 25%, 50%, 75% e max
ph_desc = df_wine["pH"].describe()

# Bordas dos intervalos que serão usados para dividir os dados em grupos
bin_edges = [ph_desc['min'] ,ph_desc["25%"] , ph_desc["50%"] ,ph_desc["75%"], ph_desc["max"]] 

# Preencha esta lista com os cinco valores que você acabou de encontrar
# Rótulos para os quadro grupos de nível de acidez
bin_names = ["Alto" ,"Moderadamente Alto" ,"Médio" ,"Baixo" ] # Nomeie cada categoria de nível de acidez

# Cria a coluna acidity_levels
df_wine['acidity_levels'] = pd.cut(df_wine['pH'], bin_edges, labels=bin_names)

# Verifica se esta coluna foi criada corretamente
df_wine.head()

# Encontre a qualidade média de cada nível de acidez com groupby
df_wine.groupby(["acidity_levels"]).mean()["quality"]

# Salve alterações para a próxima seção
df.to_csv('winequality_edited.csv', index=False)


"""Outra função útil que você usará é a função query do Pandas.

Na aula anterior, selecionamos linhas em um dataframe indexando com uma máscara. 
Aqui estão os mesmos exemplos, juntamente a instruções equivalente que utilizam query().
"""

# selecionando registros malignos em dados de câncer
df_m = df[df['diagnosis'] == 'M']
df_m = df.query('diagnosis == "M"')

# selecionando registros de pessoas que ganham mais de $50K
df_a = df[df['income'] == ' >50K']
df_a = df.query('income == " >50K"')

"""
Desenhando conclusões usando Query
No notebook abaixo, você investigará duas perguntas sobre esses dados usando a função query do Pandas. 
Seguem algumas dicas para responder a cada pergunta:

P1: Vinhos com maior teor alcoólico recebem classificações maiores?
Para responder a essa pergunta, use o query para criar dois grupos de amostras de vinho:

Baixo álcool (amostras com um teor alcoólico abaixo da média)
Alto álcool (amostras com um teor alcoólico maior ou igual à média)
Em seguida, encontre a classificação média de qualidade de cada grupo.

P2: Vinhos mais doces (mais açúcar residual) recebem classificações maiores?
Da mesma forma, use a mediana para dividir as amostras em dois grupos, por açúcar residual, e encontre 
a classificação média de qualidade de cada grupo.
"""

#Tirando conclusões usando o Query
# Carregue o arquivo `winequality_edited.csv`
import pandas as pd
df_wine = pd.read_csv("winequality_edited.csv")

#Será que vinhos com maior teor alcóolico recebem avaliações melhores?
# obtenha o valor mediano do teor alcóolico
alcohol_median = df_wine["alcohol"].median()


# selecione amostras com teor alcóolico abaixo da mediana
low_alcohol = df_wine.query('alcohol < @alcohol_median')

# selecione amostras com teor alcóolico maior ou igual à mediana
high_alcohol = df_wine.query('alcohol >= @alcohol_median')

# certifique-se que estas consultas incluíram cada amostra uma única vez
num_samples = df_wine.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count() # resultado deve ser True


# obtenha a avaliação média de qualidade para grupos com alto e baixo teor alcóolico
print(" Avaliação média para alto teor:{0} \n Avaliação média para baixo teor:{1}".format(
        high_alcohol["quality"].mean(), low_alcohol["quality"].mean() ))


#Vinhos mais suaves recebem avaliações melhores?

# obtenha o valor mediano do nível de açúcar residual
sugar_median = df_wine["residual_sugar"].median()

# selecione amostras com nível de açúcar residual abaixo da mediana
low_sugar = df_wine.query('residual_sugar < @sugar_median')

# selecione amostras com nível de açúcar residual maior ou igual à mediana
high_sugar = df_wine.query('residual_sugar >= @sugar_median')

# certifique-se que estas consultas incluíram cada amostra uma única vez
num_samples == low_sugar['quality'].count() + high_sugar['quality'].count() # resultado deve ser True


# obtenha a avaliação média de qualidade para grupos com alto e baixo nível de açúcar residual
print(" Avaliação média para alto nível:{0} \n Avaliação média para baixo nível:{1}".format(
        high_sugar["quality"].mean(), low_sugar["quality"].mean() ))


"""Exemplo de Matplotlib
Abaixo está a visualização de tipos e qualidade criada com o Matplotlib. Como você pode observar, o Matplotlib possibilita
 muito mais controle sobre nossas visualizações.
"""

#Antes de continuarmos para a criação dessa visualização, vamos passar por um exemplo simples usando Matplotlib 
#para criar um gráfico de barras. Nós podemos usar a função bar do pyplot para isso.

#Criando um gráfico de barras usando matplotlib

import matplotlib.pyplot as plt
% matplotlib inline

#Dois argumentos são necessários para se usar a função bar do pyplot: a coordenada no eixo x das barras e sua altura.
plt.bar([1, 2, 3], [224, 620, 425]);

#Você pode especificar os rótulos das marcações do eixo x usando a função xticks do pyplot, 
#ou ainda especificando um parâmetro adicional na função bar. As duas células abaixo 
#The two cells below accomplish the same thing.


# trace as barras
plt.bar([1, 2, 3], [224, 620, 425])

# especifique as coordenadas no eixo x das marcações e seus rótulos
plt.xticks([1, 2, 3], ['a', 'b', 'c']);

# trace as barras com rótulos nas marcações do eixo x
plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c']);



#Defina o título e o rótulo dos eixos assim.

plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c'])
plt.title('Some Title')
plt.xlabel('Some X Label')
plt.ylabel('Some Y Label');




"""
Traçando gráficos com matplotlib
Use matplotlib para criar gráficos de barras que permitam visualizar as conclusões que você tirou com groupby e query.
"""

# Importe os pacotes necessários e carregue o arquivo `winequality_edited.csv`
import pandas as pd
from matplotlib import pyplot as plt
df_wine = pd.read_csv("winequality_edited.csv")

"""1: Será que vinhos com maior teor alcóolico recebem avaliações melhores?
Crie um gráfico de barras com uma barra para amostras de vinho com baixo teor alcóolico e outra para 
amostras com alto teor alcóolico. Esse primeiro está preenchido para você.
"""


# Use query para selecionar cada grupo e obter sua qualidade média
median = df_wine['alcohol'].median()
low = df_wine.query('alcohol < {}'.format(median))
high = df_wine.query('alcohol >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()


# Crie um gráfico de barras com rótulos adequados
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating');


"""
#2: Vinhos mais suaves recebem avaliações melhores?
Crie um gráfico de barras com uma barra para amostras de vinho com baixo nível de açúcar residual 
e outra para amostras com alto nível de açúcar residual.
"""

# Use query para selecionar cada grupo e obter sua qualidade média
median_sugar = df_wine['residual_sugar'].median()
low_sugar = df_wine.query('residual_sugar < {}'.format(median_sugar))
high_sugar = df_wine.query('residual_sugar >= {}'.format(median_sugar))

mean_quality_low_sugar = low['quality'].mean()
mean_quality_high_sugar = high['quality'].mean()


# Crie um gráfico de barras com rótulos adequados
locations = [1, 2]
heights = [mean_quality_low_sugar, mean_quality_high_sugar]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Residual Sugar')
plt.xlabel('Sugar Level')
plt.ylabel('Average Quality Rating');



#3: Qual o nível de acidez que recebe a maior avaliação média?
#Crie um gráfico de barras com uma barra para cada um dos quatro níveis de acidez.

# Use groupby para obter a qualidade média para cada nível de acidez
# Crie um gráfico de barras com rótulos adequados
df_wine.groupby(["acidity_levels"]).mean()["quality"].plot(kind="bar", ylim=(5.5,6), title="Qualidade Média por Níveis de Acidez")



df_wine.groupby(["acidity_levels"]).mean()["quality"].plot(kind="line", ylim=(5.5,6), title="Qualidade Média por Níveis de Acidez")




"""
Visualização de tipos e qualidade com Matplotlib
Abaixo está o código usado para criar a visualização com o Matplotlib.
"""


#Traçando gráficos com tipo de vinho e qualidade com matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline
import seaborn as sns
sns.set_style('darkgrid')

wine_df = pd.read_csv('winequality_edited.csv')




"""
Crie vetores para as alturas das barras correspondentes aos vinhos tinto e branco
Lembre-se, existe uma barra para cada combinação de tipo de vinho e avaliação de qualidade. 
A altura de cada barra é baseada na proporção de amostrar daquele tipo com aquela avaliação de qualidade.

Proporções das barras de vinho tinto = contagens para cada avaliação de qualidade / número total de amostras de vinho tinto
Proporções das barras de vinho branco = contagens para cada avaliação de qualidade / número total de amostras de vinho branco
"""

# obtenha as contagens para cada avaliação e tipo de vinho
color_counts = wine_df.groupby(['color', 'quality']).count()['pH']
color_counts


# obtenha a contagem total para cada tipo de vinho
color_totals = wine_df.groupby('color').count()['pH']
color_totals


# obtenha proporções dividindo as contagens das avaliações dos vinhos tintos pelo número total de amostras de vinho tinto
red_proportions = color_counts['red'] / color_totals['red']
red_proportions


# obtenha proporções dividindo as contagens das avaliações dos vinhos brancos pelo número total de amostras de vinho branco
white_proportions = color_counts['white'] / color_totals['white']
white_proportions


#Trace as proporções em um gráfico de barras
#Defina a localização no eixo x para cada grupo de avaliação e a largura de cada barra


ind = np.arange(len(red_proportions))  # a localização no eixo x dos grupos
width = 0.35       # a largura das barras

#Agora vamos criar o gráfico.

# trace as barras
red_bars = plt.bar(ind, red_proportions, width, color='r', alpha=.7, label='Red Wine')
white_bars = plt.bar(ind + width, white_proportions, width, color='w', alpha=.7, label='White Wine')

# título e rótulos
plt.ylabel('Proportion')
plt.xlabel('Quality')
plt.title('Proportion by Wine Color and Quality')
locations = ind + width / 2  # localização dos marcadores no eixo x
labels = ['3', '4', '5', '6', '7', '8', '9']  # rótulos dos marcadores no eixo x
plt.xticks(locations, labels)

# legenda
plt.legend()



"""Opa, isso não funcionou porque está faltando um valor de vinho tinto para a avaliação 9. 
Embora esteja número seja 0, precisamos dele para nosso gráfico. 
Execute as últimas duas células depois de executar a célula abaixo.
"""

red_proportions['9'] = 0
red_proportions























