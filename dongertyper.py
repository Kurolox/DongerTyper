#! /usr/bin/python3

import gi, os, sys, xerox
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class FlowBoxWindow(Gtk.Window):
    # You can manually add emotes by putting them in donglist.txt.
    # Put just one for each line.
    dongerfile = open(os.path.join(sys.path[0], "donglist.txt"), "r")
    dongerlist = dongerfile.read().splitlines()

    def __init__(self):
        Gtk.Window.__init__(self, title="FlowBox Demo")
        self.set_border_width(10)
        self.set_default_size(300, 250)

        header = Gtk.HeaderBar(title="DongerTyper v.0.1a")
        header.set_subtitle("ヽ༼ຈل͜ຈ༽ﾉ raise your dongers ヽ༼ຈل͜ຈ༽ﾉ")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(30)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

        self.create_flowbox(flowbox)

        scrolled.add(flowbox)

        self.add(scrolled)
        self.show_all

    def on_donger_clicked(self, button, donger):
        """Links each button to a donger in the clipboard."""
        xerox.copy(donger)
        Gtk.main_quit()

    def create_flowbox(self, flowbox):
        """Adds each donger to a button."""
        for donger in self.dongerlist:
            button = Gtk.Button.new_with_label(donger)
            button.connect("clicked", self.on_donger_clicked, donger)
            flowbox.add(button)


win = FlowBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.set_type_hint(Gdk.WindowTypeHint.UTILITY)
win.show_all()
Gtk.main()
