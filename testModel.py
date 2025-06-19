from database.DAO import DAO
from model.album import Album
from model.model import Model

m = Model()
m.creaGrafo(1500)
print(m.getNum())
a = Album(228, "Heroes, Season 1", 148, 2599142.0870)
print(m.handleConnComp(a))


