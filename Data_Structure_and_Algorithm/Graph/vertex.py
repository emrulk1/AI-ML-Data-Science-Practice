class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,neighbor_id,weight=0):
        self.connectedTo[neighbor_id] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([neighbour.id for neighbour in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,neighbor_id):
        return self.connectedTo[neighbor_id]