from ...state import State
import subprocess
import time
from pywinauto.application import Application, ProcessNotFoundError
import sys
from ..state_return import StateReturn
from pywinauto import keyboard


class StartMtgoState(State):
    def start_state(self):
        mtgo_process = subprocess.Popen(['cmd.exe', '/c', "Magic The Gathering Online .appref-ms"])

        mtgo_process_timeout = 10

        start_time = time.time()
        while time.time() - start_time < mtgo_process_timeout:
            try:
                mtgo_app = Application().connect(path='MTGO.exe')
                break
            except ProcessNotFoundError:
                time.sleep(1)
        if mtgo_app is None:
            print("Failed to start MTGO")
            sys.exit(1)
        # TODO: Figure out a better way to wait for the login prompt
        time.sleep(5)

        mtgo_window = mtgo_app[u'Magic: The Gathering Online']
        mtgo_window.SetFocus()

        # Maximize window
        keyboard.SendKeys('%+x')
        return StateReturn(storage_updates={'mtgo_process': mtgo_process,
                                            'mtgo_window': mtgo_window,
                                            'mtgo_app': mtgo_app},
                           next_state='LoginPromptWaitState')

    def apply_image(self, new_image):
        return StateReturn(next_state='LoginPromptWaitState')