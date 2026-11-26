import evdev
from evdev import UInput, ecodes as e
import threading, time, select

CPS = 1000 # clicks per second
TOGGLE_KEY = e.KEY_GRAVE   # backtick
QUIT_KEY = e.KEY_F7

capabilities = {
    e.EV_KEY: [e.BTN_LEFT, e.BTN_RIGHT, e.BTN_MIDDLE],
    e.EV_REL: [e.REL_X, e.REL_Y, e.REL_WHEEL],
}
ui = UInput(capabilities, name="autoclicker-mouse")
time.sleep(1)  # give the compositor time to register the new device

clicking = False

def click_loop():
    while True:
        if clicking:
            ui.write(e.EV_KEY, e.BTN_LEFT, 1)
            ui.syn()
            time.sleep(0.01)
            ui.write(e.EV_KEY, e.BTN_LEFT, 0)
            ui.syn()
        time.sleep(1 / CPS)

threading.Thread(target=click_loop, daemon=True).start()

keyboards = []
for path in evdev.list_devices():
    dev = evdev.InputDevice(path)
    if e.KEY_A in dev.capabilities().get(e.EV_KEY, []):
        keyboards.append(dev)
        print("Using keyboard:", dev.name, dev.path)

if not keyboards:
    print("No keyboards found. Check that you're in the input group.")
    raise SystemExit(1)

print("Running. ` toggles clicking, F7 quits.")

try:
    while True:
        readable, _, _ = select.select(keyboards, [], [])
        for dev in readable:
            for event in dev.read():
                if event.type == e.EV_KEY and event.value == 1:
                    if event.code == TOGGLE_KEY:
                        clicking = not clicking
                        print("Clicking:", clicking)
                    elif event.code == QUIT_KEY:
                        raise KeyboardInterrupt
except KeyboardInterrupt:
    print("Exiting")
finally:
    ui.close()
