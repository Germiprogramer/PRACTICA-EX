from classes.estadisticos import *
from classes.graficos import *
import matplotlib.pyplot as plt
import seaborn as sns

casas = pd.read_csv("laliga_player_stats_spanish.csv")

corr_habi_dorm_precio = Correlacion(casas, ["Equipo","Posicion","Dorsal","Nombre","Partidos jugados","Porcentaje de Partidos jugados","Partidos jugados enteros","Porcentaje de Partidos jugados enteros","Partidos jugados como titular","Porcentaje de Partidos jugados como titular","Partidos sustituido","Porcentaje de Partidos sustituido","Tarjetas amarillas","Tarjetas rojas","Segunda tarjeta amarilla","Goles marcados","Penaltis marcados","Goles en propia puerta","Goles encajados mientras el jugador estaba en el campo","Bloqueos","Intercepciones","Recuperaciones","Despejes","Entradas con éxito","Entradas fallidas","Jugadas como último hombre","Duelos con éxito","Duelos fallidos","Duelos aéreos con éxito","Duelos aéreos fallidos","Fueras de juegos cometidos","Faltas recibidas","Faltas cometidas","Penaltis recibidos","Penaltis cometidos","Faltas por manos","Faltas cometidas por cada tarjetas recibida","Asistencias de gol","Regates realizados con éxito","Goles marcados desde dentro del área","Goles marcados desde fuera del área","Goles marcados con el pie izquierdo","Goles marcados con el pie derecho","Goles marcados de penalti","Goles marcados de cabeza","Goles marcados de jugada a balón parado","Goles marcados en propia puerta","Centros realizados","Corneres lanzados","Entradas realizadas","Duelos realizados","Duelos cuerpo a cuerpo realizados","Duelos aéreos realizados","Pases","Pases cortos","Pases largos","Pases al hueco"], "corr_habi_dorm_precio")
corr_habi_dorm_precio.calculo()