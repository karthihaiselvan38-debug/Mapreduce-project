def mapper(line):
    """
    The Mapper.

    Takes ONE line of text and converts every word in it into a
    (word, 1) pair. It does NOT count anything -- it just tags
    each occurrence of a word with the number 1.

    Example:
        Input line: "apple banana apple"
        Output:     [("python", 1), ("java", 1), ("python", 1)]
    """
    words = line.strip().split()
    output = []

    for word in words:
        output.append((word, 1))

    return output
