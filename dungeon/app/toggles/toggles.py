class Toggles:
    def __init__(self):
        self._toggles = dict()

    def activate(self, toggle_name):
        self._toggles[toggle_name] = True

    def is_active(self, toggle_name):
        if toggle_name not in self._toggles.keys():
            return False
        return self._toggles[toggle_name]

    def deactivate(self, toggle_name):
        self._toggles[toggle_name] = False
