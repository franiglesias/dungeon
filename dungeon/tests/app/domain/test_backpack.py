import unittest

from dungeon.app.domain.player.backpack import BackpackMother
from dungeon.app.domain.thing import ThingMother


class BackpackTestCase(unittest.TestCase):
    def test_we_cannot_keep_more_things_in_a_full_backpack(self):
        backpack = BackpackMother.full()
        with self.assertRaises(IndexError):
            backpack.keep(ThingMother.random())


if __name__ == '__main__':
    unittest.main()
