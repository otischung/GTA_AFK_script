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
        # for k in tqdm(range(710)):  # 8400s
        #     actions.wasd()
        actions.accessMasterControlTerminal()
        actions.CEO()
        actions.getIntoDisruption()
        actions.buyWeaponSupplies()
        actions.fromSuppliesToDisruption()
        actions.fromDisruptionToMCT()
        actions.leaveChair()
        actions.cancelCEO()
        actions.kickPlayersInPublicSession()
        # actions.accessMasterControlTerminal()
        for k in tqdm(range(710)):  # 8400s
            actions.wasd()
