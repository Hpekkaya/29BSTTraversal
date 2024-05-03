class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
  
    def BFS(self):
        # 1 Assign curent_node to self.root
        current_node = self.root
        # 2 Initialize the Queue and Results List
        results, queue = [], []
        # queue = []
        # 3 Append the Queue the current_Node
        queue.append(current_node)
        # 4 Loop though the all Tree (len > 0)
        while len(queue) > 0:
            # 41 Pop and assign to the currentNode
            current_node = queue.pop(0)
            # 42 Append The current value to Result List
            results.append(current_node.value)
            # 43 Check if current left is not None Append Current left to Queue
            if current_node.left is not None:
                queue.append(current_node.left)
            # 4 Check if current right is not None Append Current right to Queue
            if current_node.right is not None:
                queue.append(current_node.right)
        # 5 return result
        return results




my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())



"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 76, 18, 27, 52, 82]

 """





                



 