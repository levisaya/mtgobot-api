from mtgobot_api.bot.states.state import State
from mtgobot_api.bot.states.login_start.main_screen_wait import MainScreenWaitState
from pywinauto import keyboard
from optparse import OptionParser
import time


class LoginState(State):
    def apply(self, state_machine, new_image):
        parser = OptionParser()
        parser.add_option("-u", "--username", dest="username")
        parser.add_option("-p", "--password", dest="password")

        (options, args) = parser.parse_args()

        keyboard.SendKeys('+{VK_TAB}{DELETE}')
        keyboard.SendKeys(options.username +
                          '{VK_TAB}' +
                          options.password)
        time.sleep(1)
        keyboard.SendKeys('{ENTER}')
        state_machine.remove_state(self)
        state_machine.enqueue_new_state(MainScreenWaitState)
