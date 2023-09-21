class Processes:
    _singleton = None

    @staticmethod
    def __new__(cls):
        self = Processes._singleton
        if not self:
            Processes._singleton = self = super().__new__(cls)
        return self
    
    def __init__(self):
        pass

    _procinfo = {}

    def add_process(self, pid, info):
        Processes._procinfo[pid] = info

    def remove_process(self, pid):
        del Processes._procinfo[pid]
        