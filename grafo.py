import random

class Grafo():
    '''
    El grafo puede recibir dos parámetros:
    1: True si es dirigido o False en caso contrario
    2: un diccionario con los vertices a agregar
    '''
    
    def __init__(self, dirigido = True, vertices = {}):
        self.es_dirigido = dirigido
        self.vertices = vertices
        self.cantidad = len(vertices)

    def agregarVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}
            self.cantidad += 1

    def eliminarVertice(self, v):
        if v in self.vertices:
            del self.vertices[v]
        
            for w in self.vertices:
                if v in self.vertices[w]:
                    del self.vertices[w][v]
            
            self.cantidad -= 1

    def agregarArista(self, v, w, peso = 1):
        if v in self.vertices and w in self.vertices:
            self.vertices[v][w] = peso
            if not self.es_dirigido:
                self.vertices[w][v] = peso

    def eliminarArista(self, v, w):
        if v in self.vertices and w in self.vertices[v]:
            del self.vertices[v][w]
            if not self.es_dirigido:
                del self.vertices[w][v]

    def obtenerPeso(self, v, w):
        if v in self.vertices and w in self.vertices[v]:
            return self.vertices[v][w]

    def verticeExiste(self, v):
        if v in self.vertices:
            return True
        return False

    def obtenerRandomVertice(self):
        return random.choice(list(self.vertices.keys()))

    def obtenerVertices(self):
        return self.vertices.keys()

    def obtenerAdyacentes(self, v):
        adyacentes = []
        if v in self.vertices:
             adyacentes = self.vertices[v].keys()
        return adyacentes

    def __len__(self):
        return self.cantidad

    def __del__(self): #Borrar uno por uno? 
        del self.vertices

    def __str__(self):
        return str(self.vertices)

