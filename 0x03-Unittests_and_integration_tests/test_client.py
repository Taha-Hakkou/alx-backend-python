#!/usr/bin/env python3
""" test_client.py """
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized, parameterized_class
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """  """

    @parameterized.expand([
        ['google', {'login': 'google'}],
        ['abc', {'login': 'abc'}]
    ])
    @patch('client.get_json')
    def test_org(self, org_name, response, get_json_mock):
        """  """
        get_json_mock.return_value = MagicMock(return_value=response)
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), response)
        get_json_mock.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')


    def test_public_repos_url(self):
        """  """
        with patch('GithubOrgClient.org') as mock:
            mock.return_value = {'payload': True}
            self.assertEqual(GithubOrgClient._public_repos_url, {'payload': True})

    """
    @patch('get_json', return_value={'payload': True})
    def test_public_repos(self):
        """  """
        with patch('GithubOrgClient._public_repos_url') as mock:
            mock.return_value = {'payload': False}
            assertEqual()
        assert_called_once()

    @parameterized.expand([
        [{"license": {"key": "my_license"}}, "my_license", True],
        [{"license": {"key": "other_license"}}, "my_license", False]
    ])
    def test_has_license(self, repo, license_key, result):
        """  """
        self.assertEqual(has_license(repo, license_key), result)


@parameterized_class
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """  """

    @classmethod
    def setUpClass(self):
        """"""
        get_patcher = patch('', side_effect=)
        get_patcher.start()

    @classmethod
    def tearDownClass(self):
        """ """
        get_patcher.stop()

    def test_public_repos(self):
        """  """
        # not understand"""
