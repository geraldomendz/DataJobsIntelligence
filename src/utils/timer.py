import time


class Timer:

    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def __str__(self):

        seconds = int(self.elapsed())

        horas = seconds // 3600
        minutos = (seconds % 3600) // 60
        segundos = seconds % 60

        if horas > 0:
            return f"{horas}h {minutos}min {segundos}s"

        if minutos > 0:
            return f"{minutos}min {segundos}s"

        return f"{segundos}s"