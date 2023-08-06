class Cliops:
    def __init__(self):
        self.doVessels = False
        self.doSpines = False
        self.doLog = False
    
    def parseArgs(self, args):
        if len(args) > 1:
            for arg in range(1, len(args)):
                if "v" in args[arg]:
                    self.doVessels = True
                if "s" in args[arg]:
                    self.doSpines = True
                if "l" in args[arg]:
                    self.doLog = True