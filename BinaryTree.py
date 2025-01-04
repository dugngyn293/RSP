from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data <= root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)

def print_preorder(root):
    if root:
        print(root.data, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)

def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.data, end=" ")

# Depth-First Search (DFS)
def dfs(root):
    if not root:
        return
    dfs(root.left)        # Visit left subtree
    print(root.data, end=" ")  # Visit root
    dfs(root.right)       # Visit right subtree

# Breadth-First Search (BFS)
def bfs(root):
    queue = deque()  # Create a queue
    if root:
        queue.append(root)  # Start with the root
    while queue:
        curr = queue.popleft()  # Dequeue the current node
        print(curr.data, end=" ")  # Process the current node
        if curr.left:             # Enqueue left child if it exists
            queue.append(curr.left)
        if curr.right:            # Enqueue right child if it exists
            queue.append(curr.right)

# Building the binary tree
root = Node(50)

root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# Printing traversals
print("In-order traversal:")
print_inorder(root)

print("\nPre-order traversal:")
print_preorder(root)

print("\nPost-order traversal:")
print_postorder(root)

# DFS and BFS Traversals
print("\nDFS Traversal:")
dfs(root)

print("\nBFS Traversal:")
bfs(root)
