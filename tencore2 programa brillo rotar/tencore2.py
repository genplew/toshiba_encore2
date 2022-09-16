import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ScreenOrientationManager(Gtk.Window):

    def __init__(self):

        # init
        margin = 20
        devices = self.popcache()

        # window
        Gtk.Window.__init__(self, title="Toshiba Encore 2")

        # layout
        self.grid = Gtk.Grid()
        self.grid.props.margin_top = margin
        self.grid.props.margin_left = margin
        self.grid.props.margin_bottom = margin
        self.grid.props.margin_right = margin
        self.add(self.grid)

        # [1] add screen entry
        self.screen_entry = Gtk.Entry()
        self.screen_entry.set_placeholder_text("DSI-1")
        if len(devices[1]) != 0:
            self.screen_entry.set_text(devices[1])
        self.grid.attach(self.screen_entry, 1, 1, 50, 1)

        # [2] add touchpad entry
        self.touchpad_entry = Gtk.Entry()
        self.touchpad_entry.props.margin_top = margin
        self.touchpad_entry.set_placeholder_text("04F30732:00 04F3:0410")
        if len(devices[0]) != 0:
            self.touchpad_entry.set_text(devices[0])
        self.grid.attach(self.touchpad_entry, 1, 2, 50, 1)

        self.screen_rotacion = Gtk.Entry()
        self.screen_rotacion.props.margin_top = margin
        self.screen_rotacion.set_text("ROTACION Y BRILLO")
        self.grid.attach(self.screen_rotacion, 1, 4, 50, 1)
        self.screen_rotacion.set_sensitive(False)

        # [5] button layout
        self.buttons_grid = Gtk.Grid()
        self.buttons_grid.props.margin_top = margin
        self.grid.attach(self.buttons_grid, 1, 5, 1, 1)

        # [1] rotacion buttons
        left = self.create_button(self.buttons_grid, "Left", None)
        normal = self.create_button(self.buttons_grid, "Normal", left)
        right = self.create_button(self.buttons_grid, "Right", normal)
        invert = self.create_button(self.buttons_grid, "Invert", right)

        # [1] brillo button
        brillo0 = self.create_button2(self.buttons_grid, "brillo0", None)
        brillo10 = self.create_button2(self.buttons_grid, "brillo10", brillo0)
        brillo50 = self.create_button2(self.buttons_grid, "brillo50", brillo10)
        brillo100 = self.create_button2(self.buttons_grid, "brillo100", brillo50)

        # finally
        #self.on_check_changed(self.display_check)

    def create_button(self, grid, label, sibling):
        button = Gtk.Button(label=label)
        button.connect("clicked", self.on_click)
        margin = 20
        if sibling is None:
            grid.attach(button, 1, 1, 1, 1)
        else:
            button.props.margin_left = margin
            grid.attach_next_to(button, sibling, Gtk.PositionType.RIGHT, 1, 1)
        return button

    def create_button2(self, grid, label, sibling):
        button = Gtk.Button(label=label)
        button.connect("clicked", self.on_click)
        margin = 20
        button.props.margin_top = margin
        if sibling is None:
            grid.attach(button, 1, 2, 1, 1)
        else:
            button.props.margin_left = margin
            grid.attach_next_to(button, sibling, Gtk.PositionType.RIGHT, 1, 1)
        return button

#        button.props.margin_top = margin
#        button.props.margin_left = margin
#        grid.attach(button, 2, 2, 2, 1)
#        return button

    def on_click(self, widget):

        label = str(widget.get_label())

        if label.lower() == "left":
            self.rotate("l")
        elif label.lower() == "normal":
            self.rotate("n")
        elif label.lower() == "right":
            self.rotate("r")
        elif label.lower() == "invert":
            self.rotate("i")
        elif label.lower() == "brillo0":
            self.brillo0()
        elif label.lower() == "brillo10":
            self.brillo10()
        elif label.lower() == "brillo50":
            self.brillo50()
        elif label.lower() == "brillo100":
            self.brillo100()

    def rotate(self, rotation):
        proc = subprocess.Popen(['sh', 'bin/' + rotation + '.sh', self.screen_entry.get_text(), self.touchpad_entry.get_text()], stdout=subprocess.PIPE).wait()

    def brillo0(self):
        proc = subprocess.Popen(['sh', 'bin/0.sh'], stdout=subprocess.PIPE).wait()

    def brillo10(self):
        proc = subprocess.Popen(['sh', 'bin/10.sh'], stdout=subprocess.PIPE).wait()

    def brillo50(self):
        proc = subprocess.Popen(['sh', 'bin/50.sh'], stdout=subprocess.PIPE).wait()

    def brillo100(self):
        proc = subprocess.Popen(['sh', 'bin/100.sh'], stdout=subprocess.PIPE).wait()

    def encache(self, touchpad, touchscreen, display):
        with open('bin/config.txt', 'w') as file:
            file.write(touchpad + "\n" + touchscreen + "\n" + display)

    def popcache(self):
        devices = []
        with open('/bin/config.txt', 'r') as file:
            devices = [file.readline().strip(), file.readline().strip()]
        return devices


win = ScreenOrientationManager()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
