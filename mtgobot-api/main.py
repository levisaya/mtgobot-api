from flask import Flask, send_file
from bot.bot_process import BotProcess
from io import BytesIO
from optparse import OptionParser

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
    parser = OptionParser()
    parser.add_option("-u", "--username", dest="username")
    parser.add_option("-p", "--password", dest="password")

    (options, args) = parser.parse_args()

    bot = BotProcess(options.username, options.password)
    bot.start()
    app.run()