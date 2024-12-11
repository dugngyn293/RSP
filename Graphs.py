from queue import deque
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adjList = {}
n = 4
visit = set()
for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)

def dfs(node):
    if node in visit:
        return
    visit.add(node)
    # Process the node if needed, e.g., print it.
    print(node)
    for neighbor in adjList[node]:
        dfs(neighbor)

dfs("A")
def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)  # Process the node (e.g., print it)

        for neighbor in adjList[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
# Count paths (backtracking)
def backtracking(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)

    return count

# Shortest path from node to target
def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = deque()
    queue.append(node)

    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length

            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length