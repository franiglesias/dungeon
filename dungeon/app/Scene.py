class Scene():
    def __init__(self, title, command, description, energy):
        self._title = title
        self._command = command
        self._description = description
        self._energy = energy

    @classmethod
    def from_result(cls, result):
        return cls(
            title=result.get("title"),
            command=result.get("command"),
            description=result.get("message"),
            energy=result.get("energy")
        )

    def title(self):
        return self._title

    def command(self):
        return self._command

    def description(self):
        return self._description

    def energy(self):
        return self._energy
