from dittolive.__observer import Observer

class FooObserver(Observer):
    def __init__(self, closed):
        super().__init__()
        self.closed = closed

    def _close_callback(self):
        self.closed[0] = True
        ...

def test_del_observer():
    closed = [False]
    observer = FooObserver(closed)
    assert closed[0] == False
    del observer
    assert closed[0] == True

def test_close_observer():
    closed = [False]
    observer = FooObserver(closed)
    assert closed[0] == False
    observer.close()
    assert closed[0] == True

def test_close_del_observer():
    closed = [False]
    observer = FooObserver(closed)
    assert closed[0] == False
    observer.close()
    assert closed[0] == True
    del observer
    assert closed[0] == True

def test_scoped_observer():
    def observe(closed):
        assert closed[0] == False
        _ = FooObserver(closed)

    closed = [False]
    observe(closed)
    assert closed[0] == True