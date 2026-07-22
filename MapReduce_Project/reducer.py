def reducer(key, values):
    """
    The Reducer.

    Takes a key (e.g. "apple") and a list of all the values that
    were emitted for that key (e.g. [1, 1, 1, 1]), and combines
    them into a single final result.

    Example:
        key = "apple", values = [1, 1, 1, 1]
        returns ("apple", 4)
    """
    total = sum(values)

    return key, total