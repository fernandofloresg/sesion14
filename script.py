import pandas as pd
import matplotlib.pyplot as plt

athletes = pd.read_csv("./categorias_de_corredores.csv", sep=";", index_col=0)

athletes.info()

athletes.head()

plt.figure(1)

plt.hist(athletes['Tiempo'], 15, color='yellow', ec='black')
plt.title("Histograma Tiempo")
plt.savefig("Histograma.jpg")

import seaborn as sns
plt.figure(2)
sns.countplot(x=athletes['Velocidad'], palette='ocean')
plt.savefig("Velocidades.jpg")

#Si queremos saber las velocidades en hombres y mujeres
plt.figure(3)
plt.title('Grafico de Barras Genero')

# Changed something in here
grafico3 = sns.countplot(x='Genero', hue='Velocidad', palette='hot_r', data= athletes)
grafico3.set(title='Velocidades por genero', xlabel='Genero', ylabel='Total')
plt.title('Grafico de Barras Genero')
plt.savefig('Genero.jpg')
plt.show()
