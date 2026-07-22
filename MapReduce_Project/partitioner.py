def partition(key, number_of_reducers):
    """
    The Partitioner.

    Decides WHICH reducer a given key should be sent to.

    This must be deterministic: the same key must ALWAYS map to the
    same reducer, no matter which mapper produced it. Otherwise a
    single word's counts could get split across reducers and never
    correctly summed.

    Hint: Python's built-in hash() function, combined with the
    modulo operator (%), gives you exactly this property.
    """
    return hash(key) % number_of_reducers