import pytest
import Main
import unittest

class testClass(unittest.TestCase):
    def test_markdownify(self):
        assert Main.MDhandler.markupify('<strong>Hearthstone 11/29/16</strong>') == '**Hearthstone 11/29/16**\r\n' or '**Hearthstone 11/29/16**\n'

    def test_bytefix(self):
        assert Main.MDhandler.fix(b'<p><strong>Hearthstone Update 11/29/16</strong></p>') == '<p><strong>Hearthstone Update 11/29/16</strong></p>'


