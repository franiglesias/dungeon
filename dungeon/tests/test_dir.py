from unittest import TestCase

from dungeon.app.domain.dir import Dir


class TestDir(TestCase):
    def test_can_tell_opposite(self):
        self.assertEqual(Dir.S, Dir.N.opposite())
        self.assertEqual(Dir.N, Dir.S.opposite())
        self.assertEqual(Dir.W, Dir.E.opposite())
        self.assertEqual(Dir.E, Dir.W.opposite())
