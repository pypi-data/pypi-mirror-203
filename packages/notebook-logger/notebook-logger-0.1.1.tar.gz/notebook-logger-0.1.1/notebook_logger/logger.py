import logging

class SimpleLogger:

    def __init__(self, filepath='notebook_msg.log', print=True):
        self.is_print = print
        logging.basicConfig(
            filename=filepath,
            level=logging.INFO,
            format='%(asctime)s.%(msecs)03d || %(message)s',
            datefmt='%m/%d/%Y %H:%M:%S',
        )

    def set_print(self, print=True):
        self.is_print = print

    def log(self, message, print=True):
        if print or self.is_print:
            print(message)
        logging.info(message)
        