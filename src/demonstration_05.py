"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    # sort() can use a key=none parameter
    # list_item is the parameter, and lambda is the function it's using to create a mini return function
    lst.sort(key = lambda list_item: len(list_item))
    print(lst)
    
    # this also works
    # lst.sort(key = len)
    # print(lst)
    
# with the lambda function, there is no need to have a seperate return statement
sort_by_length(["apple", "banana", "grapefruit", "tangerine"])