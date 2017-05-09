from .states.state_return import StateReturn


class State:
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def apply_image(self, new_image):
        return StateReturn()

    def start_state(self):
        return StateReturn()

    def post_state(self):
        return StateReturn()
