import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._tracks = []
        self._idMapTracks = {}


    def creaGrafo(self, min, max, genere):
        self._graph.clear()
        self._tracks = DAO.getAllTracks(min, max, genere)
        for t in self._tracks:
            self._idMapTracks[t.TrackId] = t
        self._graph.add_nodes_from(self._tracks)
        self.addEdges(min, max, genere)

    def addEdges(self, min, max, genere):
        self._archi = DAO.getAllArchi(min, max, genere)
        for a in self._archi:
            u = self._idMapTracks[a[0]]
            v = self._idMapTracks[a[1]]
            self._graph.add_edge(u, v)

    def getAllGeneri(self):
        return DAO.getAllGeneri()

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getConnectedComponent(self):
        res = []
        for n in nx.connected_components(self._graph):
            num_p=0
            subgraph = self._graph.subgraph(n)
            for u, v in subgraph.edges():
                for a in self._archi:
                    if u == self._idMapTracks[a[0]] and v ==self._idMapTracks[a[1]]:
                        num_p+=a[2]
            res.append((len(n), num_p))
        return res



