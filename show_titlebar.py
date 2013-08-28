#!/usr/bin/env python
# −*− coding: UTF−8 −*−

# Written by Piotr Gularski <piotr.gularski@gmail.com>
# Copyright 2013 Piotr Gularski
# GPL v2 
# See copyright file that comes with this file for full licence

"""show_titlebar.py - Terminator Plugin to show title bar in context menu.

Normally it's better (for me) to have title bar hidden, but I can't drag'n'drop
terminal without a visible title bar. Now, digging through all options to turn
it visible, drag, drop, and again dig to hide it is an overkill. This plugin
makes my life way easier as "Show titlebar" is now an option in terminal's
context menu.

"""
import gtk

import terminatorlib.plugin as plugin
from terminatorlib.translation import _

# Every plugin you want Terminator to load *must* be listed in 'AVAILABLE'
AVAILABLE = ['ShowTitleBar']


class ShowTitleBar(plugin.MenuItem):
    """Terminator Plugin to display "Show titlebar" in context menu."""

    def __init__(self):
        plugin.MenuItem.__init__(self)

    def callback(self, menuitems, menu, terminal):
        item = gtk.CheckMenuItem(_('Show titlebar'))
        item.set_active(terminal.titlebar.get_property('visible'))
        item.connect("toggled", self.do_titlebar_toggle, terminal)
        menuitems.append(item)

    @classmethod
    def do_titlebar_toggle(cls, _widget, terminal):
        """Show or hide the terminal title bar. """
        config = terminal.config
        config['show_titlebar'] = not config['show_titlebar']
        config.save()
        terminal.toggle_widget_visibility(terminal.titlebar)
