def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print(node, end = ' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


if __name__ == '__main__':

    # Using a Python dictionary to act as an adjacency list
    graph = {
        '5' : ['3','7'],
        '3' : ['2', '4'],
        '7' : ['8'],
        '2' : [],
        '4' : ['8'],
        '8' : []
    }

    visited = set() # Set to keep track of visited nodes of graph.

    start_node = input()
    print("start_node : ", start_node)
    
    try:
        print("Following is the Depth-First Search result starting from {}".format(start_node))
        dfs(visited, graph, start_node)
    except:
        print("DFS is not possible since {} not found in the graph".format(start_node))
    
    
