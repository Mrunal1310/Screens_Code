import customtkinter as ctk

from home_screen import HomeScreen
from print.print_screen import PrintScreen
from edit.edit_screen import EditScreen
from file.file_screen import FileScreen
from settings.settings_screen import SettingsScreen

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter Multi-Screen App")
        self.geometry("600x400")

        self.frames = {}

        for F in (HomeScreen, PrintScreen, EditScreen, FileScreen, SettingsScreen):
            page_name = F.__name__
            frame = F(master=self, controller=self)
            frame.place(relwidth=1, relheight=1)
            self.frames[page_name] = frame

        self.show_frame("HomeScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()