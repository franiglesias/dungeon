from dungeon.app.domain.thing import Thing


class Container:
    def __init__(self):
        pass

    def get_safe(self, thing_name) -> Thing:
        raise NotImplementedError

    def exchange(self, to_keep: Thing, thing_name) -> Thing:
        raise NotImplementedError
