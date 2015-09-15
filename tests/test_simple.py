import unittest

from Identicon import Identicon


class TestSimple(unittest.TestCase):
    
    def test_try(self):
        i = Identicon(background=(0,0,0,0))
        image = i.generate('fsdfsdfsdf')

        with open('identicon.png', 'wb') as out:
            image.save(out, 'PNG')

        image.show()

