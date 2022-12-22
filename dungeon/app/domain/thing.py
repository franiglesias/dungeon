from dungeon.app.domain.player.energy import EnergyUnit


class ThingName:
    def __init__(self, name):
        if len(name) == 0:
            raise ValueError("Things must have name")
        self._name = name

    def to_s(self):
        return self._name


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

    def apply_on(self, user):
        user.increase_energy(EnergyUnit(10))

    @classmethod
    def from_raw(cls, name):
        thing_name = ThingName(name)
        thing_id = ThingId.from_name(thing_name)
        return cls(thing_name, thing_id)
