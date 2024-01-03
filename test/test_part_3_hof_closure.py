import pytest
from src.part_3_hof_closure import generate_multiples, secure_func
from types import FunctionType
from unittest.mock import patch

@pytest.fixture(scope='function')
def func_no_args():
    
    @secure_func('secretpassw0rd')
    def secret_word():
        return 'Wibble'
    
    return secret_word

@pytest.fixture(scope='function')
def func_with_args():
    
    @secure_func('secretpassw0rd')
    def upperify(word, exclaim=True):
        return word.upper() + '!' if exclaim else word.upper()
    
    return upperify
    

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


@pytest.mark.describe('Secure Function')
class TestSecureFunction:

    @pytest.mark.skip
    @pytest.mark.it('requires password prompt for decorated function')
    def test_new_function(self, func_no_args):
        with patch('builtins.input', return_value='secretpassw0rd') as p:
            func_no_args()
            p.assert_called_once()

    @pytest.mark.skip
    @pytest.mark.it('function with no args executes correctly with password')
    def test_no_args(self, func_no_args):
        with patch('builtins.input', return_value='secretpassw0rd'):
            result = func_no_args()
            assert result == 'Wibble'

    @pytest.mark.skip
    @pytest.mark.it('function with no args issues error on incorrect password')
    def test_no_args_bad_pwd(self, func_no_args):
        with patch('builtins.input', return_value='wrongpassw0rd'):
            result = func_no_args()
            assert result == 'Sorry your password is incorrect!'

    @pytest.mark.skip
    @pytest.mark.it('function with args executes correctly with password')
    def test_args(self, func_with_args):
        with patch('builtins.input', return_value='secretpassw0rd'):
            result1 = func_with_args('wibble')
            assert result1 == 'WIBBLE!'
            result2 = func_with_args('wobble', exclaim=False)
            assert result2 == 'WOBBLE'

    @pytest.mark.skip
    @pytest.mark.it('function with args issues error on incorrect password')
    def test_args_bas_pwd(self, func_with_args):
        with patch('builtins.input', return_value='wrongpassw0rd'):
            result = func_with_args('wibble', exclaim=False)
            assert result == 'Sorry your password is incorrect!'
