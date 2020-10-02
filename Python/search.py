size = 10
matrix = [[0 for i in range(size)] for i in range(size)]

# Demo graph(Undirected considered) :
#         0
#        /  \
#       1    2 -- 4
#     / \    | \
#    5   6   3--9
#       /  \
#      7 -- 8

matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]


def bfs(matrix, start, goal):
    # Using a queue
    q = []
    visited = [0 for i in range(size)]
    visited[start] = 1
    q.append(start)
    path = []
    while(len(q)):
        k = q.pop(0)
        path.append(k)
        if(k == goal):
            return path
        for i in range(size):
            if(matrix[k][i] and not visited[i]):
                visited[i] = 1
                q.append(i)
    return path


def dfs(matrix, start, goal):
    # Using a stack
    s = []
    visited = [0 for i in range(size)]
    visited[start] = 1
    s.append(start)
    path = []
    while(len(s)):
        k = s.pop()
        path.append(k)
        if(k == goal):
            return path
        for i in range(size):
            if(matrix[k][i] and not visited[i]):
                visited[i] = 1
                s.append(i)
    return path


start = 0
end = 4
print('Starting node considered is : {} and ending node considered is {}'.format(start, end))

print('Path by DFS Traversal is ', dfs(matrix, start, end))
print('Path by BFS Traversal is ', bfs(matrix, start, end))
