from dungeon.app.command.action_result import ActionResult
from dungeon.app.domain.player.energy import EnergyUnit, Energy
from dungeon.app.domain.player.player_events import PlayerDied, PlayerEnergyChanged, PlayerSentCommand, \
    PlayerGotDescription
from dungeon.app.events.subject import Subject


class Player:
    def __init__(self, starting_energy):
        self._energy = Energy(starting_energy)
        self._last_result = ActionResult.player_acted("I'm ready")
        self._subject = Subject()
        self._receiver = None
        self._holds = None

    @classmethod
    def awake(cls):
        return cls(EnergyUnit(100))

    @classmethod
    def awake_with_energy(cls, starting_energy):
        return cls(starting_energy)

    def awake_in(self, dungeon):
        dungeon.register(self)
        self._receiver = dungeon

    def do(self, command):
        self._execute_command(command, self._receiver)
        self._update_energy()

    def holds(self):
        return self._holds

    def _execute_command(self, command, receiver):
        self._last_result = command.do(receiver)
        self._notify_observers(PlayerSentCommand(command.name(), command.argument()))
        self._notify_observers(PlayerGotDescription(self._last_result.get('message')))

    def _update_energy(self):
        self._energy.decrease(self._last_action_cost())
        self._notify_observers(PlayerEnergyChanged(self._energy.current()))
        if self._energy.is_dead():
            self._notify_observers(PlayerDied())

    def _last_action_cost(self):
        return self._last_result.get("cost")

    def register(self, observer):
        self._subject.register(observer)

    def _notify_observers(self, event):
        self._subject.notify_observers(event)

    def notify(self, event):
        if "player_got_thing" == event.name():
            self._holds = event.thing()
