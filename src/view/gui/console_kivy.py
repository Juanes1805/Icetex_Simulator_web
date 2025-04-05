from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle


class Icetex_Calculator( App ):
    def build(self):
        main_container = BoxLayout(orientation = "vertical")
        
        # Agregar un color de fondo usando Canvas
        with main_container.canvas.before:
            Color(240, 240, 240, 1) 
            self.rect = Rectangle(pos=main_container.pos, size=main_container.size)
            
        def update_react(instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size
        
        main_container.bind(pos=update_react, size=update_react)

        title_welcome = Label(text = "Welcome to the ICETEX simulator", color=(0,0,0,1), font_size=30)
  
        container_tittle_welcome = AnchorLayout(anchor_x = "center", anchor_y = "center")
        
        container_tittle_welcome.add_widget(title_welcome)
        
        credit_title = Label(text = "Choose your credit type", color=(0,0,0,1), font_size=19)

        container_buttons = BoxLayout(orientation = "horizontal")

        #Buttons for the credit type
        btn_30_porcentage = Button(text = "30 %", background_color =(0, 0.7, 1, 1))
        btn_60_porcentage = Button(text = "60 %", background_color =(0, 0.7, 1, 1))
        btn_100_porcentage = Button(text = "100 %", background_color =(0, 0.7, 1, 1))

        #Inputs for the semesteer
        layout_input_cost = AnchorLayout(anchor_x = "center", anchor_y = "center")
        layout_input_quantity = AnchorLayout(anchor_x = "center", anchor_y = "center")

        cost_semesteer_title = Label(text = "Enter the cost of semester", color=(0,0,0,1), font_size=19)
        quantity_semesteers_title = Label(text = "Enter the number of semesters", color=(0,0,0,1), font_size=19)

        cost_semesteer = TextInput(hint_text = "e.g. (12000000)", halign= "center", size_hint=(0.5, 0.5), multiline=False)
        quantity_semesteer = TextInput(hint_text = "e.g. (10)", halign= "center", size_hint=(0.5, 0.5), multiline=False)

        layout_input_cost.add_widget(cost_semesteer)
        layout_input_quantity.add_widget(quantity_semesteer)
        
        container_button_calculate = AnchorLayout(anchor_x = "center", anchor_y = "center")
        calculate = Button(text = "Calculate", background_color =(0, 0.78, 0.25, 0.9), size_hint=(0.34, 1))
        container_button_calculate.add_widget(calculate)
        
        
        container_output = BoxLayout()
        output = Label(text = "Total credit: ", halign = "center", color=(0,0,0,1), font_size=19)
        container_output.add_widget(output)

        #Add widgets to the container buttons
        container_buttons.add_widget(btn_30_porcentage)
        container_buttons.add_widget(btn_60_porcentage)
        container_buttons.add_widget(btn_100_porcentage)

        #Add widges to the container inputs
        main_container.add_widget(container_tittle_welcome)
        main_container.add_widget(credit_title)
        main_container.add_widget(container_buttons)
        main_container.add_widget(cost_semesteer_title)
        main_container.add_widget(layout_input_cost)
        main_container.add_widget(quantity_semesteers_title)
        main_container.add_widget(layout_input_quantity)
        main_container.add_widget(container_button_calculate)
        main_container.add_widget(container_output)
        
        return main_container
    
        

    
if __name__ == "__main__":
    Icetex_Calculator().run()