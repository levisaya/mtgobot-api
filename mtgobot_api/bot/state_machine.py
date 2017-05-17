from mtgobot_api.bot.singleton import Singleton
from mtgobot_api.bot.states.login_start.start_mtgo import StartMtgoState
import logging


class StateMachine(metaclass=Singleton):
    def __init__(self):
        self.state_queue = [StartMtgoState()]

    def apply(self, new_image):
        if len(self.state_queue):
            logging.info("Executing state {} UID {}".format(self.state_queue[0].__class__.__name__, self.state_queue[0].uid))
            self.state_queue[0].apply(self, new_image)
        return False

    def enqueue_new_state(self, new_state_cls):
        logging.info("Enqueueing state {}".format(new_state_cls.__name__))
        self.state_queue.append(new_state_cls())

    def remove_state(self, state_to_remove):
        logging.info("Removing state {} UID ()".format(state_to_remove.__class__.__name__, state_to_remove.uid))
        self.state_queue.remove(state_to_remove)
