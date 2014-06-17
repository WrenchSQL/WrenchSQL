
# stdlib
import os
import sys
import textwrap
import platform
import signal

# requirements
try:
	from gi.repository import Gtk

except ImportError as e:
	import_error_help = {
		'Windows': {
			'gi': textwrap.dedent("""
				Please install GTK3.
				This can be a little tricky on windows.
				The most up to date help should be avaiable here:
				http://stackoverflow.com/a/6008390/1695680
			"""),
		}
	}

	if platform.system() in import_error_help\
	and e.name in import_error_help[platform.system()]:
		print("Fatal Error:")
		print(e.msg)
		print(import_error_help[platform.system()][e.name])
	else:
		raise(e)

	sys.exit()


class Wrench(Gtk.Builder):
	"""Graphical SQL client"""

	def __init__(this):
		super(Wrench, this).__init__()
		this.add_from_file("window.glade")
		this.connect_signals(this)

		this.window = this.get_object("window1")
		this.win2()
		this.window.show_all()

	connections_dir = os.path.join(os.path.expanduser("~"), '.wrenchsql', 'connections')
	def win2(this):
		# Create connections directory if not exists
		if not os.path.exists(this.connections_dir):
			os.makedirs(this.connections_dir)
			with open(os.path.join(this.connections_dir, 'default.wrench-mysql'), 'w') as fh:
				fh.write(textwrap.dedent("""
					Server=localhost;Uid=root;
				"""))

		this.win2_treestore()

	def win2_treestore(self):
		treestore = Gtk.TreeStore(str)
		treeview = Gtk.TreeView(treestore)

		parents = {}
		for dir, dirs, files in os.walk(self.connections_dir):
			for subdir in dirs:
				parents[os.path.join(dir, subdir)] = treestore.append(parents.get(dir, None), [subdir])
			for item in files:
				treestore.append(parents.get(dir, None), [os.path.splitext(item)[0]])

		column = Gtk.TreeViewColumn("Connections")
		treeview.append_column(column)

		cell = Gtk.CellRendererText()
		column.pack_start(cell, False)
		column.add_attribute(cell, "text", 0)

		self.get_object('connections_container').add(treeview)

	def onDeleteWindow(this, *args):
		Gtk.main_quit(*args)

	def onButtonPressed(this, button):
		print(this.get_object('dbstring').get_text())

	def main(this):
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		Gtk.main()
