class Var:

    def __init__(self, ob, name):
        self.name = name
        self.ob = ob

    def __eq__(self, other):
        if getattr(self, 'v', other) != other:
            return False
        self.v = other
        setattr(self.ob, self.name, other)
        return True

class Vars(object):

    def __init__(self):
        self.__vars = {}

    def __getattr__(self, name):
        if name in self.__vars:
            return self.__vars[name]

        var = self.__vars[name] = Var(self, name)
        return var
