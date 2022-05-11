from classes.estadisticos import *
from classes.graficos import *
import matplotlib.pyplot as plt
import numpy as np

jugadores = pd.read_csv("laliga_player_stats_spanish.csv")

#FILTRAMOS EL DATASET 
jugadores = jugadores.drop(jugadores[jugadores['Posicion']=="Portero"].index)
jugadores = jugadores.drop(jugadores[jugadores['Posicion']=="Defensa"].index)
jugadores = jugadores.drop(jugadores[jugadores['Posicion']=="Centrocampista"].index)

delanteros_buenos = jugadores.drop(jugadores[jugadores['Minutos jugados']==0].index)


#MEDIA
media_HP = Media(delanteros_buenos, "Goles marcados")
media_HP.calculo()

#Numero de filas
filas = Filas(delanteros_buenos)
filas.calculo()

#Numero de columnas
columnas = Columnas(delanteros_buenos)
columnas.calculo()

#Valores maximos
max = Maximos(delanteros_buenos, "Goles marcados")
max.calculo()
#Valores minimos
min = Minimos(delanteros_buenos, "Goles marcados")
min.calculo()


#Mediana
mediana_HP = Mediana(delanteros_buenos, "Goles marcados")
mediana_HP.calculo()

#Moda
moda_HP = Moda(delanteros_buenos, "Goles marcados")
moda_HP.calculo()

#Desviación típica
desv_HP = Desviacion_tipica(delanteros_buenos, "Goles marcados")
desv_HP.calculo()

#q1
q1 = Q1(delanteros_buenos, "Goles marcados")
q1.calculo()


#q3
q3 = Q3(delanteros_buenos, "Goles marcados")
q3.calculo()

#rango intercuartilico
a = delanteros_buenos["Goles marcados"].quantile(0.25)
b = delanteros_buenos["Goles marcados"].quantile(0.75)
rango_int = b - a
print("El rango intercuartilico es {}".format(rango_int))

#grafico
grafico(delanteros_buenos["Goles marcados"], "hist", "Goles", "histogramagoles")


