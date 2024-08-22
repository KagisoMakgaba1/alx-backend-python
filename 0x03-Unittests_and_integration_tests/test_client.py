#!/usr/bin/env python3

"""Unit tests for the GithubOrgClient class in the client module."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
import requests
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"name": "Google", "repos_url":
         "https://api.github.com/orgs/google/repos"}),
        ("abc", {"name": "ABC", "repos_url":
         "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json', return_value={"name":
           "Google", "repos_url": "https://api.github.com/orgs/google/repos"})
    def test_org(self, org_name, expected, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Create an instance of GithubOrgClient with the given org_name
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Ensure get_json was called once with the correct URL
        mock_get_json.assert_called_once_with
        (f"https://api.github.com/orgs/{org_name}")

        # Assert that the result matches the expected value
        self.assertEqual(result, expected)

        @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test the GithubOrgClient._public_repos_url."""
        # Define the mocked org payload
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/google/repos"}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the _public_repos_url method
        result = client._public_repos_url

        # Assert that the result matches the expected value
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    def test_public_repos(self, mock_get_json):
        """Test the GithubOrgClient.public_repos."""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=property) as mock_url:
            # Define the mocked _public_repos_url value
            mock_url.return_value = "https://api.github.com/orgs/google/repos"

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")

            # Call the public_repos method
            result = client.public_repos

            # Assert that the result matches the expected value
            self.assertEqual(result, ["repo1", "repo2"])

            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with
            ("https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the GithubOrgClient.has_license."""
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Mock the repos attribute to return the test repo
        with patch.object(client, 'repos', new_callable=property)
        as mock_repos:
            mock_repos.return_value = [repo]

            # Call the has_license method
            result = client.has_license(license_key)

            # Assert that the result matches the expected value
            self.assertEqual(result, expected)

            # Ensure the repos property was accessed once
            mock_repos.assert_called_once()


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the patcher and mock responses for requests.get."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Set up the side effects for different URLs
        def side_effect(url, *args, **kwargs):
            if url.endswith("/repos"):
                return MockResponse(cls.repos_payload)
            else:
                return MockResponse(cls.org_payload)

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the GithubOrgClient.public_repos method integration."""
        client = GithubOrgClient("google")
        result = client.public_repos
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the GithubOrgClient.public_repos method."""
        client = GithubOrgClient("google")
        result = client.public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)


class MockResponse:
    """Mock class for requests.Response."""
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


if __name__ == '__main__':
    unittest.main()
