#!/usr/bin/env python3
""" Unit test for utils.access_nested_map """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """this class inherits from unittest.Testcase"""

    @parameterized.expand([
        {"a": 1}, ("a",)
        {"a": {"b": 2}}, ("a",)
        {"a": {"b": 2}}, ("a", "b")
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """this method tests the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), result)
