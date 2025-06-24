from database.DAO import DAO
from model.album import Album
from model.model import Model

m = Model()
m.creaGrafo(20)
print(m.getNum())
a = Album(141, 'Greatest Hits', 100, 56.43)
a2 = Album(75, 'Angel Dust', 82, 13.86)
print(m.getBestPath(a, a2, 20))