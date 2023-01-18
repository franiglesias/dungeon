from dungeon.app.domain.dir import Dir
from dungeon.app.domain.dungeon import Dungeon
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.thing import Key, Food, ThingKey
from dungeon.app.domain.wall import Locked, Exit


class DungeonMother:
    @staticmethod
    def with_objects(*things) -> Dungeon:
        builder = DungeonBuilder()
        builder.add('start')
        for thing in things:
            builder.put('start', thing)
        return builder.build()

    @staticmethod
    def with_locked_exit(direction=Dir.N) -> Dungeon:
        builder = DungeonBuilder()
        builder.add('start')
        builder.set('start', direction, Locked(Exit(), ThingKey("super-secret")))
        builder.put('start', Key.from_raw("key", "super-secret"))
        builder.put('start', Food.from_raw("food"))
        return builder.build()
