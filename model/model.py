import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._album = []
        self._idMapAlbum={}

    def creaGrafo(self, durata):
        self._album = DAO.getAllAlbum(durata)
        for a in self._album:
            self._idMapAlbum[a.AlbumId]=a
        self.addEdges()

    def addEdges(self):
        archi = DAO.getAllEdges(self._idMapAlbum)
        for a in archi:
            self._graph.add_edge(a[0], a[1])

    def handleConnComp(self, album):
        set_album = nx.node_connected_component(self._graph, album)
        totTracks = 0
        for a in set_album:
            totTracks+=DAO.getTracksCount(a.AlbumId)[0]
        return len(set_album), totTracks

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()
