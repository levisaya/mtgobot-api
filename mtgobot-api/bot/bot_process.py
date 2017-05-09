from multiprocessing import Process
import asyncio
from .state_machine import StateMachine


class BotProcess(Process):
    def __init__(self, username, password):
        Process.__init__(self)
        self.event_loop = None
        self.username = username
        self.password = password

    def poll(self, state_machine):
        state_machine.poll()
        self.event_loop.call_later(1, self.poll, *(state_machine,))

    def run(self):
        state_machine = StateMachine(self.username, self.password
                                     )
        self.event_loop = asyncio.new_event_loop()
        self.event_loop.call_soon_threadsafe(self.poll, *(state_machine,))
        self.event_loop.run_forever()
