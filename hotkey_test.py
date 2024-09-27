import ctypes
import ctypes.wintypes as wintypes
import atexit

# Constants from the Windows API
MOD_ALT = 0x0001  # ALT key
MOD_CONTROL = 0x0002  # CTRL key
WM_HOTKEY = 0x0312  # Hotkey message

# Register the hotkey function from the Windows API
user32 = ctypes.windll.user32

# Define a callback for cleanup
def unregister_hotkeys():
    user32.UnregisterHotKey(None, 1)

# Register cleanup on program exit
atexit.register(unregister_hotkeys)

def register_hotkey():
    if not user32.RegisterHotKey(None, 1, MOD_CONTROL | MOD_ALT, wintypes.VK_F5):
        print("Failed to register hotkey.")
        return False
    return True

def listen_for_hotkey():
    msg = wintypes.MSG()
    while True:
        if user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
            if msg.message == WM_HOTKEY:
                print("Hotkey pressed!")
                if msg.wParam == 1:
                    break  # Exit on hotkey press
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))

if __name__ == "__main__":
    if register_hotkey():
        print("Listening for hotkey (CTRL + ALT + F5)...")
        listen_for_hotkey()
    else:
        print("Could not register the hotkey.")
