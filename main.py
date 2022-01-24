import keyboard
from DirectKeys import *
import random
import time

# https://www.youtube.com/watch?v=tWqbl9IUdCg

counter = 0


def action():
    PressKey(17)  # w
    print("Press W")
    time.sleep(random.randint(1, 5))
    ReleaseKey(17)
    print("Release W")
    PressKey(30)  # a
    print("Press A")
    time.sleep(random.randint(1, 5))
    ReleaseKey(30)
    print("Release A")
    PressKey(31)  # s
    print("Press S")
    time.sleep(random.randint(1, 5))
    ReleaseKey(31)
    print("Release S")
    PressKey(32)  # d
    print("Press D")
    time.sleep(random.randint(1, 5))
    ReleaseKey(32)
    print("Release D")


if __name__ == "__main__":
    for i in list(range(3))[::-1]:
        print(i + 1)
        time.sleep(1)
    print("Start")
    while True:
        counter += 1
        print(f"{counter} cycle")
        action()
