from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Icetex( App ):
    def build(self):
        main_container = BoxLayout(orientation = "vertical")

        credit_title = Label(text = "Escoge tu tipo de crédito")

        container_buttons = BoxLayout(orientation = "horizontal")


        btn_30_porcentage = Button(text = "30 %", background_color = (0, 0.8, 1, 1))
        btn_60_porcentage = Button(text = "60 %", background_color = (0, 0.8, 1, 1))
        btn_100_porcentage = Button(text = "100 %", background_color = (0, 0.8, 1, 1))

        container_buttons.add_widget(btn_30_porcentage)
        container_buttons.add_widget(btn_60_porcentage)
        container_buttons.add_widget(btn_100_porcentage)

        main_container.add_widget(credit_title)
        main_container.add_widget(container_buttons)

        return main_container
        

    
if __name__ == "__main__":
    Icetex().run()