import actions
import pydirectinput
import random
import time
from tqdm import tqdm

if __name__ == "__main__":
    for i in list(range(3))[::-1]:
        print(i + 1)
        time.sleep(1)
    print("Start")
    for j in range(10):
        actions.nightclubBuyWeaponSupplies()
        for k in tqdm(range(2800)):  # 8400s
            pydirectinput.keyDown("f4")
            time.sleep(0.1)
            pydirectinput.keyUp("f4")
            time.sleep(random.randint(1, 5))
