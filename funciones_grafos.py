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

'''
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
'''

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
		nueva_cfc = []
		while (True):
			elemento = pila.pop()
			nueva_cfc.append(elemento)
			if elemento == v:
				break
		for i in nueva_cfc:
			componentes[i] = nueva_cfc

# para el comando ciclo de n articulos
# backtracking
def ciclo_de_largo_n(grafo, origen, n):
	camino = []
	visitados = set()
	if(ciclo_de_largo_n_rec(grafo, origen, origen, n, camino, visitados)):
		camino.append(origen)
		return camino
	return None

def ciclo_de_largo_n_rec(grafo, origen, v, n, camino, visitados):
	if len(camino) == n:
		if v == origen:
			return True
		return False

	if v in visitados or len(camino) > n:
		return False

	camino.append(v)
	visitados.add(v)
	for w in grafo.obtenerAdyacentes(v):
		todo_ok = ciclo_de_largo_n_rec(grafo, origen, w, n, camino, visitados)
		if todo_ok:
			return True
	camino.pop()
	return False


#Para el comando diametro
#Aplica bfs para cada vertice
def diametro(grafo):
	_padres = {}
	_orden = {}
	diametro = 0
	for v in grafo.obtenerVertices():
		padres, orden = bfs(grafo, v)
		if ( max(orden.values()) > diametro):
			_padres = padres
			_orden = orden
			diametro = max(orden.values())
	
	return diametro, _padres, _orden 

def coeficiente_de_clustering(grafo, v):
	ady_enlazados = 0
	grado_de_salida = 0
	adyacentes = grafo.obtenerAdyacentes(v)
	if len(adyacentes) < 2:
		return 0
	for w in adyacentes:
		if w == v:
			continue
		grado_de_salida += 1
		for z in grafo.obtenerAdyacentes(w):
			if z in adyacentes and z != w and z != v:
				ady_enlazados += 1
	if ady_enlazados == 0:
		return 0
	coef = ady_enlazados / (grado_de_salida * (grado_de_salida - 1))
	return round(coef, 3)


#para el comando lectura a las 2 am
def orden_topologico_bfs(grafo, elementos = None):
	if(elementos == None):
		elementos = grafo.obtenerVertices()

	cola = deque()
	grado_entrada = {}
	resultado = []

	for i in elementos:
		grado_entrada[i] = 0
	for v in elementos:
		for w in grafo.obtenerAdyacentes(v):
			if w in grado_entrada:
				grado_entrada[w] += 1
	for z in elementos:
		if grado_entrada[z] == 0:
			cola.append(z)

	while len(cola) > 0:
		v = cola.popleft()
		for w in grafo.obtenerAdyacentes(v):
			if w in grado_entrada:
				grado_entrada[w] -= 1
				if grado_entrada[w] == 0:
					cola.append(w)
		resultado.append(v)
	if len(resultado) != len(elementos):
		return None
	return resultado

'''def diametro(grafo):
	_padres = {}
	_orden = {}
	maximo = 0
	for v in grafo.obtenerVertices():
		padres, distancias = bfs(grafo, v)
		for w in distancias:
			if distancias[w] > maximo:
				maximo = distancias[w]
				_padres = padres
				_orden = distancias
	
	return maximo, _padres, _orden 
'''


'''
def vertices_distancia_n(grafo, origen, n):
	q = deque()
	q.append(origen)
	distancia = {}
	distancia[origen] = 0
	lista = []
	while q:
		v = q.popleft()
		for w in grafo.obtenerAdyacentes(v):
			if w not in distancia:
				distancia[w] = distancia[v] + 1
				q.append(w)
				if distancia[w] == int(n):
					lista.append(w)
				if distancia[w] > int(n):
					return lista 
'''
