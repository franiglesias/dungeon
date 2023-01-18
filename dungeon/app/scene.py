class Scene:
    def __init__(self, title, command, description, energy, inventory, hand):
        self._title = title
        self._command = command
        self._description = description
        self._energy = energy
        self._inventory = inventory
        self._hand = hand

    def title(self):
        return self._title

    def command(self):
        return self._command

    def description(self):
        return self._description

    def energy(self):
        return self._energy

    def inventory(self):
        return self._inventory

    def hand(self):
        return self._hand
