"""
Logger Library for colored logging messages
"""
import logging as log
class handler(log.StreamHandler):
    colors = {
        log.DEBUG: '\033[37m',
        log.INFO: '\033[36m',
        log.WARNING: '\033[33m',
        log.ERROR: '\033[31m',
        log.CRITICAL: '\033[101m'
    }
    reset = '\033[0m'
    fmtr = log.Formatter('%(levelname)s %(message)s')
    def format(self, record):
        color = self.colors[record.levelno]
        log = self.fmtr.format(record)
        reset = self.reset
        return color + log + reset
log.basicConfig(level=log.DEBUG, handlers=[handler()])