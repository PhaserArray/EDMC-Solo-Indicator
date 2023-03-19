import logging
import tkinter as tk
from monitor import monitor
from config import appname

def plugin_start3(plugin_dir = ""):
    return "Solo Indicator"

class This():
    def __init__(self):
        self.logger = logging.getLogger(f'{appname}.{plugin_start3()}')
        self.logger.info("Starting Solo Indicator")

this = This()

def plugin_app(parent):
    this.parent = parent

def journal_entry(cmdr, is_beta, system, station, entry, state):
    if not this.parent:
        return
    
    cmdr = this.parent.nametowidget(f".{appname.lower()}.cmdr")
    if not cmdr:
        this.logger.error("Could not find cmdr widget")
        return

    if monitor.mode.lower() == "solo":
        cmdr["text"] = '%s / %s' % (monitor.cmdr, 'Solo')
