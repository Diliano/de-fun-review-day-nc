import pytest
from src.part_2_vending_machine import VendingMachine


@pytest.fixture(scope="function")
def machine():
    return VendingMachine()


class TestVendingMachine:
    def test_initial_credit_set_to_0(self, machine):
        assert machine.credit == 0

    def test_initial_stock(self, machine):
        assert machine.stock["A"] == {}
        assert machine.stock["B"] == {}
        assert machine.stock["C"] == {}

    def test_add_credit_method_sets_credit_attribute(self, machine):
        machine.add_credit(75)
        assert machine.credit == 75
        new_machine = VendingMachine()
        new_machine.add_credit(62)
        assert new_machine.credit == 62

    def test_add_credit_increases_current_credit(self, machine):
        machine.add_credit(19)
        assert machine.credit == 19
        machine.add_credit(33)
        assert machine.credit == 52

    def test_credit_checker_returns_true_for_sufficient_credit(self, machine):
        machine.add_credit(36)
        assert machine.credit_checker(30) is True

    def test_credit_checker_returns_false_for_insufficient_credit(self, machine):
        machine.add_credit(36)
        assert machine.credit_checker(44) is False

    def test_add_stock_method_raises_exception_if_given_stock_is_not_a_dict(self, machine):
        with pytest.raises(TypeError) as excinfo:
            machine.add_stock("Mars bar", "A")
        assert str(excinfo.value) == "Stock must be a dictionary"

    def test_add_stock_method_raises_exception_if_given_position_is_not_a_string(self, machine):
        with pytest.raises(TypeError) as excinfo:
            machine.add_stock({}, 2)
        assert str(excinfo.value) == "Position must be a string"

    def test_add_stock_method_raises_exception_if_given_position_does_not_exist(self, machine):
        with pytest.raises(ValueError) as excinfo:
            machine.add_stock({}, "D")
        assert str(excinfo.value) == "Position does not exist"

    def test_add_stock_method_adds_given_stock_at_given_position(self, machine):
        # Arrange
        test_stock = {"name": "mars_bar", "price": 50, "quantity": 6}
        test_position = "A"
        # Act
        machine.add_stock(test_stock, test_position)
        # Assert
        assert machine.stock == {
            "A": {"name": "mars_bar", "price": 50, "quantity": 6},
            "B": {},
            "C": {}
        }
        
        """
        If stock already exists, given stock will replace it
        """
        # Arrange
        replacement_stock = {"name": "snickers_bar", "price": 60, "quantity": 3}
        # Act
        machine.add_stock(replacement_stock, test_position)
        # Assert
        assert machine.stock == {
            "A": {"name": "snickers_bar", "price": 60, "quantity": 3},
            "B": {},
            "C": {}
        }