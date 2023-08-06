# This file is placed in the Public Domain.
# pylint: disable=C0115,C0116,W1201,R0903,E0402


"log"


import logging as log
import logging.handlers as loghdl
import os


from .persist import Persist, cdir, touch


ERASE_LINE = '\033[2K'
BOLD='\033[1m'
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
ENDC = '\033[0m'


LEVELS = {'debug': log.DEBUG,
          'info': log.INFO,
          'warning': log.WARNING,
          'warn': log.WARNING,
          'error': log.ERROR,
          'critical': log.CRITICAL
         }

RLEVELS = {log.DEBUG: 'debug',
           log.INFO: 'info',
           log.WARNING: 'warn',
           log.ERROR: 'error',
           log.CRITICAL: 'critical'
          }


class Logging:

    @staticmethod
    def debug(txt):
        pass


def setlevel(name="info"):
    logfile = os.path.join(Persist.logdir(), "operbot.log")
    cdir(logfile)
    touch(logfile)
    fplain = "%(message)s"
    datefmt = '%H:%M:%S'
    formatter_plain = log.Formatter(fplain, datefmt=datefmt)
    try:
        filehandler = loghdl.TimedRotatingFileHandler(logfile, 'midnight')
    except (IOError, AttributeError) as ex:
        log.error("can't create file loggger %s" % str(ex))
        filehandler = None
    level = LEVELS.get(str(name).lower(), log.NOTSET)
    root = log.getLogger()
    root.setLevel(level)
    if root and root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)
    mlog = log.StreamHandler()
    mlog.setLevel(level)
    mlog.setFormatter(formatter_plain)
    root.addHandler(mlog)
    if filehandler:
        root.addHandler(filehandler)
    log.info(name)


def getlevel():
    root = log.getLogger()
    return RLEVELS.get(root.level)
