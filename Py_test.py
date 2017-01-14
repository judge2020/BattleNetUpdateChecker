import pytest
import unittest
import Main
class Test_class(unittest.TestCase):
    def Test_fixByte(self):
        assert Main.MDhandler.fix('Hearthstone Update \xe2\x80\x93 11/29/16') == 'Hearthstone Update - 11/29/16'
