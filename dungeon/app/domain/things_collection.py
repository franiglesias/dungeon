from dungeon.app.domain.thing import ThingId


class ThingsCollection:
    def __init__(self):
        self._things = dict()

    def store(self, a_thing):
        self._things[a_thing.id()] = a_thing

    def retrieve(self, thing_name):
        thing_id = ThingId.normalized(thing_name)
        if thing_id in self._things.keys():
            return self._things.pop(thing_id)
        return None

    def inventory(self, prefix, item_format, item_join, empty):
        if len(self._things) > 0:
            return prefix + self._item_listing(item_format, item_join)
        else:
            return empty

    def count(self):
        return len(self._things)

    def _item_listing(self, item_format: str, join_string: str) -> str:
        content = []
        for key, item in self._things.items():
            content.append(item_format.format(item.name().to_s()))
        return join_string.join(content)
