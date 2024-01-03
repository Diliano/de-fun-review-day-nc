from src.part_4_iterators import indexer
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
    