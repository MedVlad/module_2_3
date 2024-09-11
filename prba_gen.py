import threading


class Counter:
    def __init__(self):
        self.val = 0
        self.lock = threading.Lock()

    def change(self):
        with self.lock:
            self.val += 1


def work(counter, operationsCount):
    for _ in range(operationsCount):
        counter.change()


def run_threads(counter, threadsCount, operationsPerThreadCount):
    threads = []

    for _ in range(threadsCount):
        t = threading.Thread(target=work, args=(counter, operationsPerThreadCount))

        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == "__main__":
    threadsCount = 100
    operationsPerThreadCount = 1000000
    expectedCounterValue = threadsCount * operationsPerThreadCount
    counters = [Counter()]

    for counter in counters:
        run_threads(counter, threadsCount, operationsPerThreadCount)
        print(f"{counter.__class__.__name__}: expected val: {expectedCounterValue},actual val: {counter.val}")
