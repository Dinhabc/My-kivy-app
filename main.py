from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
Builder.load_file("main.kv")
class MyGrid(Widget):
	def check(self):
		if self.ids.ten.text == "Định" and self.ids.mk.text == "10A3":
			App.get_running_app().stop()

class MyApp(App):
	def build(self):
		#Clock.schedule_once(self.re_move, 5)
		return MyGrid()		
	 	
	#def re_move(self, dt):
	#	self.root.ids.i1.opacity=0
	#	self.root.ids.la.opacity=1
	
		
if __name__ == "__main__":
	MyApp().run()

	