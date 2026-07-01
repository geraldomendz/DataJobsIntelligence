import time


class Timer:

    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def __str__(self):
        return f"{self.elapsed():.2f}s"