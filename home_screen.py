import customtkinter as ctk

class HomeScreen(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        ctk.CTkLabel(self, text="🏠 Home Screen", font=("Arial", 24)).pack(pady=20)

        ctk.CTkButton(self, text="🖨️ Print", command=lambda: controller.show_frame("PrintScreen")).pack(pady=10)
        ctk.CTkButton(self, text="✏️ Edit", command=lambda: controller.show_frame("EditScreen")).pack(pady=10)
        ctk.CTkButton(self, text="📁 File", command=lambda: controller.show_frame("FileScreen")).pack(pady=10)
        ctk.CTkButton(self, text="⚙️ Settings", command=lambda: controller.show_frame("SettingsScreen")).pack(pady=10)