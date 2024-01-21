class Node:
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next_node=node2
node2.next_node=node3

current_node=node1

while current_node:
    print(current_node.data)
    current_node=current_node.next_node

#current_node.next_node=Node(4)
#print(current_node.data)