class TreeNode:
    def __init__(self, label):
        self.parent = None
        self.left_child = None
        self.right_sibling = None
        self.label = label
        
    def __str__(self):
        return "TreeNode(%s)" % str(self.label)

class Tree:
    def __init__(self):
        self.root = None

    def assign_root(self, label):
        assert self.root is None
        self.root = TreeNode(label)

    def is_empty(self):
        return self.root is None

    def add_new_node_1(self, parent, label):
        new_node = TreeNode(label)
        left_child = parent.left_child
        parent.left_child = new_node
        new_node.right_sibling = left_child
        new_node.parent = parent
        return new_node

    def add_new_node_2(self, parent, label):
        new_node = TreeNode(label)
        new_node.parent = parent
        if parent.left_child is None:
            parent.left_child = new_node
        else:
            left_child = parent.left_child
            while left_child.right_sibling is not None:
                left_child = left_child.right_sibling
            left_child.right_sibling = new_node
        return new_node

    def add_new_node(self, parent, label):
        return self.add_new_node_2(parent, label)
    
    def find_in_subtree(self, label, node):
        if node.label == label:
            return node

        child = node.left_child
        while child is not None:
            result = self.find_in_subtree(label, child)
            if result is not None:
                return result
            child = child.right_sibling
        return None


    def find_by_label(self, label):
        if self.is_empty():
            return None
        return self.find_in_subtree(label, self.root)


    def add_new_node_by_label(self, parent_label, label):
        self.add_new_node(self.find_by_label(parent_label), label)

    def get_subtree_size(self, node):
        if node is None:
            return 0

        count = 1
        child = node.left_child
        while child is not None:
            count += self.get_subtree_size(child)
            child = child.right_sibling

        return count


    def get_size(self):
        if self.is_empty():
            return 0
        return self.get_subtree_size(self.root)

    def pre_order(self, node):
        order_list = list()
        if node is None:
            return order_list

        order_list.append(node.label)
        child = node.left_child
        while child is not None:
            order_list.extend(self.pre_order(child))
            child = child.right_sibling
        return order_list

    def post_order(self, node):
        order_list = list()
        if node is None:
            return order_list

        child = node.left_child
        while child is not None:
            order_list.extend(self.post_order(child))
            child = child.right_sibling
        order_list.append(node.label)
        return order_list

    def in_order(self, node):
        order_list = list()
        if node is None:
            return order_list
        child = node.left_child
        order_list.extend(self.in_order(child))
        order_list.append(node.label)
        while child is not None:
            child = child.right_sibling
            order_list.extend(self.in_order(child)) 
        return order_list

import 	sys
from random import shuffle, randint
argv = sys.argv
n = int(argv[1])
file_name = int(argv[2])

node_list = [i for i in range(n)]
shuffle(node_list)
node_degree = [0 for i in range(n)]
t = Tree()
t.assign_root(node_list[0] + 1)

for i in range(n - 1):
    ind = randint(0, i)
    while node_degree[ind] >= 2:
        ind = randint(0, i)
    t.add_new_node_by_label(node_list[ind] + 1, node_list[i + 1] + 1)
    node_degree[ind] += 1

with open("input/input" + str(file_name) + ".txt", "w") as input_file:
	input_file.write(str(t.pre_order(t.root)) + "\n")
	input_file.write(str(t.in_order(t.root)) + "\n")
with open("output/output" + str(file_name) + ".txt", "w") as output_file:
    output_file.write(str(t.post_order(t.root)) + "\n")
