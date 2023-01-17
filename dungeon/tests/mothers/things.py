from dungeon.app.domain.thing import Thing


class ThingMother:
    @staticmethod
    def with_name(name) -> Thing:
        return Thing.from_raw(name)

    @staticmethod
    def from_names(*names):
        result = []
        for name in names:
            result.append(Thing.from_raw(name))
        return result
