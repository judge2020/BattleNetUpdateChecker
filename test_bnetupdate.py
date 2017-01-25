import pytest
import Main
import unittest

class testClass(unittest.TestCase):
    def test_markdownify(self):
        assert Main.MDhandler.markupify('<p><strong>Hearthstone Update \u2013 11/29/16</strong></p>') == '**Hearthstone Update \u2013 11/29/16**\r\n'

    def test_bytefix(self):
        assert Main.MDhandler.fix(b'<p><strong>Hearthstone Update \xe2\x80\x93 11/29/16</strong></p>') == '<p><strong>Hearthstone Update \u2013 11/29/16</strong></p>'
