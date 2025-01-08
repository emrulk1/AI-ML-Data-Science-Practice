from collections import deque
from pprint import pprint

def bfs(graph,start):
    q=deque()
    q.append(start)
    visited=set()
    visited.add(start)
    # print(start , end = ' ')
    while q:
        vertex=q.pop()
        print(vertex, end = '')
        # if vertex != start:
        #     print("-->", end = '')
        # print(vertex, end =' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                print(" --> {}".format(neighbor), end ='')
                visited.add(neighbor)
                q.append(neighbor)
        print("\n")
    return visited
                

if __name__ == "__main__":
    
    graph={
        0:[1,2],
        1:[0,2],
        2:[3],
        3:[2],
        4: []
    }

print("input graph is : ")
pprint(graph)
print("\n")

start_node = int(input())
print("start_node : ", start_node)

try:
    print("Following is the Breadth-First Search result starting from {}".format(start_node), end = "\n\n")
    bfs(graph, start_node)

except:
    print("BFS is not possible since {} not found in the graph".format(start_node))
