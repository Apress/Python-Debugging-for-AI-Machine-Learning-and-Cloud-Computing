import processes
import filemon
import time

def main():
    procs = processes.Processes()
    files = filemon.Files()
    for pid in range (1, 10): 
        procs.add_process(pid, "info")
    while True:
        pid += 1
        procs.add_process(pid, "info")
        time.sleep(1)
        procs.remove_process(pid)
        time.sleep(1)
        files.process_files()

if __name__ == "__main__":
    main()
