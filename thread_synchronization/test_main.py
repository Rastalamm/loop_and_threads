from main import PrintSyncOnThreads
from threading import Lock, Thread

def test_printing_syncronously(capsys):
    digit_lock = PrintSyncOnThreads()
    digit_lock.run(3)
    captured = capsys.readouterr()
    assert captured.out == "Thread 1: The number is '1'\nThread 2: The number is '2'\nThread 1: The number is '3'\n"

    digit_lock.run(5)
    captured = capsys.readouterr()
    assert captured.out == "Thread 1: The number is '1'\nThread 2: The number is '2'\nThread 1: The number is '3'\nThread 2: The number is '4'\nThread 1: The number is '5'\n"
