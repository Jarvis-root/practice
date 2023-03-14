import datetime
import threading
import time

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import register_thread


def main():
    # put_row([input_group('lalalal', [put_input('a',), put_input('b', )]),])
    put_row([put_code('A'), None, put_code('B')])


def show_time():
    while True:
        with use_scope(name='time', clear=True):
            put_text(datetime.datetime.now())
            time.sleep(1)

def app():
    t = threading.Thread(target=show_time)
    register_thread(t)
    put_markdown('## Clock')
    t.start()  # run `show_time()` in background

    # ❌ this thread will cause `SessionNotFoundException`
    # threading.Thread(target=show_time).start()

    put_text('Background task started.')




if __name__ == '__main__':
    start_server(main, debug=True, port=8080)