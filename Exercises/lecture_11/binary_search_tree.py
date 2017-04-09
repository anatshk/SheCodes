"""
Binary Search Tree

1. https://en.wikipedia.org/wiki/Binary_search_tree
2. Define a class TreeNode and write the ctor which takes one argument (value) and initializes the left and right children to None.
3. Write a function to prints the tree.
4. Write a function that inserts a new value in the tree at the right location.
5. Write a function that looks up a value in the tree.
6. Write a function that removes a value from the tree.
"""

from copy import copy


class TreeNode(object):
    def __init__(self, value, root=False):
        self.value = value
        self.left = None
        self.right = None
        self.root = root

    def __repr__(self):
        left = self.left.get_tree() if self.left is not None else None
        right = self.right.get_tree() if self.right is not None else None
        return "{}<{}>{}".format(str(left) + ', ' if left is not None else '',
                                 self.value,
                                 ', ' + str(right) if right is not None else '')

    def get_tree(self):
        tree = [self.value]
        if self.left is not None:
            tree = self.left.get_tree() + tree
        if self.right is not None:
            tree = tree + self.right.get_tree()
        return tree

    def print_tree(self):
        print('Tree: {}'.format(self.get_tree()))

    def insert_value(self, value):  # TODO: convert to inplace=False?
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)  # no left branches - initialize
            else:
                self.left.insert_value(value)  # insert value to left branch
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert_value(value)
        else:
            pass  # if value exists - don't do anything

    def is_in_tree(self, value):
        if self.value == value:
            return self
        if value < self.value:
            if self.left is None:
                return None
            return self.left.is_in_tree(value)
        if value > self.value:
            if self.right is None:
                return None
            return self.right.is_in_tree(value)

    def remove_value(self, value):
        assert self.is_in_tree(value), 'Sorry, {} not in tree'.format(value)
        return TreeNode._remove_value(self, value)

    @staticmethod
    def _remove_value(node, value):
        """
        1. Deleting a node with no children: simply remove the node from the tree.
        2. Deleting a node with one child: remove the node and replace it with its child.
        3. Deleting a node with two children: call the node to be deleted D. Do not delete D.
           Instead, choose either its in-order predecessor node or its in-order successor node as replacement node E.
           Copy the user values of E to D.
           If E does not have a child simply remove E from its previous parent G.
           If E has a child, say F, it is a right child. Replace E with F at E's parent.
        """
        tree_node = copy(node)
        if tree_node.value == value:
            # reached the node to remove
            if tree_node.left is None and tree_node.right is None:
                return None  # Remove node with no children
            elif tree_node.left is None:
                return tree_node.right  # node only has right child
            elif tree_node.right is None:
                return tree_node.left  # node only has left child
            else:
                # Node has both left and right children - remove parent and combine left and right
                # (right node is the replacement node)
                return TreeNode._combine_nodes(tree_node.right, tree_node.left)
        if value < tree_node.value:
            tree_node.left = TreeNode._remove_value(tree_node.left, value)
        if value > tree_node.value:
            tree_node.right = TreeNode._remove_value(tree_node.right, value)
        return tree_node

    @staticmethod
    def _combine_nodes(right, left):
        """
        Combines the right and left nodes of self.
        Attaches left on right in correct leaf node.
        """
        current_node = copy(right)
        while current_node.left is not None:
            if left.value < current_node.value:
                current_node = current_node.left
            elif left.value > current_node.value:
                current_node = current_node.right
            else:
                raise Exception('should not happen')
        else:
            # we found the correct position for the 'other' node
            if left.value < current_node.value and current_node.left is None:
                current_node.left = left
            elif left.value > current_node.value and current_node.right is None:
                current_node.right = left
            else:
                raise Exception('should not happen')
        return right


