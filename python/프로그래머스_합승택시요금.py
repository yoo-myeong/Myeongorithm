import heapq

def dijkstra(s,e):
    global graph, length
    visited = [1e9] * (length+1)
    visited[s] = 0
    h_list = [[0,s]]
    heapq.heapify(h_list)
    
    while h_list:
        cost, node = heapq.heappop(h_list)
        
        if cost > visited[node] : continue
            
        for n_node, n_cost in graph[node]:
            n_cost += cost
            
            if n_cost < visited[n_node]:
                visited[n_node] = n_cost
                heapq.heappush(h_list, [n_cost, n_node])
                
    return visited[e]

def solution(n, s, a, b, fares):
    global graph, length
    answer = 1e9
    
    graph = [[] for _ in range(n+1)]
    length = n
    
    for i,j,cost in fares:
        graph[i].append([j,cost])
        graph[j].append([i,cost])
    
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s,i)+dijkstra(i,a)+dijkstra(i,b))
    
    return answer
