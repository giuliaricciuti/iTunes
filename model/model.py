from networkx import DiGraph

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = DiGraph()
        self._idAlbum = {}

    def creaGrafo(self, n):
        self._graph.clear()
        self._idAlbum = {}
        self._album = DAO.getAlbums(n)
        self._graph.add_nodes_from(self._album)
        for a in self._album:
            self._idAlbum[a.AlbumId]=a
        self.addEdges(n)

    def addEdges(self, num):
        for a1 in (self._album):
            for a2 in self._album:
                peso = a1.n+a2.n
                if a1.n>a2.n and (peso>4*num):
                    self._graph.add_edge(a2, a1, weight = peso)
                elif a2.n>a1.n and (peso>4*num):
                    self._graph.add_edge(a1, a2, weight = peso)

    def getBilancio(self, album):
        result = []
        for s in self._graph.successors(album):
            bilancio = 0
            for e_in in self._graph.in_edges(s, data=True):
                bilancio+=e_in[2]["weight"]
            for e_out in self._graph.out_edges(s, data=True):
                bilancio-=e_out[2]["weight"]
            result.append((s, bilancio))
        result.sort(key = lambda x: x[1], reverse=True)
        return result

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()