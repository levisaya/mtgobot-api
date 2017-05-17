import subprocess
from pywinauto.application import Application
from pywinauto.findwindows import ElementNotFoundError
import asyncio
from mtgobot_api.bot.singleton import Singleton


class WindowManager(metaclass=Singleton):
    def __init__(self, state_machine):
        self.image_hash = None
        self.current_state = None

        self.mtgo_process = subprocess.Popen(['cmd.exe', '/c', "Magic The Gathering Online .appref-ms"])
        self.event_loop = asyncio.new_event_loop()
        self.state_machine = state_machine

    def run(self):
        self.event_loop.call_soon_threadsafe(self.poll)
        self.event_loop.run_forever()

    @staticmethod
    def get_mtgo_window():
        mtgo_window = None
        try:
            mtgo_app = Application().Connect(title=u'Magic: The Gathering Online')
        except ElementNotFoundError:
            mtgo_app = None

        if mtgo_app is not None:
            try:
                mtgo_window = mtgo_app[u'Magic: The Gathering Online']
            except AttributeError:
                pass
        return mtgo_window

    def poll(self):
        mtgo_window = self.get_mtgo_window()
        repoll_immediate = False
        if mtgo_window is not None:
            mtgo_window.set_focus()
            image = mtgo_window.capture_as_image()
            repoll_immediate = self.state_machine.apply(image)

        if repoll_immediate:
            self.event_loop.call_soon_threadsafe(self.poll())
        else:
            self.event_loop.call_later(1, self.poll)

