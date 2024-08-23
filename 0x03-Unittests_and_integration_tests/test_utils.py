#!/usr/bin/env python3


"""This module contains unit tests for the utils module."""

import unittest
import unittest.mock

from parameterized import parameterized

import utils


class TestAccessNestedMap(unittest.TestCase):
    """This class tests the access_nested_map function."""

    @parameterized.expand(
        [
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a", "b"], 2),
            ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that the function returns the expected output."""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ["a"]),
            ({"a", 1}, ["a", "b"]),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that the function raises a KeyError for invalid keys."""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """This class tests the get_json function."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    def test_get_json(self, url, payload):
        """Test that the function returns the expected output."""
        with unittest.mock.patch("requests.get") as get:
            get.return_value.json.return_value = payload
            response = utils.get_json(url)
            get.assert_called_once_with(url)
            self.assertEqual(response, payload)


class TestMemoize(unittest.TestCase):
    """This class tests the memoize function."""

    def test_memoize(self):
        """Test that the function returns the expected output."""

        class TestClass:
            """A test class."""

            @staticmethod
            def a_method():
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with unittest.mock.patch.object(TestClass, "a_method") as method:
            instance = TestClass()
            method.return_value = 42

            result = instance.a_property
            self.assertEqual(result, 42)

            result = instance.a_property
            self.assertEqual(result, 42)

            method.assert_called_once()
