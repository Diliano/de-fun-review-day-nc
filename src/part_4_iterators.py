def indexer(text):
    if text:
        for index, char in enumerate(text):
            if (index == 0 and not char.isspace()) or (not char.isspace() and text[index - 1].isspace()):
                yield index

def cool_cat(*args):
    for arg in args:
        if isinstance(arg, (str, list)):
            yield from arg
        elif isinstance(arg, dict):
            yield from arg.items()