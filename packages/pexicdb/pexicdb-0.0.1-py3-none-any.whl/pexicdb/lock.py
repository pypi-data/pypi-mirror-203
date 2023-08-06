import time

class Lock:
    """
    Simple lock mechanism to perform operations in queue.

    Loop is used to wait while the lock is used by another function,
    after one by one operation is performed.

    Basic example:
    ```
    import time
    import threading
    from pexicdb.lock import Lock

    lock = Lock()

    def a1():
        with lock:
            for i in range(10):
                print("a1:",i)
                time.sleep(0.5)

    def b1():
        with lock:
            for i in range(10):
                print("b1:",i)
                time.sleep(0.5)

    t1 = threading.Thread(target=a1)
    t2 = threading.Thread(target=b1)
    t1.start()
    t2.start()
    ```
    """
    def __init__(self) -> None:
        self.__locked = False
    
    def __enter__(self):
        while self.__locked is True:
            time.sleep(0.05)
        
        self.__locked = True

    def __exit__(self, *args, **kws):
        self.__locked = False
