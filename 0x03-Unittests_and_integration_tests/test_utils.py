#!/usr/bin/env python3
""" Unit test for utils.access_nested_map """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """this class inherits from unittest.Testcase"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """this method tests the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """this method tests keyError and raises an exceeption"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """this class and implement the method that returns the expected result"""
    @parameterized.expand([
       ("http://example.com", {"payload": True}),
       ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """this method to test and returns the expected result"""
        class Mocke(Mock):
            """Mocke class that inherits from Mock"""
            def json(self):
                """Retruns payload"""
                return payload

        with patch("requests.get") as mock_req:
            mock_req.return_value = Mocke()
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """this class is implemented using the test_memoize method"""
    def test_memoize(self):
        """memoize test"""

        class TestClass:
            """Test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mocke:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocke.asset_called_once()
