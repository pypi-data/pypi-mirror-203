import logging

class SimpleLogger:

    def __init__(self, filepath='notebook_msg.log', is_print=True):
        self.is_print = is_print
        logging.basicConfig(
            filename=filepath,
            level=logging.INFO,
            format='%(asctime)s.%(msecs)03d || %(message)s',
            datefmt='%m/%d/%Y %H:%M:%S',
        )

    def set_print(self, is_print=True):
        self.is_print = is_print

    def log(self, message, is_print=True):
        if (is_print) or (is_print is None and self.is_print):
            is_print(message)
        logging.info(message)
        