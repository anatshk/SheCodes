from unittest import TestCase
from TestDebugPresentation.testing_debugging_presentation import return_last_name


class TestReturnLastName(TestCase):
    def test_sanity(self):
        expected = 'Jackson'
        actual = return_last_name('Michael Jackson')
        self.assertEqual(actual, expected)

    def test_no_last_name(self):
        expected = 'No last name'
        actual = return_last_name('Prince')
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        with self.assertRaisesRegex(AssertionError, 'Empty String'):
            return_last_name('')

    def test_numbers_in_name(self):
        expected = 'King'
        actual = return_last_name('Henry King 8')
        self.assertEqual(actual, expected)

        actual = return_last_name('Henry King VIII')
        self.assertEqual(actual, expected)

    def setUp(self):
        super(TestReturnLastName, self).setUp()

    def tearDown(self):
        super(TestReturnLastName, self).tearDown()