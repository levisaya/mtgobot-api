from flask import Flask, send_file
from bot.window_manager import WindowManager
from bot.state_machine import StateMachine
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


# @app.route("/screenshot")
# def screenshot():
#     image = bot_instance.take_screenshot()
#     img_io = BytesIO()
#     image.save(img_io, 'JPEG')
#     img_io.seek(0)
#     return send_file(img_io, mimetype='image/jpeg')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    state_machine = StateMachine()

    window_manager = WindowManager(state_machine)
    window_manager.run()
    app.run()