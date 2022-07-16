# coding=utf-8
from Trees.QuadTree import QuadTreeNode


def construct_quad_tree(matrix):
    """
    Leetcode 427
    :type matrix: list
    """
    m = len(matrix)
    if m != len(matrix[0]) or ((m - 1) & m != 0):
        raise Exception("Must be 2^x * 2^x matrix")

    if m == 1:
        return QuadTreeNode(val=matrix[0][0], isLeaf=1)
    else:
        top_left_node = construct_quad_tree([sub_matrix[:(m // 2)] for sub_matrix in matrix[:(m // 2)]])
        top_right_node = construct_quad_tree([sub_matrix[(m // 2):] for sub_matrix in matrix[:(m // 2)]])
        bottom_left_node = construct_quad_tree([sub_matrix[:(m // 2)] for sub_matrix in matrix[(m // 2):]])
        bottom_right_node = construct_quad_tree([sub_matrix[(m // 2):] for sub_matrix in matrix[(m // 2):]])
        if top_left_node.val == top_right_node.val == bottom_left_node.val == bottom_right_node.val and \
                (top_left_node.isLeaf & top_right_node.isLeaf & bottom_left_node.isLeaf & bottom_right_node.isLeaf == 1):
            return QuadTreeNode(val=top_left_node.val, isLeaf=1)
        else:
            return QuadTreeNode(val=0, isLeaf=0, topLeft=top_left_node, topRight=top_right_node,
                                bottomLeft=bottom_left_node, bottomRight=bottom_right_node)
