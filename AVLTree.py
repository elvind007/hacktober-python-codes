

# Heigth Parameter
# height = max(height of left child, height of right child) + 1
# Blance Factor (left - right)
# 
# if negative, it is right heavy situation, make left rotation to rebalance
# roation does not change properties and O(logN) for rotation

class Node:
    def __init__(self, data, parent) -> None:
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0

class AVLTree:

    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)

        else:
            self.insert_node(data, self.root)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert_node(self, data, node):

        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1

                self.handle_volation(node)

        else:
            if node.right_node:
                self.insert_node(data, node.right_node)

            else:
                node.right_node = Node(data, node)
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1

                self.handle_volation(node)

        
    def remove_node(self, data, node):
        if node is None:
            return
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node")
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None

                elif parent is not None and parent.right_node == node:
                    parent.right_node = None

                elif parent is None:
                    self.root = None

                del node

                self.handle_volation(parent)

            elif node.left_node is None and node.right_node is not None:
                print("removing node with the single right child")

                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node

                elif parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                elif parent is None:
                    self.root = node.right_node

                node.right_node.parent = parent

                del node

                self.handle_volation(parent)

            elif node.left_node is not None and node.right_node is None:
                print("removing node with the single left child")

                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node

                elif parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node

                elif parent is None:
                    self.root = node.left_node

                node.left_node.parent = parent

                del node

                self.handle_volation(parent)

            else:
                print("removing node with both childern")

                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

    def handle_volation(self, node):
        while node is not None:
            node.height = max(self.calc_height(node.left_node,
            self.calc_height(node.right_node)) +1
            )
            self.violation_helper(node)

            node = node.parent

    def violation_helper(self, node):
        balance = self.calc_balance(node)

        if balance > 1:
            # we know it could be LL heavy or LR heavy

            if self.calc_balance(node.left_node) < 0:
                # For LR, roate L then R
                self.rotate_left(node.left_node)

            # For LL rotate R
            self.rotate_right(node)

        elif balance < -1:
            # we know it cloud be RR heavy or LR heavy

            if self.calc_balance(node.right_node) > 0:
                # For RL, rotate R then L
                self.rotate_right(node.right_node)

            self.rotate_left(node)


    def calc_height(self, node):
        if node is None:
            return -1

        return node.height
    
    def calc_balance(self, node):

        if node is None:
            return 0

        return self.calc_height(node.left_node) - self.calc_height(node.right_node)


    def handle_volation(self):
        pass