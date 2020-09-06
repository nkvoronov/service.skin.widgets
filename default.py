import sys
from lib import widgets

if (__name__ == "__main__"):
    widgets.log("script version %s started" % __addonversion__)
    widgets.Main()
    del widgets.Widgets_Monitor
    del widgets.Widgets_Player
    del widgets.Main
    widgets.log("script version %s stopped" % __addonversion__)
