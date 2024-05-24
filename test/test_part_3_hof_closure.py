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
    @pytest.mark.it('function with no args invokes with correct password')
    def test_no_args(self):

        @secure_func('password')
        def func_no_args():
            return 'Function ran successfully!'

        result = func_no_args('password')
        assert result == 'Function ran successfully!'

    @pytest.mark.skip
    @pytest.mark.it('function with no args errors on incorrect password')
    def test_no_args_bad_pwd(self):

        @secure_func('password')
        def func_no_args():
            return 'Function ran successfully!'

        result = func_no_args('eggy_bread')

        assert result == 'Sorry, your password is incorrect!'

    @pytest.mark.skip
    @pytest.mark.it('function with args invokes with correct password')
    def test_args(self):

        @secure_func('P4s5w0rd!!!')
        def func_with_args(*args):
            return list(args)

        result = func_with_args('P4s5w0rd!!!', 1, 2, 3)

        assert result == [1, 2, 3]

    @pytest.mark.skip
    @pytest.mark.it('function with args errors on incorrect password')
    def test_args_bas_pwd(self):

        @secure_func('P4s5w0rd!!!')
        def func_with_args(*args):
            return list(args)

        result = func_with_args('Th15_1s_WR0ng', 1, 2, 3)

        assert result == 'Sorry, your password is incorrect!'

    @pytest.mark.skip
    @pytest.mark.it('function with args & kwargs invokes on correct password')
    def test_args_and_kwargs(self):

        @secure_func('P4s5w0rd!')
        def func_with_args_and_kwargs(*args, **kwargs):
            return (list(args), kwargs)

        result = func_with_args_and_kwargs('P4s5w0rd!', 1, 2, 3, invoked=True)

        assert result == ([1, 2, 3], {"invoked": True})

    @pytest.mark.skip
    @pytest.mark.it('function with args & kwargs errors on incorrect password')
    def test_args_and_kwargs_bad_pwd(self):

        @secure_func('P4s5w0rd!!!')
        def func_with_args_and_kwargs(*args, **kwargs):
            return (list(args), dict(kwargs))

        result = func_with_args_and_kwargs('3ggy_bRe4d', 1, 2, invoked=False)

        assert result == 'Sorry, your password is incorrect!'
