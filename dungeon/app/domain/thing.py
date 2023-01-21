import random
import string

from dungeon.app.domain.player.energy import EnergyUnit


class ThingName:
    def __init__(self, name):
        if len(name) == 0:
            raise ValueError("Things must have name")
        self._name = name

    def to_s(self):
        return self._name


class ThingNullName(ThingName):
    def __init__(self):
        self._name = "nothing"


class ThingId:
    def __init__(self, id):
        if len(id) == 0:
            raise ValueError("Things must have identifier")
        self._id = id

    def __eq__(self, other):
        return self.to_s() == other.to_s()

    def __hash__(self):
        return hash(self._id)

    def to_s(self):
        return self._id

    @classmethod
    def normalized(cls, id):
        return cls(id.lower())

    @classmethod
    def from_name(cls, thing_name):
        return cls.normalized(thing_name.to_s())


class Thing:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def name(self):
        return self._name

    def id(self):
        return self._id

    def apply_on(self, some_object):
        pass

    @classmethod
    def from_raw(cls, name):
        thing_name = ThingName(name)
        thing_id = ThingId.from_name(thing_name)
        return cls(thing_name, thing_id)

    def is_named(self, name):
        return self.id() == ThingId.normalized(name)


class Food(Thing):
    @classmethod
    def from_raw(cls, name, energy=EnergyUnit(10)):
        thing_name = ThingName(name)
        thing_id = ThingId.from_name(thing_name)
        return cls(thing_name, thing_id, energy)

    def __init__(self, name, id, energy):
        super().__init__(name, id)
        self._energy = energy

    def apply_on(self, user):
        user.increase_energy(self._energy)


class ThingKey:
    def __init__(self, key):
        self._key = key

    def match(self, other):
        return self.key() == other.key()

    def key(self):
        return self._key


class Key(Thing):
    @classmethod
    def from_raw(cls, name, key):
        thing_name = ThingName(name)
        thing_id = ThingId.from_name(thing_name)
        think_key = ThingKey(key)
        return cls(thing_name, thing_id, think_key)

    def __init__(self, name, _id, key):
        super().__init__(name, _id)
        self._key = key

    def apply_on(self, door):
        door.unlock_with(self._key)
        return self


class ThingMother:
    @staticmethod
    def random():
        return Thing.from_raw(''.join(random.choice(string.ascii_letters)))

    @staticmethod
    def with_name(name) -> Thing:
        return Thing.from_raw(name)

    @staticmethod
    def from_names(*names):
        result = []
        for name in names:
            result.append(Thing.from_raw(name))
        return result
