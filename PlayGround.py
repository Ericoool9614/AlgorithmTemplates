# coding=utf-8
from Trees.TreeConstructor import construct_quad_tree

grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
grid2 = [[1,1,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,1]]
# quad_tree = construct_quad_tree(grid)
quad_tree_2 = construct_quad_tree(grid2)
# print(quad_tree.show_tree())
print(quad_tree_2.show_tree())