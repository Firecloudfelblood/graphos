class Vertice:
    def __init__(self, clave):
        self.id = clave
        self.conectadoA = {}

    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = [ponderacion]

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerPonderacion(self, vecino):
        if vecino in self.conectadoA:
            return self.conectadoA[vecino]
        else:
            return None


class Grapho:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self, clave):
        self.numVertices += 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def agregarArista(self, de, a, costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecinos(self.listaVertices[a], costo)
