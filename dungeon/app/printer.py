from dungeon.app.domain.player.player_events import PlayerEnergyChanged, PlayerGotDescription, PlayerMoved, \
    PlayerSentCommand, PlayerExited, PlayerGotThing, ActionNotCompleted, PlayerHitWall, PlayerAwake, BackpackChanged, \
    DoorWasLocked, ThingInHandChanged, DoorWasUnlocked, PlayerFinishedGame
from dungeon.app.events.subject import Observer
from dungeon.app.scene import Scene


class Printer(Observer):
    def __init__(self, show_output):
        self.show_output = show_output
        self._command = ""
        self._description = ""
        self._energy = ""
        self._title = ""

    def notify(self, event):
        if event.of_type(PlayerEnergyChanged):
            self._energy = str(event.energy().value())
        elif event.of_type(PlayerGotDescription):
            self._description = event.description()
        elif event.of_type(PlayerMoved):
            self._title = event.room()
            self._description = "You moved to room '{dest}'".format(dest=event.room())
        elif event.of_type(PlayerSentCommand):
            self._command = "{} {}".format(event.command(), event.argument())
        elif event.of_type(PlayerExited):
            self._description = "Congrats. You're out"
        elif event.of_type(PlayerGotThing):
            self._description = "You've got {}".format(event.thing().name())
        elif event.of_type(ActionNotCompleted):
            self._description = "Action was not finished because {}".format(event.reason())
        elif event.of_type(PlayerHitWall):
            self._description = "You hit a wall. There is no door."
        elif event.of_type(PlayerAwake):
            self._title = "Welcome to the Dungeon"
            self._energy = "100"
        elif event.of_type(BackpackChanged):
            self._description = "Your backpack now contains: {}".format(event.content())
        elif event.of_type(ThingInHandChanged):
            self._description = "Your hand now holds: {}".format(event.content())
        elif event.of_type(DoorWasLocked):
            self._description = "The door is locked. You will need a key."
        elif event.of_type(DoorWasUnlocked):
            self._description = "The door is unlocked."
        elif event.of_type(PlayerFinishedGame):
            self._title = "You decided to leave the game."
            self._description = "Thanks for playing. See you soon."

    def draw(self):
        scene = Scene(
            title=self._title,
            command=self._command,
            description=self._description,
            energy=self._energy
        )

        return self.show_output.put(scene)

    def welcome(self):
        return self.draw()

    def goodbye(self):
        return self.draw()
