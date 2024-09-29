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


class CoolCatIterator:
    def __init__(self, *collections):
        self.collection_iterators = ([iter(collection.items()) if isinstance(collection, dict) else iter(collection) for collection in collections])
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.collection_iterators):
            try:
                return next(self.collection_iterators[self.index])
            except StopIteration:
                self.index += 1
        raise StopIteration