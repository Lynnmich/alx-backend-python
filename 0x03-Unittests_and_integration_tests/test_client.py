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

    @parameterized.expand([
        ("random_url", {"repos_url": "http://a_url.com"})
    ])
    def test_public_repos_url(self, org_name, result):
        """Method for unittest"""
        with patch("client.GithubOrgClient.org",
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(org_name).public_repos_url
            self.assertEqual(response, result.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, mocked_method):
        """unittest public repos"""
        payload = [{"org_name": "Google"}, {"org_name": "GitHub"}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:

            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "GitHub"])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """test has license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
