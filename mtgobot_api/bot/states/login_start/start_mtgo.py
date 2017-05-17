from mtgobot_api.bot.states.state import State
from pywinauto import keyboard
from mtgobot_api.bot.states.login_start.login_prompt_wait import LoginPromptWaitState


class StartMtgoState(State):
    def apply(self, state_machine, new_image):
        # Maximize window
        keyboard.SendKeys('%+x')
        state_machine.remove_state(self)
        state_machine.enqueue_new_state(LoginPromptWaitState)
