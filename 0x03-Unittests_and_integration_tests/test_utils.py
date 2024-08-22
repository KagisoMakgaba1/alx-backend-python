#!/usr/bin/env python3

"""This module contains unit tests for the utils module."""i

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function in the utils module."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """This class test the access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),  # Test with an empty dictionary
        ({"a": 1}, ("a", "b"))  # Test with a missing key in the nested path
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises a KeyError for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        # Ensure the exception message is as expected
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function in the utils module."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected result."""
        # Patch 'requests.get' to return a mock object
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator in the utils module."""

    class TestClass:
        """A test class to demonstrate the use of the memoize decorator."""

        def a_method(self):
            """A method that returns a constant value."""
            return 42

        @memoize
        def a_property(self):
            """A property that calls a_method."""
            return self.a_method()

    def test_memoize(self):
        """Test that the memoize decorator caches the result of a_property."""
        # Create an instance of the test class
        test_instance = self.TestClass()

        # Patch the a_method to observe its behavior
        with patch.object(test_instance, 'a_method',
                          return_value=42) as mock_method:
            # Call the a_property twice
            result_first_call = test_instance.a_property
            result_second_call = test_instance.a_property

            # Check that the correct result is returned both times
            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)

            # Check that a_method was only called once
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
