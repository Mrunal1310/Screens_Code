import customtkinter as ctk

class EditScreen(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        ctk.CTkLabel(self, text="✏️ Edit Screen", font=("Arial", 20)).pack(pady=20)
        ctk.CTkButton(self, text="⬅ Back", command=lambda: controller.show_frame("HomeScreen")).pack()