import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._albums = []
        self._idMapAlbum = {}
        self.bestPath = []
        self._bestScore = 0


    def getBestPath(self, start, stop, soglia):
        self.bestPath = []
        self._bestScore = 0
        parziale = [start]
        vicini = self._graph.neighbors(start)
        for v in vicini:
            if self._graph[start][v]['weight']>=soglia:
                parziale.append(v)
                self._ricorsione(parziale, stop, soglia)
                parziale.pop()
        return self.bestPath, self._bestScore


    def _ricorsione(self, parziale, stop, soglia):
        if parziale[-1]==stop:
            bilancioTot=0
            for p in parziale:
                bilancioTot+=self.getBilancio(p)
            if bilancioTot>self._bestScore:
                self._bestScore = bilancioTot
                self.bestPath = copy.deepcopy(parziale)
            return
        for v in self._graph.neighbors(parziale[-1]):
            if (v not in parziale and
                    self._graph[parziale[-1]][v]['weight'] >= soglia):
                parziale.append(v)
                self._ricorsione(parziale, stop, soglia)
                parziale.pop()


    def creaGrafo(self, n):
        self._albums = DAO.getAllAlbums(n)
        for a in self._albums:
            self._idMapAlbum[a.AlbumId]=a
        self._graph.add_nodes_from(self._albums)
        self.addEdges()

    def addEdges(self):
        for i in range(len(self._albums)):
            u = self._albums[i]
            for j in range(i+1, len(self._albums)):
                v = self._albums[j]
                peso = abs(u.price-v.price)
                if u.AlbumId != v.AlbumId and peso>0:
                    self._graph.add_edge(u, v, weight = peso)


    def getAdiacenti(self, a):
        adiacenti = []
        for n in self._graph.neighbors(a):
            bilancio = self.getBilancio(n)
            adiacenti.append((n, bilancio))
            adiacenti.sort(key=lambda x: x[1], reverse=True)
        return adiacenti

    def getBilancio(self, n):
        somma=0
        for n1 in self._graph.neighbors(n):
            somma+=self._graph[n][n1]['weight']
        bilancio = somma/len(list(self._graph.neighbors(n)))
        return bilancio

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()