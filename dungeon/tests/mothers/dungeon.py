from dungeon.app.domain.dungeon import Dungeon
from dungeon.app.domain.dungeon_builder import DungeonBuilder


class DungeonMother:
    @staticmethod
    def with_objects(*things) -> Dungeon:
        builder = DungeonBuilder()
        builder.add('start')
        for thing in things:
            builder.put('start', thing)
        return builder.build()
