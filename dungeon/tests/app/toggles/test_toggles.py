import unittest

from dungeon.app.toggles.toggles import Toggles


class TogglesTestCase(unittest.TestCase):
    def test_can_activate_toggle(self):
        toggles = Toggles()
        toggles.activate('some toggle')

        self.assertTrue(toggles.is_active('some toggle'))

    def test_can_deactivate_toggle(self):
        toggles = Toggles()
        toggles.activate('another toggle')
        toggles.deactivate('another toggle')

        self.assertFalse(toggles.is_active('another toggle'))

    def test_undefined_toggle_is_deactivated(self):
        toggles = Toggles()

        self.assertFalse(toggles.is_active('undefined toggle'))


if __name__ == '__main__':
    unittest.main()
