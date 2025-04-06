# custom_clock.py
# A timeless clock widget, refined with macOS-inspired spacing.

from libqtile.widget import base
import datetime

class CustomClock(base.ThreadPoolText):
    # A perfectly balanced time display, with subtle elegance.
    
    defaults = [
        ("format", "%a  %b  %-d  %-I:%M  %p", "Time format: Day, month, date, hour, AM/PM — with refined spacing"),
        ("update_interval", 1.0, "Refresh interval in seconds for seamless flow"),
        ("foreground", "#f0edec", "Text color: Warm white for understated brilliance"),
    ]

    def __init__(self, **config):
        # Initialize with a clean, airy aesthetic.
        base.ThreadPoolText.__init__(self, "", **config)
        self.add_defaults(CustomClock.defaults)

    def poll(self):
        # Present the time with a touch of sophistication.
        return datetime.datetime.now().strftime(self.format)