class Backpack:
    def __init__(self):
        self._items = dict()

    def append(self, item):
        self._items[item.name().lower()] = item

    def content(self):
        content = []
        for key, item in self._items.items():
            content.append(item.name())

        return ", ".join(content)

    def get(self, thing_name):
        if thing_name.lower() in self._items.keys():
            return self._items.pop(thing_name.lower())
