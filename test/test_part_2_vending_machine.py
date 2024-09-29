import pytest
from src.part_2_vending_machine import VendingMachine, InsufficientCreditError, OutOfStockError


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

    def test_add_stock_method_replaces_any_existing_stock(self, machine):
        # Arrange
        test_stock = {"name": "mars_bar", "price": 50, "quantity": 6}
        test_position = "A"
        replacement_stock = {"name": "snickers_bar", "price": 60, "quantity": 3}
        # Act & Assert
        machine.add_stock(test_stock, test_position)
        assert machine.stock == {
            "A": {"name": "mars_bar", "price": 50, "quantity": 6},
            "B": {},
            "C": {}
        }
        machine.add_stock(replacement_stock, test_position)
        assert machine.stock == {
            "A": {"name": "snickers_bar", "price": 60, "quantity": 3},
            "B": {},
            "C": {}
        }

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

    def test_purchase_item_method_raises_exception_if_insufficient_credits(self, machine):
        # Arrange
        test_stock = {"name": "mars_bar", "price": 50, "quantity": 6}
        test_position = "A"
        # Act
        machine.add_stock(test_stock, test_position)
        # Assert
        with pytest.raises(InsufficientCreditError) as excinfo:
            machine.purchase_item(test_position)
        assert str(excinfo.value) == "Insufficient credit!"

    def test_purchase_item_method_raises_exception_if_0_quantity_available(self, machine):
        # Arrange
        test_stock = {"name": "mars_bar", "price": 50, "quantity": 0}
        test_position = "A"
        # Act
        machine.add_credit(60)
        machine.add_stock(test_stock, test_position)
        # Assert
        with pytest.raises(OutOfStockError) as excinfo:
            machine.purchase_item(test_position)
        assert str(excinfo.value) == "Item out of stock"

    def test_purchase_item_updates_stock_quantity_with_successful_purchase(self, machine):
        # Arrange
        test_stock = {"name": "mars_bar", "price": 50, "quantity": 6}
        test_position = "A"
        # Act
        machine.add_stock(test_stock, test_position)
        machine.add_credit(60)
        machine.purchase_item(test_position)
        # Assert
        assert machine.stock == {
            "A": {"name": "mars_bar", "price": 50, "quantity": 5},
            "B": {},
            "C": {}
        }

    def test_purchase_item_updates_credit_with_successful_purchase(self, machine):
        # Arrange
        test_stock = {"name": "mars_bar", "price": 50, "quantity": 6}
        test_position = "A"
        # Act
        machine.add_stock(test_stock, test_position)
        machine.add_credit(60)
        machine.purchase_item(test_position)
        # Assert
        assert machine.credit == 10

    def test_purchase_item_returns_item_name_with_successful_purchase(self, machine):
        # Arrange
        test_stock = {"name": "mars_bar", "price": 50, "quantity": 6}
        test_position = "A"
        expected = "mars_bar"
        # Act
        machine.add_stock(test_stock, test_position)
        machine.add_credit(60)
        result = machine.purchase_item(test_position)
        # Assert
        assert result == expected

    def test_purchase_item_method_raises_exception_if_given_position_is_not_a_string(self, machine):
        test_position = 2
        with pytest.raises(TypeError) as excinfo:
            machine.purchase_item(test_position)
        assert str(excinfo.value) == "Position must be a string"

    def test_purchase_item_method_raises_exception_if_given_position_does_not_exist(self, machine):
        test_position = "D"
        with pytest.raises(ValueError) as excinfo:
            machine.purchase_item(test_position)
        assert str(excinfo.value) == "Position does not exist"