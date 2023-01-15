from dungeon.app.domain.player.container import Container
from dungeon.app.domain.thing import Thing
from dungeon.app.domain.things_collection import ThingsCollection


class Backpack(Container):
    def __init__(self, capacity=5):
        self._capacity = capacity
        self._collection = ThingsCollection()

    def exchange(self, to_keep: Thing, thing_name) -> Thing:
        try:
            thing = self.get_safe(thing_name)
            self._store_thing(to_keep)
            return thing
        except IndexError:
            raise

    def keep(self, a_thing):
        if self._is_full():
            raise IndexError
        self._store_thing(a_thing)

    def _is_full(self):
        return self._collection.count() >= self._max_capacity()

    def _max_capacity(self):
        return self._capacity

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

    def get_safe(self, thing_name):
        thing = self.get(thing_name)
        if thing is None:
            raise IndexError
        return thing

    def _retrieve_thing(self, thing_name):
        return self._collection.retrieve(thing_name)
