from graph import Graph
from pprint import pprint

if __name__ == "__main__":
    
    g = Graph()

    for i in range(6):
        g.addVertex(i)

    pprint(g.vertList)

    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)

    print("\nEdges added to graph :\n")
    for u in g:
        for v in u.getConnections():
            print("( %s , %s )" % (u.getId(), v.getId()))