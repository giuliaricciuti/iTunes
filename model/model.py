import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._album = DAO.getAllAlbum()
        self._idMapAlbum = {}
        for a in self._album:
            self._idMapAlbum[a.AlbumId] = a

    def buildGraph(self, durata):
        self._graph.clear()
        self._nodes = DAO.getAlbumDurata(durata, self._idMapAlbum)
        self._graph.add_nodes_from(self._nodes)

    def getNodesNumber(self):
        return self._graph.number_of_nodes()
