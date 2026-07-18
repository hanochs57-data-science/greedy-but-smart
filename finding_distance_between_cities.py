graph ={
    'Mumbai':[('Pune',75),('Indore',500),('Delhi',700)],
    'Pune':[('Mumbai',75),('Indore',300),('Delhi',500)],
    'Indore':[('Mumbai',500),('Pune',300),('Delhi',200)],
    'Delhi':[('Mumbai',700),('Pune',500),('Indore',200)],
    'Navi Mumbai':[]
}
heuristic ={
    'Mumbai':20,
    'Pune':100,
    'Delhi':650,
    'Indore':450,
    'Navi Mumbai': 0,
}

def astar(start,goal):
    queue=[]
    heapq.heappush(queue,(heuristic[start],0,start,[start]))
    visited = set()
    while queue:
        f_cost, g_cost, city, path = heapq.heappop(queue)
        if city == goal: return g_cost, path
        if city not in visited: visited.add(city)
        for neighbor, distance in graph[city]:
            new_g = g_cost + distance
            new_f = new_g + heuristic[neighbor]

            heapq.heappush(queue,(new_f,new_g,neighbor,path+[neighbor]))

    return None,[]

cost, path = astar('Mumbai','Delhi')
print("Shortest Path using A* Search: ")
print("Path: ","->".join(path))
print("Total Cost: ",cost)
print("HANOCH SHETTY T043")
