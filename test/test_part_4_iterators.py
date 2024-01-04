from src.part_4_iterators import indexer, cool_cat
import pytest

text1 = 'Hello'
text2 = 'Hello Dolly'
text3 = 'The moon shines bright. In such a night as this,'
text4 = """The
End"""
text5 = "  Space,   the final   frontier  "


@pytest.fixture(scope='function')
def file_data():
    with open('test/sonnet18.txt', 'r') as f:
        text = f.read()
    return text

@pytest.mark.describe(' Indexer Function')
class TestIndexer:

    @pytest.mark.skip
    @pytest.mark.it('returns empty generator for empty string')
    def test_iterator(self):
        text = ''
        result = indexer(text)
        with pytest.raises(StopIteration):
            next(result)
        
    @pytest.mark.skip
    @pytest.mark.it('has leading index zero for nonempty input')
    def test_leading_zero(self):
        assert next(indexer(text1)) == 0
        assert next(indexer(text2)) == 0
        assert next(indexer(text3)) == 0

    @pytest.mark.skip
    @pytest.mark.it('correctly indexes single-line text')
    def test_single_line(self):
        res1 = indexer(text1)
        assert next(res1) == 0
        assert list(indexer(text2)) == [0, 6]
        assert list(indexer(text3)) == [0, 4, 9, 16, 24, 27, 32, 34, 40, 43]
        with pytest.raises(StopIteration):
            next(res1)

    @pytest.mark.skip
    @pytest.mark.it('does not index leading or repeated space')
    def test_leading_space(self):
        assert list(indexer(text5)) == [2, 11, 15, 23]

    @pytest.mark.skip
    @pytest.mark.it('deals correctly with newline characters')
    def test_new_line(self):
        assert list(indexer(text4)) == [0, 4]

    @pytest.mark.skip
    @pytest.mark.it('deals with multiline text read from a file')
    def test_file_text(self, file_data):
        indexed1 = indexer(file_data)
        list1 = list(indexed1)
        assert len(list1) == 114
        assert list1[0:4] == [0, 6, 8, 16]
        assert list1[33] == 173
    


@pytest.mark.describe('Cool Cat' )
class TestCoolCat:

    @pytest.mark.skip
    @pytest.mark.it('works on single character strings')
    def test_single_char(self):
        result = cool_cat('A', 'B', 'C')
        assert next(result) == 'A'
        assert next(result) == 'B'
        assert next(result) == 'C'
        with pytest.raises(StopIteration):
            next(result)

    @pytest.mark.skip
    @pytest.mark.it('works on single item lists')
    def test_single_item_list(self):
        result = cool_cat(['A'], ['B'], ['C'])
        assert next(result) == 'A'
        assert next(result) == 'B'
        assert next(result) == 'C'
        with pytest.raises(StopIteration):
            next(result)

    @pytest.mark.skip
    @pytest.mark.it('works on single item dictionaries')
    def test_single_item_dict(self):
        result = cool_cat({'A': 1}, {'B': 2}, {'C': 3})
        assert next(result) == ('A', 1)
        assert next(result) == ('B', 2)
        assert next(result) == ('C', 3)
        with pytest.raises(StopIteration):
            next(result)

    @pytest.mark.skip
    @pytest.mark.it('works on multi-character strings')
    def test_multi_char(self):
        result = list(cool_cat('ABC', 'DEF', 'HIJ'))
        assert result == ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J']

    @pytest.mark.skip
    @pytest.mark.it('works on multi-item lists')
    def test_multi_item_list(self):
        result = list(cool_cat(['A', 'B', 'C'], ['D', 'E'], ['F', 'G', 'H']))
        assert result == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    @pytest.mark.skip
    @pytest.mark.it('works on multi item dictionaries')
    def test_multi_item_dict(self):
        result = cool_cat({'A': 1, 'B': 2, 'C': 3}, {'x': 4}, {'y': 96, 'z': 47}, {'P': 456})
        expected = {'A': 1, 'B': 2, 'C': 3, 'x': 4, 'y': 96, 'z': 47, 'P': 456}
        expected_iter = iter(expected.items())
        for i in expected_iter:
            curr = next(result)
            assert curr == i
