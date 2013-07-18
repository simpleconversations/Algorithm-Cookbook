## binaryTree.py
##
## Written by Matthew Egan
## Written on 18th July
##
## Binary Tree implementation

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Insert new node with data
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        # Lookup node containing data
        if data < self.data:
            if self.left == None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right == None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        # Returns number of children
        if self is None:
            return None
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        # Delete node containing data
        node, parent = self.lookup(data)
        if node != None:
            children_count = node.children_count()
        if children_count == 0:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            del node
        elif children_count == 1:
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left == node:
                    parent.left = n
                else:
                    parent.right = n
            del node
        else:
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left
            node.data = successor.data
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def print_tree(self):
        # Print tree contents in order
        if self.left:
            self.left.print_tree()
        print self.data
        if self.right:
            self.right.print_tree()

    def compare_trees(self, node):
        # Compare 2 trees
        if node == None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left == None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if self.right == None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res

    def tree_data(self):
        # Generator to get the tree nodes data
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.data
                node = node.right

def main():
    root = Node(3)
    #root.print_tree()
    root.insert(8)
    root.insert(11)
    root.print_tree()
    print "---"
    root.delete(11)
    root.print_tree()
    
    root1 = Node(3)
    root1.insert(8)

    print root.compare_trees(root1)

if __name__ == "__main__": main()