class Node:
    '''
    Class to represent a node of the tree and store its contents
    '''
    def __init__(self, interval=None, max=None):
        self.lb = interval[0]
        self.hb = interval[1]
        self.max = interval[1]
        self.left = None
        self.right = None


class IntervalTree:
    def __init__(self):
        '''
        Initializes the tree
        '''
        self.root = None

    def getRoot(self):
        '''
        Return reference of the root of the tree
        '''
        return self.root

    def add(self, interval, node=None):
        '''
        Helper function to add a node to the tree
        '''
        if self.root == None:
            self.root = Node(interval)
        else:
            if node == None:
                node = self.root
            if interval[1] > node.max:
                node.max = interval[1]
            if interval[0] < node.lb:
                if(node.left != None):
                    self.add(interval, node.left)
                else:
                    node.left = Node(interval)
            else:
                if(node.right != None):
                    self.add(interval, node.right)
                else:
                    node.right = Node(interval)


    def delete(self, key, node=None):
        '''
        Helper function to delete a node from the tree
        '''
        if self.root == None:
            return None
        else:
            global storage

            if node == None:
                node = self.root

            if node.lb == key[0] and node.hb == key[1]:
                if node.left is None and node.right is None:
                    if storage.lb < node.lb:
                        storage.right = None
                    else:
                        storage.left = None
                elif node.left is None:
                    if storage.lb < node.lb:
                        storage.right = node.right
                    else:
                        storage.left = node.right
                elif node.right is None:
                    if storage.lb < node.lb:
                        storage.right = node.left
                    else:
                        storage.left = node.left
                else:
                    curr = node.right
                    while curr.left:
                        curr = curr.left
                    if storage.lb < node.lb:
                        storage.right = curr
                        curr.left = node.left
                    elif storage.lb > node.lb:
                        storage.left = curr
                        curr.right = node.right

            storage = node
            node.max = node.hb
            if key[0] < node.lb:
                if node.left != None:
                    self.delete(key, node.left)
            else:
                if node.right != None:
                    self.delete(key, node.right)

    def display(self):
        '''
        Helper function to display the tree on console
        '''
        if self.root != None:
            self.displayRecursive(self.root)

    def displayRecursive(self, node):
        if node.left != None:
            self.displayRecursive(node.left)
        print("Interval: [{}, {}], Maximum: {}.".format(node.lb, node.hb, node.max))
        if node.right != None:
            self.displayRecursive(node.right)

    def search(self, key, node=None):
        '''
        Function to search for intervals which overlap with given search key
        '''
        if self.root != None:
            if node == None:
                node = self.root
            if key[0] > node.lb and key[1] < node.hb:
                print("Interval found: [{}, {}] ".format(node.lb, node.hb))
            elif key[0] < node.lb and node.left != None:
                self.search(key, node.left)
            elif key[0] > node.lb and node.right != None:
                self.search(key, node.right)
            elif node.left == None and node.right == None:
                print("No node overlapping with the interval")
