def reducer(key, values):
    """
    The Reducer.

    Takes a key (e.g. "apple") and a list of all the values that
    were emitted for that key (e.g. [1, 1, 1, 1]), and combines
    them into a single final result.

    Example:
        key = "python", values = [1, 1, 1, 1]
        returns ("python", 4)
    """
    total = sum(values)

    return key, total
