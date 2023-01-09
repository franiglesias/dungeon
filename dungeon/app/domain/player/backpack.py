from dungeon.app.domain.things_collection import ThingsCollection


class Backpack:
    def __init__(self):
        self._things = dict()
        self._collection = ThingsCollection()

    def append(self, a_thing):
        self._store_thing(a_thing)

    def _store_thing(self, a_thing):
        self._collection.store(a_thing)

    def inventory(self):
        return self._things_inventory(
            prefix="",
            item_format="{}",
            item_join=", ",
            empty=""
        )

    def _things_inventory(self, prefix, item_format, item_join, empty):
        return self._collection.inventory(prefix, item_format, item_join, empty)

    def get(self, thing_name):
        return self._retrieve_thing(thing_name)

    def _retrieve_thing(self, thing_name):
        return self._collection.retrieve(thing_name)
