import itertools as it
import time
import itertools as it
import threading as th
import multiprocessing as mp
import numpy as np


class Worker:
    def __init__(self, id, global_counter) -> None:
        self.id = id
        self.global_counter = global_counter
        self.local_counter = it.count()

    def run(self):
        while True:
            time.sleep(np.random.rand()*2)
            global_step = next(self.global_counter)
            local_step = next(self.local_counter)
            print("Worker({}): {}".format(self.id, local_step))
            if global_step >= 20:
                break

global_counter = it.count()
nb_workers = mp.cpu_count()

workers = [Worker(id, global_counter) for id in range(nb_workers)]
threads = [th.Thread(target=worker.run) for worker in workers]

for thread in threads: thread.start()
for thread in threads: thread.join()

print("DONE!") 