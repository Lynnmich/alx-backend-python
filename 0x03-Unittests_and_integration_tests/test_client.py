#!/usr/bin/env python3
"""A class that implements the test_org method"""
import unittest
from unittest import mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient Class"""
    @patch("client.get_json")
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, info, mock):
        """New test"""
        endpoint = 'https://api.github.com/orgs/{}'.format(info)
        spec = GithubOrgClient(info)
        spec.org()
        mock.assert_called_once_with(endpoint)
