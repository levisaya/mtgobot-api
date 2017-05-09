from ..state import State
from .state_return import StateReturn


class IdleState(State):
    def apply_image(self, new_image):
        return StateReturn()