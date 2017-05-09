from ...state import State
from ..state_return import StateReturn
from pywinauto import keyboard


class LoginState(State):
    def apply_image(self, new_image):
        keyboard.SendKeys('+{VK_TAB}{DELETE}')
        keyboard.SendKeys(self.state_machine.storage.get('username') +
                          '{VK_TAB}' +
                          self.state_machine.storage.get('password'))
        keyboard.SendKeys('{ENTER 2}')
        return StateReturn(next_state='IdleState')