import pytest
from src.part_3_hof_closure import generate_multiples, capitaliser, secure_func
from types import FunctionType


class TestGenerateMultiples:
    @pytest.mark.skip
    def test_returns_function(self):
        assert type(generate_multiples(4)) is FunctionType

    @pytest.mark.skip
    def test_new_func_returns_empty_list_when_passed_0(self):
        mults_5 = generate_multiples(5)
        assert mults_5(0) == []

    @pytest.mark.skip
    def test_new_func_returns_single_item_list_when_passed_0(self):
        mults_5 = generate_multiples(5)
        assert mults_5(1) == [5]

    @pytest.mark.skip
    def test_new_func_returns_correct_number_of_itmes_in_list(self):
        mults_5 = generate_multiples(5)
        assert mults_5(3) == [5, 10, 15]
        assert mults_5(5) == [5, 10, 15, 20, 25]
        assert mults_5(7) == [5, 10, 15, 20, 25, 30, 35]
        mults_7 = generate_multiples(7)
        assert mults_7(6) == [7, 14, 21, 28, 35, 42]


class TestCapitaliser:
    @pytest.mark.skip
    def test_returns_function(self):
        def example_func():
            pass

        result = capitaliser(example_func)

        assert isinstance(result, FunctionType)

    @pytest.mark.skip
    def test_decorated_func_returns_capitalised_string_result(self):
        def example_func():
            return "hello world"

        decorated_func = capitaliser(example_func)
        result = decorated_func()

        assert result == "HELLO WORLD"

    @pytest.mark.skip
    def test_decorated_func_returns_int_result_unchanged(self):
        def example_func():
            return 14

        decorated_func = capitaliser(example_func)
        result = decorated_func()

        assert result == 14

    @pytest.mark.skip
    def test_decorated_func_returns_bool_result_unchanged(self):
        def example_func():
            return False

        decorated_func = capitaliser(example_func)
        result = decorated_func()

        assert result is False

    @pytest.mark.skip
    def test_function_acts_as_decorator(self):
        @capitaliser
        def example_func():
            return "hey hey it's decorating time"

        result = example_func()
        assert result == "HEY HEY IT'S DECORATING TIME"


class TestSecureFunction:
    @pytest.mark.skip
    def test_func_with_no_args_invoked_with_correct_password(self):
        @secure_func("password")
        def func_no_args():
            return "Function ran successfully!"

        result = func_no_args("password")
        assert result == "Function ran successfully!"

    @pytest.mark.skip
    def test_func_with_no_args_errors_on_bad_password(self):
        @secure_func("password")
        def func_no_args():
            return "Function ran successfully!"

        result = func_no_args("eggy_bread")

        assert result == "Sorry, your password is incorrect!"

    @pytest.mark.skip
    def test_func_with_args_invoked_with_correct_password(self):
        @secure_func("P4s5w0rd!!!")
        def func_with_args(*args):
            return list(args)

        result = func_with_args("P4s5w0rd!!!", 1, 2, 3)

        assert result == [1, 2, 3]

    @pytest.mark.skip
    def test_func_with_args_errors_on_bad_password(self):
        @secure_func("P4s5w0rd!!!")
        def func_with_args(*args):
            return list(args)

        result = func_with_args("Th15_1s_WR0ng", 1, 2, 3)

        assert result == "Sorry, your password is incorrect!"

    @pytest.mark.skip
    def test_args_and_kwargs_invoked_with_correct_password(self):
        @secure_func("P4s5w0rd!")
        def func_with_args_and_kwargs(*args, **kwargs):
            return (list(args), kwargs)

        result = func_with_args_and_kwargs("P4s5w0rd!", 1, 2, 3, invoked=True)

        assert result == ([1, 2, 3], {"invoked": True})

    @pytest.mark.skip
    def test_func_with_args_and_kwargs_errors_on_bad_password(self):
        @secure_func("P4s5w0rd!!!")
        def func_with_args_and_kwargs(*args, **kwargs):
            return (list(args), dict(kwargs))

        result = func_with_args_and_kwargs("3ggy_bRe4d", 1, 2, invoked=False)

        assert result == "Sorry, your password is incorrect!"
