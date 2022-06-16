import eel
import keyboard


eel.init('../front')


@eel.expose
def index():
    return 'Hello World'


eel.start(
    'templates/index.html',
    jinja_templates='templates',
    mode="chrome",
    size=(650, 760)
)
