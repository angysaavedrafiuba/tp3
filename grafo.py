import random

class Grafo():
    
    def __init__(self,vertices = {}):
        self.vertices = vertices
        self.cantidad = len(vertices)

    def agregarVertice(self, v):
        self.vertices[v] = {}
        self.cantidad += 1

    def eliminarVertice(self, v):
        del self.vertices[v]
        for w in self.vertices:
            if v in self.vertices[w]:
                del self.vertices[w][v]
        self.cantidad -= 1

    def agregarArista(self, v, w, peso = 1):
        self.vertices[v][w] = peso

        # Consultar como hacer en caso de no dirigido para agregar y borrar
        #if peso == 1:
        #    self.vertices[w][v] = peso

    def eliminarArista(self, v, w):
        peso = self.vertices[v][w]
        del self.vertices[v][w]
        #if peso == 1:
        #    del self.vertices[w][v]

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

