# coding=utf-8
from queue import Queue


class QuadTreeNode(object):
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def show_tree(self):
        queue = Queue()
        tree = [[self.isLeaf, self.val]]
        if not self.isLeaf:
            queue.put(self.topLeft)
            queue.put(self.topRight)
            queue.put(self.bottomLeft)
            queue.put(self.bottomRight)
        tree_level = 1
        counter = 0
        leaf_counter = 0
        while not queue.empty():
            cur_node = queue.get()
            counter += 1
            if cur_node is not None:
                tree.append([cur_node.isLeaf, cur_node.val])
                if not cur_node.isLeaf:
                    queue.put(cur_node.topLeft)
                    queue.put(cur_node.topRight)
                    queue.put(cur_node.bottomLeft)
                    queue.put(cur_node.bottomRight)
                else:
                    leaf_counter += 1
                    for _ in range(4):
                        queue.put(None)
            else:
                tree.append(None)
                leaf_counter += 1
            if leaf_counter == 4 ** tree_level:
                while tree[-1] is None:
                    tree.pop()
                break
            if counter == 4 ** tree_level:
                counter = 0
                leaf_counter = 0
                tree_level += 1
        return tree
