#!/bin/python3

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

    def __repr__(self):
        return self.__str__()


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            current_node = self.root
            while True:
                if val < current_node.info:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = Node(val)
                        break
                elif val > current_node.info:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = Node(val)
                        break
                else:
                    break

    @property
    def tree_root(self) -> Node:
        return self.root

    def get_depth(self, level):
        sym = ''
        for i in range(*level):
            pass

    @property
    def print_level_order(self):
        out = []
        if self.root:
            queue = []
            queue.append(self.root)
            while len(queue):
                cur_node: Node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                out.append(cur_node)
        return out

    @property
    def in_order(self):
        """
        Left, Root, Right
        :return:
        """
        out = []
        if self.root:
            stack = []
            current_node: Node = self.root
            while True:
                if current_node is not None:
                    stack.append(current_node)
                    current_node = current_node.left
                else:
                    if len(stack):
                        popped_node = stack.pop()
                        out.append(popped_node)
                        current_node = popped_node.right
                    else:
                        break
        return out

    @property
    def pre_order(self):
        """
        Root, Left, Right
        :return:
        """
        out = []
        #stack.append(self.root)
        if self.root:
            stack = []
            cur_node = self.root
            stack.append(cur_node)
            while len(stack):
                cur_node = stack.pop()
                out.append(cur_node)
                if cur_node.right:
                    stack.append(cur_node.right)
                if cur_node.left:
                    stack.append(cur_node.left)
        return out

    @property
    def post_order(self):
        """
        Left, Right, Root
        :return:
        """
        out = []
        
        return out
