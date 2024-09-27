from src.part_1_human_resources import make_name_tags, create_poll
from data.poll_data import nc_fruit_bowl
import pytest
from copy import deepcopy

@pytest.fixture
def guests():
    return [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
        },
        {
            'title': 'Mr',
            'forename': 'Kermit',
            'surname': 'The Frog',
            'age': 35,
            'company': 'Jim Henson Studios',
        }
    ]   

@pytest.fixture
def updated_guests():
    return [
        {
            'title': 'Mr',
            'forename': 'Sam',
            'surname': 'Caine',
            'age': 30,
            'company': 'Northcoders',
            'name_tag': 'Mr Sam Caine, Northcoders',
        },
        {
            'title': 'Mr',
            'forename': 'Kermit',
            'surname': 'The Frog',
            'age': 35,
            'company': 'Jim Henson Studios',
            'name_tag': 'Mr Kermit The Frog, Jim Henson Studios'
        }
    ]

class TestMakeNameTags:
    def test_returns_an_empty_list_when_given_an_empty_list(self):
        assert make_name_tags([]) == []

    def test_returned_list_is_a_new_list(self):
        # Arrange
        test_input = []
        # Act
        result = make_name_tags(test_input)
        # Assert
        assert result is not test_input

    def test_adds_formatted_name_tag_to_guest_dictionaries(self, guests, updated_guests):
        # Arrange
        test_input = guests
        # Act
        result = make_name_tags(test_input)
        # Assert
        assert result == updated_guests

    def test_original_list_is_unchanged(self, guests):
        # Arrange 
        test_input = guests
        copy_test_input = deepcopy(guests)
        # Act
        make_name_tags(test_input)
        # Assert
        assert test_input == copy_test_input


class TestCreatePoll():
    def test_returns_empty_dict_when_given_empty_list(self):
        assert create_poll([]) == {}

    def test_calculates_results_for_list_of_same_votes(self):
        # Arrange
        test_input = ["dog", "dog", "dog"]
        expected = {"dog": 3}
        # Act
        result = create_poll(test_input)
        # Assert
        assert result == expected

    def test_calculates_results_for_mixed_votes(self):
        # Arrange
        test_input = ["cake", "biscuit", "biscuit"]
        expected = {"cake": 1, "biscuit": 2}
        # Act
        result = create_poll(test_input)
        # Assert
        assert result == expected

    def test_handles_large_list_of_mixed_votes(self):
        # Arrange
        test_input = nc_fruit_bowl
        expected = {
            'apple': 276,
            'pear': 223,
            'banana': 263,
            'orange': 238,
            'lonesome plum': 1
        }
        # Act
        result = create_poll(test_input)
        # Assert
        assert result == expected

    def test_input_is_unchanged(self):
        # Arrange
        test_input = nc_fruit_bowl
        test_copy_input = deepcopy(nc_fruit_bowl)
        # Act
        create_poll(test_input)
        # Assert
        assert test_input == test_copy_input