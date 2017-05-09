from ...state import State
import time
from ..state_return import StateReturn


class LoginPromptWaitState(State):
    def apply_image(self, new_image):
        # TODO: Wait for login screen image
        time.sleep(5)
        return StateReturn(next_state='LoginState')