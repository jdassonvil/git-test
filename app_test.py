import unittest
from app import myfunction

class AppTest(unittest.TestCase):

    def should_return1_when_arg_is_a(self):
        assert myfunction("a") == 1

    def should_return2_when_arg_is_not_a(self):
        assert myfunction("b") == 2

