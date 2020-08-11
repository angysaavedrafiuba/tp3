from grafo import Grafo
from funciones_grafos import bfs
from collections import deque
import sys

class NetStats():
    
    def __init__(self):
    	self.grafo = Grafo()
        #self.comandos = ["camino"]

    def cargarRed(self, ruta_archivo):
    	""" Recibe la ruta del archivo donde se encuentra la info de la red y crea el grafo que lo modela."""
    	with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
	    	for linea in archivo:
	    		titulos = linea.rstrip("\n").split("	")
	    		self.agregarArticulo(titulos[0])
	    		i = 1
	    		while (i < len(titulos)):
	    			self.agregarArticulo(titulos[i])
	    			self.agregarLink(titulos[i-1], titulos[i])
	    			i+=1

    def agregarArticulo(self, titulo):
    	self.grafo.agregarVertice(titulo)

    def agregarLink(self, titulo1, titulo2):
    	self.grafo.agregarArista(titulo1, titulo2)

    def camino(self, origen, destino):
    	origenes, cantidad_links = bfs(self.grafo, origen)
    	q = deque()

    	v = destino
    	while v!= origen:
    		q.append(v)
    		v = origenes[v]
    	self.imprimirCamino(origen, q, cantidad_links[destino])

    def imprimirCamino(self, origen, q, costo):
    	print(origen, end=' ')

    	while q:
    		print ("-> " + q.pop(), end=' ')

    	print()
    	print ("Costo:", end=' ')
    	print (costo)

    def __str__(self):
        return str(self.grafo)

def netstats() :
	"""Genera un grafo apartir de la ruta del archivo.
	Imprime un mensaje si los parámetros están incompletos,
	y devuelve una excepción si falla en el proceso."""
	comandos = sys.argv
	if len(comandos) == 2 :
		net = NetStats()
		try :
			net.cargarRed(comandos[1])
		except IOError :
			print("Error intentando leer/escribir archivo. Verificar que el archivo .tsv exista")

		print(net)
		net.camino("Francesco Sabatini", "Real Jardín Botánico de Madrid")
	else :
		print("Error en la línea de comando")
	return


netstats()
