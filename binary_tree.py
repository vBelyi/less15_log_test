class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    # Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

#Додавання до дерева елементів зі списку
    def insert_list(self, nodes):

        for node in nodes:
            if isinstance(node, int):
                self.insert(node)
            elif isinstance(node, list):
                self.insert_list(node)
            else:
                print(f"Node {node} не може бути додано до дерева")

#Пошук мінімального і максимального значення елементів
    def find_min(tree):
        if tree is None:
            return None
        current_node = tree
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.id_node

    def find_max(tree):
        if tree is None:
            return None
        current_node = tree
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.id_node

# Метод видалення елементів із дерева
    def delete(self, id_node):
        if self.id_node is None:
            return None

        if id_node < self.id_node:
            self.left = self.left.delete(id_node)
        elif id_node > self.id_node:
            self.right = self.right.delete(id_node)
        else:
            # Check if the node has any children
            if self.left is None:
                temp = self.right
                self.right = None
                return temp
            elif self.right is None:
                temp = self.left
                self.right = None
                return temp

            # If the node has two children
            temp = self.right.get_min_node()
            self.id_node = temp.id_node
            self.right = self.right.delete(temp.id_node)

        return self

root = Tree(9)
nodes = [3, 7, [2, 4], 6, 8, 14, 1]
root.insert_list(nodes)


print('Max value: ', Tree.find_max(root))
print('Min value: ', Tree.find_min(root))
root.delete(14)
root.print_tree()