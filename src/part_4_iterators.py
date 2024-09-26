def indexer(text):
    if text:
        for index, c in enumerate(text):
            if (index == 0 and not c.isspace()) or (not c.isspace() and text[index - 1].isspace()):
                yield index

def cool_cat(*args):
    for arg in args:
        if isinstance(arg, (str, list)):
            yield from arg
        elif isinstance(arg, dict):
            yield from arg.items()