import collections


def is_collection(x):
    """str is theoretically a collection, but in practice we use it as a primitive"""
    return isinstance(x, (list, tuple, dict, set, frozenset, collections.deque))


def is_primitive(x):
    """str is theoretically a collection, but in practice we use it as a primitive"""
    return isinstance(x, (str, int, float, bool, type(None)))
