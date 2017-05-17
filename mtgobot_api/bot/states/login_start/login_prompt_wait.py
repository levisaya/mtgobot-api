from mtgobot_api.bot.states.state import State
from mtgobot_api.bot.states.login_start.login import LoginState
import cv2
import os
from numpy import array
import logging


class LoginPromptWaitState(State):
    def __init__(self):
        super().__init__()
        self.login_button = cv2.imread(os.path.abspath(os.path.join(__file__, '..', 'images', 'login_button.png')))

    def apply(self, state_machine, new_image):
        result = cv2.matchTemplate(self.login_button, array(new_image), cv2.TM_CCOEFF_NORMED)

        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        logging.info("LoginPromptWaitState: maxVal = {}".format(maxVal))

        if maxVal > 0.6:
            state_machine.remove_state(self)
            state_machine.enqueue_new_state(LoginState)
