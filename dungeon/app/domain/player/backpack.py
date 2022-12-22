from dungeon.app.domain.thing import ThingId


class Backpack:
    def __init__(self):
        self._items = dict()

    def append(self, item):
        self._items[item.id().to_s()] = item

    def content(self):
        content = []
        for key, item in self._items.items():
            content.append(item.name().to_s())

        return ", ".join(content)

    def get(self, thing_name):
        thing_id = ThingId.normalized(thing_name)
        if thing_id.to_s() in self._items.keys():
            return self._items.pop(thing_id.to_s())
