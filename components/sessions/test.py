
from sessions import Session

Session().main()

#--------------------------------------

# from gi.repository import Gtk
# import os
# from os import path

# class MyApp(object):

# 	def __init__(self):
# 		# Build GUI
# 		self.builder = Gtk.Builder()
# 		self.builder.add_from_file(
# 			path.join(path.abspath(path.dirname(__file__)), 'dialog.glade')
# 		)

# 		# Get objects
# 		self.window = self.builder.get_object('dialog_sessions')
# 		self.myliststore = self.builder.get_object('liststore_connection_string')
# 		self.mycombobox = self.builder.get_object('combo_connection_string')

# 		# Initialize interface
# 		for connection_string in next(os.walk('connection_strings'))[1]:
# 			self.myliststore.append([connection_string])
# 		# self.myliststore.append(['hello wotld'])
# 		self.mycombobox.set_active(0)

# 		# Connect signals
# 		self.builder.connect_signals(self)

# 		# Everything is ready
# 		self.window.show()

# 	def main_quit(self, widget):
# 		Gtk.main_quit()

# 	def combobox_changed(self, widget, data=None):
# 		model = widget.get_model()
# 		active = widget.get_active()
# 		if active >= 0:
# 			code = model[active][0]
# 			print('The code of the selected color is {}'.format(code))
# 		else:
# 			print('No color selected')

# if __name__ == '__main__':
# 	try:
# 		gui = MyApp()
# 		Gtk.main()
# 	except KeyboardInterrupt:
# 		pass



# --------------------------------------

# from gi.repository import Gtk
# import os

# class Handler:
#     def onDeleteWindow(self, *args):
#         Gtk.main_quit(*args)

#     def onButtonPressed(self, button):
#         print("Hello World!")



# def on_country_combo_changed(combo):
#     tree_iter = combo.get_active_iter()
#     if tree_iter != None:
#         model = combo.get_model()
#         country = model[tree_iter][0]
#         print("Selected: country=%s" % country)



# builder = Gtk.Builder()
# builder.add_from_file("dialog.glade")
# builder.connect_signals(Handler())

# country_store = builder.get_object('connection_strings')
# for connection_string in next(os.walk('connection_strings'))[1]:
#     country_store.append([connection_string])

# window = builder.get_object("window1")

# connection_string.connect("changed", on_country_combo_changed)

# window.show_all()

# Gtk.main()

# --------------------------------------

# from gi.repository import Gtk

# class ComboBoxWindow(Gtk.Window):

#     def __init__(self):
#         Gtk.Window.__init__(self, title="ComboBox Example")

#         self.set_border_width(10)

#         name_store = Gtk.ListStore(int, str)
#         name_store.append([1, "Billy Bob"])
#         name_store.append([11, "Billy Bob Junior"])
#         name_store.append([12, "Sue Bob"])
#         name_store.append([2, "Joey Jojo"])
#         name_store.append([3, "Rob McRoberts"])
#         name_store.append([31, "Xavier McRoberts"])


#         vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

#         name_combo = Gtk.ComboBox.new_with_model_and_entry(name_store)
#         name_combo.connect("changed", self.on_name_combo_changed)
#         name_combo.set_entry_text_column(1)
#         vbox.pack_start(name_combo, False, False, 0)

#         country_store = Gtk.ListStore(str)
#         countries = ["Austria", "Brazil", "Belgium", "France", "Germany",
#             "Switzerland", "United Kingdom", "United States of America",
#             "Uruguay"]

#         from pprint import pprint
#         import os
#         for connection_string in next(os.walk('connection_strings'))[1]:

#             country_store.append([connection_string])

#         country_combo = Gtk.ComboBox.new_with_model(country_store)
#         country_combo.connect("changed", self.on_country_combo_changed)
#         renderer_text = Gtk.CellRendererText()
#         country_combo.pack_start(renderer_text, True)
#         country_combo.add_attribute(renderer_text, "text", 0)
#         vbox.pack_start(country_combo, False, False, True)

#         currencies = ["Euro", "US Dollars", "British Pound", "Japanese Yen",
#             "Russian Ruble", "Mexican peso", "Swiss franc"]
#         currency_combo = Gtk.ComboBoxText()
#         currency_combo.set_entry_text_column(0)
#         currency_combo.connect("changed", self.on_currency_combo_changed)
#         for currency in currencies:
#             currency_combo.append_text(currency)

#         vbox.pack_start(currency_combo, False, False, 0)

#         self.add(vbox)

#     def on_name_combo_changed(self, combo):
#         tree_iter = combo.get_active_iter()
#         if tree_iter != None:
#             model = combo.get_model()
#             row_id, name = model[tree_iter][:2]
#             print("Selected: ID=%d, name=%s" % (row_id, name))
#         else:
#             entry = combo.get_child()
#             print("Entered: %s" % entry.get_text())

#     def on_country_combo_changed(self, combo):
#         tree_iter = combo.get_active_iter()
#         if tree_iter != None:
#             model = combo.get_model()
#             country = model[tree_iter][0]
#             print("Selected: country=%s" % country)

#     def on_currency_combo_changed(self, combo):
#         text = combo.get_active_text()
#         if text != None:
#             print("Selected: currency=%s" % text)

# win = ComboBoxWindow()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()
