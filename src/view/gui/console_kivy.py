from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout


class Icetex_Calculator( App ):
    def build(self):
        main_container = BoxLayout(orientation = "vertical")

        credit_title = Label(text = "Escoge tu tipo de crédito")

        container_buttons = BoxLayout(orientation = "horizontal")

        container_inputs = BoxLayout(orientation = "horizontal")

        #Buttons for the credit type
        btn_30_porcentage = Button(text = "30 %", background_color =(0, 0.7, 1, 1))
        btn_60_porcentage = Button(text = "60 %", background_color =(0, 0.7, 1, 1))
        btn_100_porcentage = Button(text = "100 %", background_color =(0, 0.7, 1, 1))

        #Inputs for the semesteer
        layout_input_cost = AnchorLayout(anchor_x = "center", anchor_y = "center")
        layout_input_quantity = AnchorLayout(anchor_x = "center", anchor_y = "center")

        cost_semesteer_title = Label(text = "Ingresa el costo del semestre")
        quantity_semesteers_title = Label(text = "Ingresa la cantidad de semestres")

        cost_semesteer = TextInput(hint_text = "Ej: '12000000'", halign= "center", size_hint=(0.3, 0.4))
        quantity_semesteer = TextInput(hint_text = "Ej: 10", halign= "center", size_hint=(0.3, 0.4))

        layout_input_cost.add_widget(cost_semesteer)
        layout_input_quantity.add_widget(quantity_semesteer)



        #Add widgets to the container buttons
        container_buttons.add_widget(btn_30_porcentage)
        container_buttons.add_widget(btn_60_porcentage)
        container_buttons.add_widget(btn_100_porcentage)

        #Add widges to the container inputs


        main_container.add_widget(credit_title)
        main_container.add_widget(container_buttons)
        main_container.add_widget(cost_semesteer_title)
        main_container.add_widget(layout_input_cost)
        main_container.add_widget(quantity_semesteers_title)
        main_container.add_widget(layout_input_quantity)
        return main_container
    
        

    
if __name__ == "__main__":
    Icetex_Calculator().run()