import logging
from .states.login_start.start_mtgo import StartMtgoState
from .states.login_start.login_prompt_wait import LoginPromptWaitState
from .states.login_start.login import LoginState
from .states.idle_state import IdleState
import imagehash


class StateMachine:
    def __init__(self, username, password):
        logging.basicConfig()
        self.storage = {'username': username, 'password': password}
        self.states = {state.__name__: state(self) for state in [StartMtgoState,
                                                                 LoginPromptWaitState,
                                                                 LoginState,
                                                                 IdleState]}
        self.image_hash = None
        self.current_state = self.states['StartMtgoState']
        state_return = self.current_state.start_state()
        self.storage.update(state_return.storage_updates)

    def poll(self):
        new_image = False
        if self.storage.get('mtgo_window', None) is not None:
            image = self.storage.get('mtgo_window').capture_as_image()
            hash = imagehash.average_hash(image, hash_size=64)
            new_image = hash == self.image_hash
            self.image_hash = hash

        if new_image and self.current_state is not None:
            state_return = self.current_state.apply_image(new_image)
            if state_return.next_state is not None:
                state_name = state_return.next_state
                next_state = self.states.get(state_name)
                logging.info("Switching from state {} to {}".format(self.current_state.__class__.__name__,
                                                                    state_name))
                self.current_state.post_state()

                self.storage.update(state_return.storage_updates)

                state_return = next_state.start_state()
                self.storage.update(state_return.storage_updates)

                self.current_state = next_state
