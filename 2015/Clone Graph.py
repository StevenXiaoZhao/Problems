# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        trackQueue = []
        nodeMap = {}
        if(node == None):
            return(None)
        trackQueue.append(node)
        newNode = UndirectedGraphNode(node.label)
        nodeMap[newNode.label] = newNode
        while(len(trackQueue) > 0):
            head = trackQueue.pop(0)
            if(head.neighbors != []):
                for neighbor in head.neighbors:
                    if not neighbor.label in nodeMap:
                        newNeighbor = UndirectedGraphNode(neighbor.label)
                        nodeMap[head.label].neighbors.append(newNeighbor)
                        nodeMap[newNeighbor.label] = newNeighbor
                        trackQueue.append(neighbor)
                    else:
                        nodeMap[head.label].neighbors.append(nodeMap[neighbor.label])
        return(newNode)
ss = Solution()

a=UndirectedGraphNode('a')
b=UndirectedGraphNode('b')
c=UndirectedGraphNode('c')
d=UndirectedGraphNode('d')

a.neighbors.append(b)
a.neighbors.append(c)
a.neighbors.append(a)
c.neighbors.append(d)

result = ss.cloneGraph(a)
print(result.label)
for x in result.neighbors:
    print(x.label)
    if(x.neighbors !=[]):
        print(':'+x.neighbors[0].label)
