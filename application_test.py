#!/usr/bin/env python

from application import app, get_sorted_search_results, get_latest_commit

import unittest


class ApplicationTestCases(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_navigator(self):
        tester = app.test_client(self)
        response = tester.get('/navigator?search_term=arrow')
        self.assertEqual(response.status_code, 200)

    def test_get_sorted_search_results(self):
        json_obj = get_sorted_search_results("arrow")
        self.assertIsNotNone(json_obj)
        self.assertEqual(json_obj.__len__(), 5)

    def test_get_latest_commit(self):
        json_obj = get_latest_commit("abdullahhamid", "github-navigator")
        self.assertIsNotNone(json_obj)
        self.assertGreater(json_obj.__len__(), 1)

    def test_404(self):
        tester = app.test_client(self)
        response = tester.get('/test')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
