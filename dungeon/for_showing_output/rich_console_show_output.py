from dungeon.app.show_output import ShowOutput


class RichConsoleShowOutput(ShowOutput):
    def put(self, scene):
        print("You said: {}\n".format(scene.command()))
        print("{}".format(scene.title()))
        print("--------------------------------------")
        print("{}".format(scene.description()))
        print("Remaining energy: {}".format(scene.energy()))
        print("======================================")
