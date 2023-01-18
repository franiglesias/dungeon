from dungeon.app.events.subject import Event


class PlayerDied(Event):
    def __init__(self):
        pass


class PlayerEnergyChanged(Event):
    def __init__(self, updated_energy):
        self._updated_energy = updated_energy

    def energy(self):
        return self._updated_energy


class PlayerSentCommand(Event):
    def __init__(self, command, argument):
        self._command = command
        self._argument = argument

    def command(self):
        return self._command

    def argument(self):
        return self._argument


class PlayerGotDescription(Event):
    def __init__(self, description):
        self._description = description

    def description(self):
        return self._description


class PlayerMoved(Event):
    def __init__(self, room):
        self._room = room

    def room(self):
        return self._room


class PlayerExited(Event):
    def __init__(self):
        pass


class ActionNotCompleted(Event):
    def __init__(self, reason):
        self._reason = reason

    def reason(self):
        return self._reason


class PlayerHitWall(Event):
    def __init__(self):
        pass


class PlayerAwake(Event):
    def __init__(self):
        pass


class PlayerCollectedThing(Event):
    def __init__(self, thing):
        self._thing = thing

    def thing(self):
        return self._thing


class BackpackChanged(Event):
    def __init__(self, content):
        self._content = content

    def content(self):
        return self._content


class ThingInHandChanged(Event):
    def __init__(self, content):
        self._content = content

    def content(self):
        return self._content


class DoorWasLocked(Event):
    pass


class DoorWasUnlocked(Event):
    def __init__(self):
        pass


class PlayerFinishedGame(Event):
    def __init__(self):
        pass
