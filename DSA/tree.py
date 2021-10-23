# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }

graph = {
    'P' : ["Q","R","S"],
    "Q" : ["P","R"],
    "R" : ["P","Q","T"],
    "S" : ["P"],
    "T" : ["R"]
}

visited = [] # List for visited nodes.
qt = []     #Initialize a qt

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  qt.append(node)

  while qt:          # Creating loop to visit each node
    m = qt.pop(0) 
    print (m, end = " ") 
    # print(qt)

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        qt.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'P')    #