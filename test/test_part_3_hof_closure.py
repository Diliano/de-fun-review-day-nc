import pytest
from src.part_3_hof_closure import generate_multiples
from types import FunctionType


@pytest.mark.describe('Generate Multiples')
class TestGenerateMultiples:
    
    @pytest.mark.skip
    @pytest.mark.it('returns function')
    def test_returns_function(self):
        assert type(generate_multiples(4)) == FunctionType

    @pytest.mark.skip
    @pytest.mark.it('new function returns empty list when passed 0')
    def test_returns_empty(self):
        mults_5 = generate_multiples(5)
        assert mults_5(0) == []

    @pytest.mark.skip
    @pytest.mark.it('new function returns single-item list when passed 1')
    def test_returns_single(self):
        mults_5 = generate_multiples(5)
        assert mults_5(1) == [5]

    @pytest.mark.skip
    @pytest.mark.it('new function returns correct number of items')
    def test_returns_many(self):
        mults_5 = generate_multiples(5)
        assert mults_5(3) == [5, 10, 15]
        assert mults_5(5) == [5, 10, 15, 20, 25]
        assert mults_5(7) == [5, 10, 15, 20, 25, 30, 35]
        mults_7 = generate_multiples(7)
        assert mults_7(6) == [7, 14, 21, 28, 35, 42]