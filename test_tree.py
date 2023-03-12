import pytest
from binary_tree import *

def get_test_tree():
    root = Tree(9)
    nodes = [3, 7, [2, 4], 6, 8, 14, 1]
    root.insert_list(nodes)
    return root

def test_insert_list():
    root = get_test_tree()
    assert root.left.id_node == 3
    assert root.left.left.id_node == 2
    assert root.left.left.left.id_node == 1
    assert root.left.right.id_node == 7
    assert root.right.id_node == 14
    assert root.left.right.right.id_node == 8
    assert root.left.right.id_node == 7
    assert root.left.right.left.id_node == 4
    assert root.left.right.left.right.id_node == 6

def test_delete_leaf_node():
    root = get_test_tree()
    root.delete(1)
    assert root.findval(1) == "1 Not Found"

def test_find_min_value():
    root = get_test_tree()
    assert root.find_min() == 1

def test_find_max_value():
    root = get_test_tree()
    assert root.find_max() == 14

def test_find_min_value_empty_tree():
    root = Tree(None)
    assert root.find_min() == None

def test_find_max_value_empty_tree():
    root = Tree(None)
    assert root.find_max() == None






