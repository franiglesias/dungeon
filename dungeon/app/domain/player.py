class Player:
    def __init__(self):
        self.last_message = "I'm ready"
        self.exited = False

    @classmethod
    def awake(cls):
        return cls()

    def do(self, command, receiver):
        result = command.do(receiver)
        self.exited = result.is_finished()
        self.last_message = result.message()

    def is_alive(self):
        return True

    def has_won(self):
        return self.exited

    def said(self):
        return self.last_message
