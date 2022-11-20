from dungeon.command.action_result import ActionResult
from dungeon.dir import Dir
from dungeon.dungeon import DungeonBuilder
from dungeon.game import Game
from dungeon.wall import Exit


class Application:
    def __init__(self, obtain_user_command, show_output, dungeon_name='game'):
        self._obtain_user_command = obtain_user_command
        self._show_output = show_output
        self._dungeon_name = dungeon_name

    def run(self):
        self._show_output.put("Welcome to the Dungeon")
        dungeon = self._build_dungeon()
        game = Game()
        game.start(dungeon)
        action_result = ActionResult.player_acted("")
        while not action_result.is_finished():
            command = self._obtain_user_command.command()
            action_result = game.do_command(command)
            self._show_output.put(str(command))
            self._show_output.put(action_result.message())

    def _build_dungeon(self):
        factory = DungeonFactory()
        return factory.make(self._dungeon_name)


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
        builder.connect('2', Dir.E, '7')
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
        return builder.build()
