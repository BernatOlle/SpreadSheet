
class CircularDependencyException(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __init__(self,mssg):
        Exception.__init__(self,mssg)
    def message(self):
        print("Circular Dependency Exception")
        return "Circular Dependency Exception"