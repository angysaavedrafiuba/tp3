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