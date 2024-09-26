def flatten(lst, depth=1):
    result = []

    for element in lst:
        if isinstance(element, list) and depth > 0:
            result.extend(flatten(element, depth - 1))
        else:
            result.append(element)

    return result

def deep_entries():
    # implement me
    pass
