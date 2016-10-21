#!/usr/bin/env python

from application import app

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

    def test_404(self):
        tester = app.test_client(self)
        response = tester.get('/test')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
