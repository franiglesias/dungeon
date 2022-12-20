class Event:
    def name(self):
        pass

    def of_type(self, cls):
        return isinstance(self, cls)


class PlayerDied(Event):
    def __init__(self):
        pass

    def name(self):
        return "player_died"


class PlayerEnergyChanged(Event):
    def __init__(self, updated_energy):
        self._updated_energy = updated_energy

    def name(self):
        return "player_energy_changed"

    def energy(self):
        return self._updated_energy


class PlayerSentCommand(Event):
    def __init__(self, command, argument):
        self._command = command
        self._argument = argument

    def name(self):
        return "player_sent_command"

    def command(self):
        return self._command

    def argument(self):
        return self._argument


class PlayerGotDescription(Event):
    def __init__(self, description):
        self._description = description

    def name(self):
        return "player_got_description"

    def description(self):
        return self._description


class PlayerMoved(Event):
    def __init__(self, room):
        self._room = room

    def room(self):
        return self._room

    def name(self):
        return "player_moved"


class PlayerExited(Event):
    def __init__(self):
        pass

    def name(self):
        return "player_exited"


class PlayerGotThing(Event):
    def __init__(self, thing):
        self._thing = thing

    def name(self):
        return "player_got_thing"

    def thing(self):
        return self._thing


class ActionNotCompleted(Event):
    def __init__(self, reason):
        self._reason = reason

    def name(self):
        return "action_not_completed"

    def reason(self):
        return self._reason


class PlayerHitWall(Event):
    def __init__(self):
        pass

    def name(self):
        return "player_hit_wall"


class PlayerAwake(Event):
    def __init__(self):
        pass

    def name(self):
        return "player_awake"


class PlayerCollectedThing(Event):
    def __init__(self, thing):
        self._thing = thing

    def name(self):
        return "player_collected_thing"

    def thing(self):
        return self._thing


class BackpackChanged(Event):
    def __init__(self, content):
        self._content = content

    def name(self):
        return "backpack_changed"

    def content(self):
        return self._content
