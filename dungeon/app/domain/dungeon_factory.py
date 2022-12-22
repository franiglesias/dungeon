from dungeon.app.domain.dir import Dir
from dungeon.app.domain.dungeon_builder import DungeonBuilder
from dungeon.app.domain.thing import Thing
from dungeon.app.domain.wall import Exit


class DungeonFactory:
    def __init__(self):
        pass

    def make(self, dungeon_name):
        if dungeon_name == 'test':
            return self._build_test()
        if dungeon_name == 'game':
            return self._build_dungeon()

    def _build_test(self):
        builder = DungeonBuilder()
        builder.add('start')
        builder.set('start', Dir.N, Exit())
        return builder.build()

    def _build_dungeon(self):
        builder = DungeonBuilder()
        for cell in range(23):
            builder.add(str(cell))
        builder.add('start')
        builder.add('exit')

        builder.connect('0', Dir.S, '5')
        builder.connect('1', Dir.E, '2')
        builder.connect('2', Dir.E, '3')
        builder.connect('2', Dir.S, '7')
        builder.connect('3', Dir.E, '4')
        builder.connect('4', Dir.S, '9')
        builder.connect('5', Dir.S, '10')
        builder.connect('6', Dir.S, '11')
        builder.connect('6', Dir.E, '7')
        builder.connect('8', Dir.E, '9')
        builder.connect('8', Dir.S, '13')
        builder.connect('9', Dir.S, 'exit')
        builder.connect('10', Dir.E, '11')
        builder.connect('11', Dir.E, '12')
        builder.connect('11', Dir.S, '15')
        builder.connect('13', Dir.S, '17')
        builder.connect('14', Dir.S, '19')
        builder.connect('15', Dir.S, 'start')
        builder.connect('16', Dir.E, '17')
        builder.connect('17', Dir.E, '18')
        builder.connect('19', Dir.E, 'start')
        builder.connect('start', Dir.E, '20')
        builder.connect('start', Dir.E, '20')
        builder.connect('21', Dir.E, '22')

        builder.set('exit', Dir.E, Exit())
        builder.put('10', Thing.from_raw("Food"))
        builder.put('17', Thing.from_raw("Sword"))
        builder.put('1', Thing.from_raw("Food"))
        return builder.build()
