from collections import deque

def bfs(grafo, origen):
	visitados = set()
	padres = {}
	orden = {}
	q = deque()

	visitados.add(origen)
	padres[origen] = None
	orden[origen] = 0
	q.append(origen)

	while q:
		v = q.popleft()
		for w in grafo.obtenerAdyacentes(v):
			if w not in visitados:
				visitados.add(w)
				padres[w] = v
				orden[w] = orden[v] + 1
				q.append(w)

	return padres, orden

# para el comando camino mas corto
def camino_minimo_bfs(grafo, origen, destino):
	padres = {}
	cola = deque()

	padres[origen] = None
	cola.append(origen)

	while(len(cola) > 0):
		v = cola.popleft()
		for w in grafo.obtenerAdyacentes(v):
			if w not in padres:
				padres[w] = v
				cola.append(w)
				if w == destino:
					return armar_camino_padres(padres, origen, destino)
	return None

def armar_camino_padres(padres, origen, destino):
	camino = []
	v = destino

	while v != origen:
		camino.append(v)
		v = padres[v]
	camino.append(v)
	return camino[::-1]


# para el comando conectividad
def componentes_fuertemente_conexas(grafo, v, componentes = {}):
	orden = {}
	mas_bajo = {}
	visitados = set()
	pila = []

	orden[v] = 0
	cfc_dfs(grafo, v, componentes, orden, mas_bajo, visitados, pila)

def cfc_dfs(grafo, v, componentes, orden, mas_bajo, visitados, pila):
	mas_bajo[v] = orden[v]
	visitados.add(v)
	pila.append(v)

	for w in grafo.obtenerAdyacentes(v):
		if w not in visitados:
			visitados.add(w)
			orden[w] = orden[v] + 1
			cfc_dfs(grafo, w, componentes, orden, mas_bajo, visitados, pila)
		if mas_bajo[v] > mas_bajo[w]:
			mas_bajo[v] = mas_bajo[w]

	if mas_bajo[v] == orden[v]:
		while(True):
			elemento = pila.pop()
			componentes[elemento] = v
			if elemento == v:
				break

