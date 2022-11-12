class ShowOutput:
    def put(self, message):
        pass


class ConsoleShowOutput(ShowOutput):
    def put(self, message):
        print(message)
