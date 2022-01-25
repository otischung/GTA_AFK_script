import autoit
import keys
import pydirectinput
import random
import time
from tqdm import tqdm

# https://www.youtube.com/watch?v=tWqbl9IUdCg
# https://www.youtube.com/watch?v=VRsmPvu0xj0


def wasd():
    # DirectKeys.PressKey(17)  # w
    pydirectinput.keyDown("w")
    # print("Press w")
    time.sleep(random.randint(1, 5))
    pydirectinput.keyUp("w")
    # print("Release w")
    pydirectinput.keyDown("a")
    # print("Press a")
    time.sleep(random.randint(1, 5))
    pydirectinput.keyUp("a")
    # print("Release a")
    pydirectinput.keyDown("s")
    # print("Press s")
    time.sleep(random.randint(1, 5))
    pydirectinput.keyUp("s")
    # print("Release s")
    pydirectinput.keyDown("d")
    # print("Press d")
    time.sleep(random.randint(1, 5))
    pydirectinput.keyUp("d")
    # print("Release d")


def mouseMovement():
    autoit.mouse_move(1420, 830)
    time.sleep(random.randint(1, 5))
    autoit.mouse_move(1500, 830)
    time.sleep(random.randint(1, 5))
    autoit.mouse_move(1500, 900)
    time.sleep(random.randint(1, 5))
    autoit.mouse_move(1420, 900)
    time.sleep(random.randint(1, 5))


def nightclubBuyWeaponSupplies():
    pydirectinput.keyDown("e")  # Sit down
    time.sleep(0.1)
    pydirectinput.keyUp("e")
    time.sleep(7)
    pydirectinput.keyDown("enter")  # Access the master control terminal
    time.sleep(0.1)
    pydirectinput.keyUp("enter")
    time.sleep(3)
    autoit.mouse_move(1280, 700)  # Move to gunrunning supplies
    time.sleep(1)
    pydirectinput.keyDown("ctrlleft")  # Register to CEO
    time.sleep(0.1)
    pydirectinput.keyUp("ctrlleft")
    time.sleep(2)
    autoit.mouse_move(1280, 700)  # Gunrunning supplies
    keys.Keys().directMouse(buttons=keys.Keys().mouse_lb_press)
    time.sleep(0.1)
    keys.Keys().directMouse(buttons=keys.Keys().mouse_lb_release)
    time.sleep(1)
    autoit.mouse_move(1240, 860)  # Click to enter
    keys.Keys().directMouse(buttons=keys.Keys().mouse_lb_press)
    time.sleep(0.1)
    keys.Keys().directMouse(buttons=keys.Keys().mouse_lb_release)
    time.sleep(1)
    autoit.mouse_move(620, 670)  # Resupply
    keys.Keys().directMouse(buttons=keys.Keys().mouse_lb_press)
    time.sleep(0.1)
    keys.Keys().directMouse(buttons=keys.Keys().mouse_lb_release)
    time.sleep(1)
    autoit.mouse_move(1260, 1050)  # Buy supplies
    keys.Keys().directMouse(buttons=keys.Keys().mouse_lb_press)
    time.sleep(0.1)
    keys.Keys().directMouse(buttons=keys.Keys().mouse_lb_release)
    time.sleep(1)
    autoit.mouse_move(1420, 830)  # Confirm
    keys.Keys().directMouse(buttons=keys.Keys().mouse_lb_press)
    time.sleep(0.1)
    keys.Keys().directMouse(buttons=keys.Keys().mouse_lb_release)
    time.sleep(3)
    pydirectinput.keyDown("esc")  # Back to the main page of disruption
    time.sleep(0.1)
    pydirectinput.keyUp("esc")
    time.sleep(1)
    pydirectinput.keyDown("esc")  # Back to master control terminal
    time.sleep(0.1)
    pydirectinput.keyUp("esc")
    time.sleep(3)
    pydirectinput.keyDown("esc")  # Back to GTA main menu
    time.sleep(0.1)
    pydirectinput.keyUp("esc")
    time.sleep(1)
    pydirectinput.keyDown("esc")  # Back to the chair
    time.sleep(0.1)
    pydirectinput.keyUp("esc")
    time.sleep(3)
    keys.Keys().directMouse(buttons=keys.Keys().mouse_rb_press)  # Leave the chair
    time.sleep(0.1)
    keys.Keys().directMouse(buttons=keys.Keys().mouse_rb_release)
    time.sleep(6)
    # Cancel CEO
    pydirectinput.keyDown("m")
    time.sleep(0.1)
    pydirectinput.keyUp("m")
    time.sleep(0.1)
    pydirectinput.keyDown("enter")
    time.sleep(0.1)
    pydirectinput.keyUp("enter")
    time.sleep(0.1)
    pydirectinput.keyDown("up")
    time.sleep(0.1)
    pydirectinput.keyUp("up")
    time.sleep(0.1)
    pydirectinput.keyDown("enter")
    time.sleep(0.1)
    pydirectinput.keyUp("enter")


if __name__ == "__main__":
    for i in list(range(3))[::-1]:
        print(i + 1)
        time.sleep(1)
    print("Start")
    for j in range(10):
        nightclubBuyWeaponSupplies()
        for k in tqdm(range(1000)):
            mouseMovement()
