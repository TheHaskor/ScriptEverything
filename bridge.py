import time
from win32gui import GetWindowText, GetForegroundWindow, SetForegroundWindow
from win32process import GetWindowThreadProcessId

from win32com import client


shell = client.Dispatch("WScript.Shell")


class ActivateVenv:

    def set_cmd_to_foreground(self, hwnd, extra):
        """sets first command prompt to forgeround"""

        if "cmd.exe" in GetWindowText(hwnd):
            SetForegroundWindow(hwnd)
            return

    def get_pid(self):
        """gets process id of command prompt on foreground"""

        window = GetForegroundWindow()
        return GetWindowThreadProcessId(window)[1]

    def activate_venv(self, shell, venv_location):
        """activates venv of the active command prompt"""

        shell.AppActivate(self.get_pid())
        self.prepare_main()

    @staticmethod
    def execute_command(function_str):
        shell.SendKeys(f"{function_str} " + "{ENTER}")

    def prepare_main(self):
        self.clear_screen()
        self.execute_command('python')
        self.execute_command('from main import *')

    def clear_screen(self):
        self.execute_command('cls')

    def open_cmd(self, shell):
        """ opens cmd """

        shell.run("cmd.exe")
        time.sleep(1)


def shell_start():
    run_venv = ActivateVenv()
    run_venv.open_cmd(shell)
    run_venv.activate_venv(shell, None)


if __name__ == "__main__":
    shell_start()
