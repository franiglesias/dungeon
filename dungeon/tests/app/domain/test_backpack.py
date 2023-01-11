import unittest

from dungeon.app.domain.player.backpack import Backpack
from dungeon.app.domain.thing import Thing


class BackpackTestCase(unittest.TestCase):
    def test_allows_maximum_of_elements(self):
        backpack = Backpack()
        backpack.append(Thing.from_raw("1"))
        backpack.append(Thing.from_raw("2"))
        backpack.append(Thing.from_raw("3"))
        backpack.append(Thing.from_raw("4"))
        backpack.append(Thing.from_raw("5"))
        with self.assertRaises(IndexError):
            backpack.append(Thing.from_raw("6"))


if __name__ == '__main__':
    unittest.main()
