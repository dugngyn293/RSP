class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dfs(self, root):
        if not root:
            return
        self.dfs(self, root.left)
        print(root.val)
        self.dfs(self, root.right)

    def bfs(self, root):
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
            if curr.left:
                queue.append(root.left)
            if curr.right:
                queue.append(root.right)
            