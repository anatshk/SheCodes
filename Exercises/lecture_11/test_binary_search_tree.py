from Exercises.lecture_11.binary_search_tree import TreeNode

########################################################################################################################
# Test region
########################################################################################################################

# init
t = TreeNode(5, root=True)
assert t.left is None and t.right is None and t.value == 5, 'init fails'

# add value \ get tree
t.insert_value(3)
t.insert_value(100)
t.insert_value(5)
t.insert_value(10)
assert t.get_tree() == [3, 5, 10, 100], 'add fails'

# repr
assert t.__repr__() == '[3], <5>, [10, 100]'

# is in tree
t1 = t.is_in_tree(3)
assert t1.value == 3 and t1.left is None and t1.right is None, 'is in fails on 3'
t2 = t.is_in_tree(4)
assert t2 is None, 'is in fails on 4'

# remove value
t3 = t.remove_value(3)
assert t3.__repr__() == '<5>, [10, 100]'
assert t3.get_tree() == [5, 10, 100]

t4 = t.remove_value(100)
assert t4.__repr__() == '[3], <5>, [10]'
assert t4.get_tree() == [3, 5, 10]

t5 = t.remove_value(10)
assert t5.__repr__() == '[3], <5>, [100]'
assert t5.get_tree() == [3, 5, 100]

# what happens when node with 2 children is removed?
tt = TreeNode(5, root=True)
tt.insert_value(3)
tt.insert_value(100)
tt.insert_value(5)
tt.insert_value(10)
tt.insert_value(1)
tt.insert_value(4)
tt.insert_value(7)
tt.insert_value(12)
tt.insert_value(50)
tt.insert_value(11)
t6 = tt.remove_value(10)
assert t6.__repr__() == '[1, 3, 4], <5>, [7, 11, 12, 50, 100]'

# TODO: what happens when root node is removed?
t7 = t.remove_value(5)  # TODO: does not work
assert t7.__repr__() == '[3, 10], <100>'
assert t7.get_tree() == [3, 10, 100]
