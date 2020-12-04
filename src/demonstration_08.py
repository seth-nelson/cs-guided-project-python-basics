"""
Challenge #8:

Create a function that returns the number of arguments it was called with.

Examples:
- num_args() ➞ 0
- num_args("foo") ➞ 1
- num_args("foo", "bar") ➞ 2
- num_args(True, False) ➞ 2
- num_args({}) ➞ 1
"""

# positional vs named (keyword-only) argument:
    #arg1 and arg2 are positional. named_arg = named (must have input)
    # def num_args(arg1, arg2, named_arg=None):
    
def num_args(*args, arg2):
    print(len(args))
    print(arg2)
    return
    
num_args('foo', 'bar', arg2='This is a keyword arg!')
# num_args('foo')