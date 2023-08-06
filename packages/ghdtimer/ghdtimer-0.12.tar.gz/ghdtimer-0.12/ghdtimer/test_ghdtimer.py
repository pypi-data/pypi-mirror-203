from . import Timer
import time

def test_1():
    timer = Timer()
    assert True

def test_2():
    timer = Timer(mode="ms", decimals=3)

    timer.tick()
    time.sleep(1)
    timer.tock()
    time.sleep(1)
    timer.tock()
    time.sleep(1)
    timer.tock()
    assert True
