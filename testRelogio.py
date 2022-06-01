import unittest
from Localtime import timezones_disponiveis
from AD2_2022_1 import update_zone,update_clock
class TestRelogio(unittest.TestCase):
    def test_handle_value(self):
        self.assert_(timezones_disponiveis().test_handle_value())
        self.assert_(update_zone().test_handle_value())
        self.assert_(update_clock().test_handle_value())
    if __name__ == '__name':
        unittest.main()