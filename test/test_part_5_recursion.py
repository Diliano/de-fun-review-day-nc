from src.part_5_recursion import flatten, deep_entries


class TestFlatten:
    def test_returns_empty_list_when_given_empty_list(self):
        assert flatten([]) == []

    def test_returns_given_list_if_unnested(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_flattens_list_containing_one_nested_list_with_default_depth_1(self):
        assert flatten([1, 2, [3, 4]]) == [1, 2, 3, 4]

    def test_flattens_list_containing_multiple_nested_lists_with_default_depth_1(self):
        # Arrange
        test_input = [1, 2, [3, [4, [5, 6]]]]
        expected = [1, 2, 3, [4, [5, 6]]]
        # Act
        result = flatten(test_input)
        # Assert
        assert result == expected

    def test_flattens_list_containing_multiple_nested_lists_with_given_depth(self):
        # Arrange
        test_input = [1, 2, [3, [4, [5, 6]]]]
        test_depth = 2
        expected = [1, 2, 3, 4, [5, 6]]
        # Act
        result = flatten(test_input, test_depth)
        # Assert
        assert result == expected

        # Arrange
        test_input = [1, 2, [3, [4, [5, 6]]]]
        test_depth = 3
        expected = [1, 2, 3, 4, 5, 6]
        # Act
        result = flatten(test_input, test_depth)
        # Assert
        assert result == expected

        # Arrange
        test_input = [1, 2, [3, [4, [5, 6]]]]
        test_depth = 25
        expected = [1, 2, 3, 4, 5, 6]
        # Act
        result = flatten(test_input, test_depth)
        # Assert
        assert result == expected

class TestDeepEntries:
    def test_returns_empty_tuple_when_given_empty_dict(self):
        assert deep_entries({}) == ()

    def test_returns_key_value_tuple_when_given_single_entry_dict(self):
        assert deep_entries({"name": "Sam"}) == (("name", "Sam"),)

    def test_returns_key_value_tuples_when_given_two_entries_dict(self):
        # Arrange
        test_input = {"name": "Sam", "fave_book": "50 Shades of Python"}
        expected = (("name", "Sam"), ("fave_book", "50 Shades of Python"))
        # Act
        result = deep_entries(test_input)
        # Act
        assert result == expected

    def test_handles_nested_dictionaries(self):
        # Arrange
        test_input = {"name": "Sam", "pets": {"name": "fido"}}
        expected = (("name", "Sam"), ("pets", (("name", "fido"),)))
        # Act
        result = deep_entries(test_input)
        # Assert
        assert result == expected

        # Arrange
        test_input = {
            "name": "Sam",
            "pets": {"name": "Fido"},
            "fave_book": {"title": "50 Shades of Python", "author": {"first_name": "Cody", "last_name": "Smutt"}}
        }
        expected = (
            ("name", "Sam"),
            ("pets", (("name", "Fido"),)),
            ("fave_book", (("title", "50 Shades of Python"), ("author", (("first_name", "Cody"), ("last_name", "Smutt")))))
        )
        # Act
        result = deep_entries(test_input)
        # Assert
        assert result == expected