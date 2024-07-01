#!/usr/bin/env python3
""" test_utils.py """
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from unittest.mock import patch, Mock
import requests
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """ access_nested_map testing unit """

    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
    def test_access_nested_map(self: Any, nested_map: Mapping,
                               path: Sequence, result: Any) -> None:
        """  """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        [{}, ("a",)],
        [{"a": 1}, ("a", "b")]
    ])
    def test_access_nested_map_exception(self: Any, nested_map: Mapping,
                                         path: Sequence) -> None:
        """  """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ get_json testing unit """
    
    @parameterized.expand([
        ["http://example.com", {"payload": True}],
        ["http://holberton.io", {"payload": False}]
    ])
    def test_get_json(self: Any, test_url: str, test_payload: Mapping) -> None:
        """  """
        attrs = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**attrs)) as get_mock:
            self.assertEqual(get_json(test_url), test_payload)
            get_mock.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ memoize testing unit """

    def test_memoize(self: Any) -> None:
        """  """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=lambda: 42) as cm:
            test_object = TestClass()
            self.assertEqual(test_object.a_property(), 42)
            self.assertEqual(test_object.a_property(), 42)
            cm.assert_called_once()
