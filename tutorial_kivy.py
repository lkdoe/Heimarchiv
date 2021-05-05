# import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.inside = GridLayout()
        self.inside.cols = 2

        self.cols = 1
        self.inside.add_widget(Label(text="First Name: "))
        self.firstName = TextInput(multiline=False)
        self.inside.add_widget(self.firstName)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.add_widget(self.inside)  # Grid for the text labels and input fields

        self.inside.add_widget(Label(text="E-Mail: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        first = self.firstName.text
        last = self.lastName.text
        email = self.email.text

        print("Name: ", first + ", Last name: ", last, "\nE-mail: ", email)
        self.firstName.text = ""
        self.lastName.text = ""
        self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
