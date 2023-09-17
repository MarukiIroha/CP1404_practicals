from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicWidgetsApp(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_phone:
            # create a label for each data entry, specifying the text
            temp_label = Label(text=name)
            # set the label's background colour
            temp_label.background_color = NEW_COLOUR
            # add the label to the "entries_box" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicWidgetsApp().run()

