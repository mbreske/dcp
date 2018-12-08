# In a directed graph, each node is assigned an uppercase letter.
# We define a path's value as the number of the most frequently-occurring letter along that path.
# For example, if a path in the graph goes through "ABACA", the value of the path is 3,
# since there are 3 occurrences of 'A' on the path.

# Given a graph with n nodes and m directed edges, return the largest value path of the graph.
# If the largest value is infinite, then return null.

# The graph is represented with a string and an edge list.
# The i-th character represents the uppercase letter of the i-th node.
# Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node.
# Self-edges are possible, as well as multi-edges.

# For example, the following input graph:

# ABACA
# [(0, 1),
#  (0, 2),
#  (2, 3),
#  (3, 4)]
# Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

# The following input graph:

# A
# [(0, 0)]
# Should return null, since we have an infinite loop.
from collections import defaultdict

class node:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.visited = False
    
    def addChild(self, node):
        self.children.append(node)

def largestPath(str,edges):
    root = buildGraph(str,edges)
    maxLen = 0
    root_letters = defaultdict(int)
    root_letters[root.data] = 1
    letters = defaultdict(int)
    stack = []
    stack.append(root)
    while(len(stack)):
        curr = stack.pop()
        curr.visited = True
        letters[curr.data] += 1
        if len(curr.children) == 0:
            pathLen = max(letters.values())
            if pathLen > maxLen:
                maxLen = pathLen
            letters = root_letters
            continue
        for _,v in enumerate(curr.children):
            if not v.visited:
                stack.append(v)
    return maxLen
    
def buildGraph(str,edges):
    nodes = {}
    for i,char in enumerate(str):
        nodes[i] = node(char)
    for _,edge in enumerate(edges):
        i,j = edge
        parent = nodes[i]
        parent.addChild(nodes[j])
    return nodes[0]

if __name__ == '__main__':
    str = 'ABACA'
    edges = [(0, 1),
            (0, 2),
            (2, 3),
            (3, 4)]
    result = largestPath(str,edges)
    print(result)


