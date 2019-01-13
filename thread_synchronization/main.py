from threading import Lock, Thread

class PrintSyncOnThreads():
    """Runs two threads while printing odd / even numbers to console, syncronously switching between threads"""
    def __init__(self):
        self.digit_type = "odd"
        self.lock = Lock()

    def choose_odd_or_even(self, digit_type):
        while True:
            self.lock.acquire()
            if self.digit_type == digit_type:
                break
            self.lock.release()

    def change_to_thread(self, new_digit_type):
        self.digit_type = new_digit_type
        self.lock.release()

    def print_statement(self, thread_num, num):
        print("Thread {thread_num}: The number is '{num}'".format(thread_num=thread_num, num=num))

    def odd_printing(self, lock, n, thread_num):
        for i in range(1, (n + 1)):
            self.choose_odd_or_even("odd")
            if (i % 2 != 0):
                self.print_statement(thread_num, i)
            self.change_to_thread("even")

    def even_printing(self, lock, n, thread_num):
        for i in range(1, (n + 1)):
            self.choose_odd_or_even("even")
            if (i % 2 == 0):
                self.print_statement(thread_num, i)
            self.change_to_thread("odd")

    def run(self, num=100):
        lock = Lock()

        t1 = Thread(target=self.odd_printing, args=(lock, num, "1"))
        t2 = Thread(target=self.even_printing, args=(lock, num, "2"))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

if __name__ == "__main__":
    digit_lock = PrintSyncOnThreads()
    digit_lock.run()