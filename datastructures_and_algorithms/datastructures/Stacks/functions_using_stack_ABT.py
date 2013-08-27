from stacks_concrete import RegisteredStack

def one(stack):
    """
    Returns true if the stack contains but one element
    """
    top     = stack.pop()
    empty   = stack.empty()
    stack.push(top)
    return empty
