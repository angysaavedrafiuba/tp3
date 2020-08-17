#!/usr/bin/python3
from grafo import Grafo
from funciones_grafos import *
from collections import deque
import sys
import cmd
sys.setrecursionlimit(10**6)


class NetStats(cmd.Cmd):
	
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.grafo = Grafo()
		self.comandos = ["camino", "conectados", "ciclo", "lectura", "diametro", "rango",
						 "clustering", "mas_importantes", "navegacion"]
		self.cfc_conectividad = {}
		self.coef_clustering = {}
		self.ranking = []
		
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
					self.agregarLink(titulos[0], titulos[i])
					i+=1

	def do_camino(self, args):
		arg = args.split(',')
		self.camino(arg[0], arg[1])

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

	def do_diametro(self, args):
		self.diametro()

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

	def do_conectados(self, args):
		self.conectados(args)

	def conectados(self, pagina):
		if not pagina in self.cfc_conectividad:
			componentes_fuertemente_conexas(self.grafo, pagina, self.cfc_conectividad)
		print(", ".join(self.cfc_conectividad[pagina]))

	def do_ciclo(self, args):
		arg = args.split(',')
		self.ciclo(arg[0], int(arg[1]))

	def ciclo(self, pagina, n):
		camino = ciclo_de_largo_n(self.grafo, pagina, n)
		if camino:
			print(" -> ".join(camino))
		else:
			print("No se encontro recorrido")

	def do_clustering(self, args):
		self.clustering(args)

	def clustering(self, pagina):
		if pagina:
			if not pagina in self.coef_clustering:
				coef = coeficiente_de_clustering(self.grafo, pagina)
				self.coef_clustering[pagina] = coef
			print(self.coef_clustering[pagina])
		else:
			suma = 0
			for v in self.grafo.obtenerVertices():
				if v not in self.coef_clustering:
					coef = coeficiente_de_clustering(self.grafo, v)
					self.coef_clustering[v] = coef
				suma += self.coef_clustering[v]
			promedio = suma / len(self.grafo)
			print(round(promedio, 3))

	def do_lectura(self, args):
		arg = args.split(',')
		self.lectura(arg)

	def lectura(self, paginas):
		camino_inverso = orden_topologico_bfs(self.grafo, paginas)
		if camino_inverso == None:
			print("No existe forma de leer las paginas en orden")
		else:
			print(", ".join( camino_inverso[::-1]) )
	
	def do_rango(self, args):
		arg = args.split(',')
		self.rango(arg[0], arg[1])

	def rango(self, pagina, n):
		origenes, cantidad_links = bfs(self.grafo, pagina)
		rango = 0
		for v in cantidad_links:
			if cantidad_links[v] == int(n):
				rango += 1
		print(rango)

	def do_mas_importantes(self, args):
		n = int(args)
		self.mas_importantes(n)

	def mas_importantes(self, n):
		if len(self.ranking) == 0:
			self.ranking = pagerank(self.grafo)
		print(", ".join(self.ranking[:n]))

	def do_navegacion(self, args):
		camino = navegacion_por_primer_link(self.grafo, args)
		print(" -> ".join(camino))

	def do_listar_operaciones(self, args):
		for c in self.comandos:
			print (c)

	def do_EOF(self, line):
		return True

	def __str__(self):
		return str(self.grafo)

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
