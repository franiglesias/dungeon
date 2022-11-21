from dungeon.app.show_output import ShowOutput


class ConsoleShowOutput(ShowOutput):
    def put(self, message):
        print(message + "\n")
