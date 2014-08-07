
import signal
from gi.repository import Gtk
import os
from os import path
import json

from pprint import pprint

class Sessions(Gtk.Builder):

	query_string_form = None
	query_string_name = 'MySQL Standard'


	"""docstring for Sessions"""
	def __init__(this, connection_string = "MySQL Standard"):
		super(Sessions, this).__init__()
		this.connection_string = connection_string
		this.add_from_file( './dialog.glade')

		# Build GUI

		# Get objects
		this.window = this.get_object('dialog_sessions')
		this.liststore_connection_string = this.get_object('liststore_connection_string')
		this.combo_connection_string     = this.get_object('combo_connection_string')

		# Initialize interface
		for connection_string in next(os.walk('connection_strings'))[1]:
			this.liststore_connection_string.append([connection_string])
		this.combo_connection_string.set_active(0)

		this.query_string_form = this.get_object('query_string_form')
		this.combo_connection_string_changed(this.combo_connection_string)


		# Connect signals
		this.connect_signals(this)

		# Everything is ready
		this.window.show()

	def combo_connection_string_changed(this, widget, data=None):
		model = widget.get_model()
		active = widget.get_active()
		if active >= 0:
			this.query_string_name = model[active][0]
			print(this.query_string_name)
		else:
			super(Sessions, this).log_error('Failed to locate combo_connection_string option: ' + this.query_string_name)

		with open(path.join('connection_strings', this.query_string_name, 'connection_string.json')) as query_string_deff:
			query_string_deff = json.loads(query_string_deff.read())

		builder = Gtk.Builder()
		builder.add_from_file(path.join('connection_strings', this.query_string_name, 'form.glade'))


		this.replace_widget(
			this.query_string_form,
			builder.get_object('query_string_form')
		)
		this.query_string_form = builder.get_object('query_string_form')


	def main_quit(this, *args):
		Gtk.main_quit(*args)

	def main(this):
		signal.signal(signal.SIGINT, signal.SIG_DFL)
		Gtk.main()

	def replace_widget(this, current, new):
		"""
		Credit: Matthias @ http://stackoverflow.com/a/4119868/1695680

		Replace one widget with another.
		'current' has to be inside a container (e.g. gtk.VBox).
		"""

		if None is new:
			super(Sessions, this).log_error('form.glade not found in: ' + this.query_string_name)
			return None

		container = current.get_parent()
		assert Gtk.Container # is "current" inside a container widget?

		Gtk.Container.remove(container, current)
		new.reparent(container)

class Session(Sessions):
	"""Alias for Sessions"""

