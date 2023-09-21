import processes

class Files:
    def __init__(self):
        self._processes = processes.Processes()
        self._count = 0

    def process_files(self):
        self._count += 1
        if self._count > 25:
            self._processes.add_process(self._count, "")
