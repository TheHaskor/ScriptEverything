from bridge import shell_start as shell
import keyboard
shortcut = 'shift+s+e'


def on_triggered():
    shell()


keyboard.add_hotkey(shortcut, on_triggered)
keyboard.wait()


