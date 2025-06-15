from database.DAO import DAO
from model.album import Album
from model.model import Model

m = Model()
m.creaGrafo(4500)
print(m.getNum())
a = Album(151, "Load", 50, 4637.011)
print(m.getBilancio(a))