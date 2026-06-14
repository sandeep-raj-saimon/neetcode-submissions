
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_node_mapping = {}

        curr = head
        while curr is not None:
            # taking care of duplicate to original node mapping
            new_node = Node(curr.val)
            new_node_mapping[curr] = new_node

            curr = curr.next
        # in above code we have handled the mapping
        new_head = None
        new_curr = None
        curr = head

        while curr is not None:
            new_node = new_node_mapping.get(curr)
            new_node.random = new_node_mapping.get(curr.random)  # Set random pointer
            if new_head is None:
                new_head = new_node
                new_curr = new_node
            else:
                new_curr.next = new_node  # Set next pointer
                new_curr = new_node
            curr = curr.next

        return new_head