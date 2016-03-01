# Andy Yu
'''
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
You may not use division.
Difficulty: Medium - Hard

Solution notes:
O(n) time
O(n) space
dynamic programming
'''

def list_mult(arg):
    running_product = 1
    running_rev_product = 1
    result = [None] * len(arg)
    for number in xrange(len(arg)):
        result[number] = running_product
        running_product *= arg[number]
    for number in xrange(len(arg)-1, -1, -1):
        result[number] *= running_rev_product
        running_rev_product *= arg[number]
    return result
