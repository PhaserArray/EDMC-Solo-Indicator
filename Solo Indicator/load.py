import sys
import Tkinter as tk
from monitor import monitor

this = sys.modules[__name__]

def plugin_start():
    return "Solo Indicator"

def plugin_app(parent):
    for thing in parent.winfo_children():
        if thing._name == "cmdr":
            this.cmdrlabel = thing

def journal_entry(cmdr, is_beta, system, station, entry, state):
    if monitor.mode.lower() == "solo":
        this.cmdrlabel["text"] = '%s / %s' % (monitor.cmdr, 'Solo')