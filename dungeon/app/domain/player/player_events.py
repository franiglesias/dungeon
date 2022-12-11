class PlayerDied:
    def __init__(self):
        pass

    def name(self):
        return "player_died"


class PlayerEnergyChanged:
    def __init__(self, updated_energy):
        self._updated_energy = updated_energy

    def name(self):
        return "player_energy_changed"

    def energy(self):
        return self._updated_energy


class PlayerSentCommand:
    def __init__(self, command, argument):
        self._command = command
        self._argument = argument

    def name(self):
        return "player_sent_command"

    def command(self):
        return self._command

    def argument(self):
        return self._argument


class PlayerGotDescription:
    def __init__(self, description):
        self._description = description

    def name(self):
        return "player_got_description"

    def description(self):
        return self._description


class PlayerMoved:
    def __init__(self, room):
        self._room = room

    def room(self):
        return self._room

    def name(self):
        return "player_moved"


class PlayerExited:
    def __init__(self):
        pass

    def name(self):
        return "player_exited"


class PlayerGotThing:
    def __init__(self, thing):
        self._thing = thing

    def name(self):
        return "player_got_thing"

    def thing(self):
        return self._thing


class ActionNotCompleted:
    def __init__(self, reason):
        self._reason = reason

    def name(self):
        return "action_not_completed"

    def reason(self):
        return self._reason
