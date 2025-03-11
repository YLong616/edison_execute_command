


class E_ExecuteCommand(object):
    def __init__(self, command):
        self.command = command

    def execute(self):
        print("Executing command: %s" % self.command)
        return self.command

    def testfunc(self):
        print("Testing function edison..........")