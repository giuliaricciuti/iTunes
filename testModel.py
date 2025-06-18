from database.DAO import DAO
from model.model import Model

m = Model()
m.creaGrafo(240, 360, 2)
print(m.getNum())
print(m.getConnectedComponent())