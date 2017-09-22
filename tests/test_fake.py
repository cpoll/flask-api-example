from unittest import TestCase


class FakeTest(TestCase):
    def test_true(self):
        self.assertEqual(True, True)
