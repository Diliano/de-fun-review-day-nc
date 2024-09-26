def indexer(text):
    if text:
        for index, c in enumerate(text):
            if index == 0 and not c.isspace():
                yield index
            else:
                if not c.isspace() and text[index - 1].isspace():
                    yield index

def cool_cat():
    # implement me
    pass
