from grafo import Grafo
from funciones_grafos import *
from collections import deque
import sys
import cmd

class NetStats(cmd.Cmd):
	
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.grafo = Grafo()
		self.comandos = ["camino","diametro"]
		
	def agregarArticulo(self, titulo):
		self.grafo.agregarVertice(titulo)

	def agregarLink(self, titulo1, titulo2):
		self.grafo.agregarArista(titulo1, titulo2)

	def cargarRed(self, ruta_archivo):
		""" Recibe la ruta del archivo donde se encuentra la info de la red y crea el grafo que lo modela."""
		with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
			for linea in archivo:
				titulos = linea.rstrip("\n").split("\t")
				self.agregarArticulo(titulos[0])
				i = 1
				while (i < len(titulos)):
					self.agregarArticulo(titulos[i])
					self.agregarLink(titulos[i-1], titulos[i])
					i+=1

	def camino(self, origen, destino):
		origenes, cantidad_links = bfs(self.grafo, origen)
		if destino not in cantidad_links:
			return print("No se encontro recorrido")
		self.imprimirCamino(origenes, origen, destino, cantidad_links[destino])

	def imprimirCamino(self, padres, origen, destino, costo):
		q = deque()
		v = destino
		while v!= origen and v!=None:
			q.append(v)
			v = padres[v]

		print(origen, end=' ')

		while q:
			print ("-> " + q.pop(), end=' ')

		print ()
		print ("Costo:", end=' ')
		print (costo)
	
	def do_camino(self, args):
		arg = args.split(',')
		self.camino(arg[0], arg[1])

	def diametro(self):
		diam, origenes, cantidad_links = diametro(self.grafo)

		origen = None
		destino = None
		for v in origenes:
			if origenes[v] == None:
				origen = v
			if cantidad_links[v] == diam:
				destino = v 

		self.imprimirCamino(origenes, origen, destino, diam)

	def do_diametro(self, args):
		self.diametro()

	def __str__(self):
		return str(self.grafo)

	def do_listar_operaciones(self, args):
		for c in self.comandos:
			print (c)

	def do_EOF(self, line):
		return True

	prompt = ""


def main():
	"""Genera un grafo apartir de la ruta del archivo.
	Imprime un mensaje si los parámetros están incompletos,
	y devuelve una excepción si falla en el proceso."""
	linea_comandos = sys.argv
	if len(linea_comandos) == 2 :
		net = NetStats()
		try :
			net.cargarRed(linea_comandos[1])
		except IOError :
			print("Error intentando leer archivo. Verificar que el archivo .tsv exista")

		net.cmdloop()

	else :
		print("Error en la línea de comando")
	return

if __name__ == '__main__':
	main()
