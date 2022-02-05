#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# main.py
# Copyright (C) 2021 Asher <aswee39@eq.edu.au>
# 
# Python-SCPDatabase is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Python-SCPDatabase is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import GdkPixbuf, Gdk, Gtk
#gi.repository.require_version('Gdk', '3.0')
from gi.repository import WebKit2 as Webkit
import os, sys
from random import *
import subprocess
import json
from subprocess import call
webserver = subprocess.Popen(["python","src/webserver.py"])


#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "src/python_scpdatabase.ui"
#UI_FILE = "/usr/local/share/python_scpdatabase/ui/python_scpdatabase.ui"
LPORT = "8081"
fn = "src/test.json"
with open(fn) as f:
	data = json.load(f)

class GUI:
	def __init__(self):
		Webkit.WebView() 
		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)
		self.stack = Gtk.Stack()
		self.stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
		self.mainwindow = self.builder.get_object('mainwindow')
		window = self.builder.get_object('homepage')
		self.home = self.builder.get_object('table2')
		self.list = self.builder.get_object('revel')
		self.main = self.builder.get_object('Overlay1')
		self.revealer = self.builder.get_object('revel')
		for i in range(1,7):
			self.builder.get_object('k'+str(i))._value = i*1000
		#self.revealer.set_reveal_child(False)
		self.mainwindow.add(self.home)

		window.show_all()
		window.connect('delete_event', self.delete_event)
		
	def delete_event(self, *args):
		webserver.terminate()
		quit()

	def change_screen(self, button):
		parents = button.get_parent()
		current = parents.get_name()
		wanting = button.get_name()
		print(parents)
		print(current)
		print(wanting)
		self.mainwindow = self.builder.get_object('mainwindow')
		self.onscreen = self.builder.get_object(current)
		self.mainwindow.remove(self.onscreen)
		self.tobe = self.builder.get_object(wanting)
		self.mainwindow.add(self.tobe)
		#make this seperate def 
		if wanting == "randomScp":
			x= randint(1, 4740)
			x = f"{x:03}"
			self.webview = self.builder.get_object('randomview')
			self.webview.load_uri("http://localhost:"+LPORT+"/scp-"+x+"/")

	def search(self, button):
		self.parenting = self.builder.get_object("seachParent")
		listbox = Gtk.ListBox()
		child = self.parenting.get_child()
		if child != None:
			self.parenting.remove(child)
		self.newlist = Gtk.ListBox(name="Search")
		#self.newlist.set_halign(Gtk.Align.CENTER)
		self.parenting.add(self.newlist)

		K=button.get_text().lower()
		res = []
		namelist = []
		i=0;
		for idx, ele in enumerate(data["files"]):
			if K in ele['title'].lower() and i < 100:
					i = i+1
					res.append(idx)
					#namelist.append(ele['name'])
					row = Gtk.ListBoxRow(name="Search")
					row.set_halign(Gtk.Align.START)
					hbox = Gtk.Button(label = ele['title'],name = "searchedScp")

					hbox._value = ele['name']
					#hbox.set_halign(Gtk.Align.CENTER)
					hbox.set_valign(Gtk.Align.FILL)
					hbox.connect("clicked", self.searchedScp)
					hbox.connect("clicked", self.change_screen)
					row.add(hbox)
					self.newlist.add(row)
		self.newlist.show_all()		
		print("The indices list : " + str(res))



	def view_two_activated(self, button):
		self.home = self.builder.get_object('table2')
		window = self.builder.get_object('mainwindow')
		self.list = self.builder.get_object('revel')
		window.remove(self.home)
		window.add(self.list)
		
	def view_one_clicked(self, button):
		self.stack.set_visible_child(self.view_one)


	def back(self, button):
		self.tobe = self.builder.get_object(current)
		self.onscreen = self.builder.get_object(wanting)
		window.remove(self.onscreen)
		window.add(self.tobe)
		print(self.tobe)
		
	def get_handler_id(obj, signal_name):
		signal_id, detail = GObject.signal_parse_name(signal_name, obj, True)
		return GObject.signal_handler_find(obj, GObject.SignalMatchType.ID, signal_id, detail, None, None, None)

	#lists and populates the "Listing" table with buttons that the user is able to select
	#their desired scp from
	def oh_no_list(self, button):
		self.parenting = self.builder.get_object("responsibleParent")
		listbox = Gtk.ListBox()
		child = self.parenting.get_child()
		if child != None:
			self.parenting.remove(child)
		self.newlist = Gtk.ListBox(name="theList")
		self.parenting.add(self.newlist)
		number = button._value
		print(number)
		for x in range(number-1000,number):
			num = f"{x:03}"
			row = Gtk.ListBoxRow(name="listing")
			hbox = Gtk.Button(label = "SCP-"+num+"",name = "selectedSCP")
			hbox._value = num
			hbox.set_valign(Gtk.Align.FILL)
			hbox.connect("clicked", self.ShowScp)
			hbox.connect("clicked", self.change_screen)
			row.add(hbox)
			row.set_halign(Gtk.Align.START)
			self.newlist.add(row)
		self.newlist.show_all()
		
	def on_window_destroy(self, window):
		Gtk.main_quit()
	def searchedScp(self,button):
		x=button._value
		self.webview = self.builder.get_object('searchedview')
		self.webview.load_uri("http://localhost:"+LPORT+"/"+x+"/")
	
	def ShowScp(self, button):
		x=button._value
		self.webview = self.builder.get_object('specificView')
		self.webview.load_uri("http://localhost:"+LPORT+"/scp-"+x+"/")

		
	def reveal_child(button):
		if revealer.get_reveal_child():
			revealer.set_reveal_child(False)
			revealer.set_visible(False)
		else:
			revealer.set_reveal_child(True)
			revealer.set_visible(True)
def main():
	app = GUI()
	Gtk.main()
	
if __name__ == "__main__":
	sys.exit(main())
