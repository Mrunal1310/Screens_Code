import customtkinter as ctk
import os
from PIL import Image

def create_software_window(parent, base):
    # Hide the old screen (like BaseScreen)
    base.pack_forget()

    # Dictionary to store information
    info_dict = {
        "Language Pack": "V108011",
        "Hardware version": "V70146",
        "Software version": "SU1DBSV15.8.9-12.7",
        "Firmware version": "V230620",
        "Date version": "V1039",
        "Build time": "Mar 27 2024",
        "Rfid version": "RF0115"
    }

    # Create the Software Frame inside parent (root)
    software_frame = ctk.CTkFrame(parent, fg_color="white", corner_radius=0)
    software_frame.grid(row=0, column=0, sticky="nsew")  # Using grid instead of pack

    # Configure grid for software_frame
    software_frame.columnconfigure(0, weight=1)
    software_frame.rowconfigure(1, weight=1)

    # --- Frame for Title ---
    frame1 = ctk.CTkFrame(software_frame, fg_color="#A83232", corner_radius=0)
    frame1.grid(row=0, column=0, sticky="new")
    frame1.columnconfigure(0, weight=1)

    # Load Close Button Image
    script_dir = os.path.dirname(os.path.dirname(__file__))  # Script directory
    image_path = os.path.join(script_dir, "images", "close_icon.png")
    
    try:
        close_img = Image.open(image_path)
        close_ctk_img = ctk.CTkImage(light_image=close_img, size=(20, 20))

        close_button = ctk.CTkButton(
            frame1, text="", image=close_ctk_img,
            command=lambda: close_software_frame(software_frame, base),
            hover_color="#A83232", fg_color="#A83232", width=50, height=20, corner_radius=0
        )
        close_button.grid(row=0, column=1, sticky='e', padx=10, pady=5)
    except Exception as e:
        print(f"Image loading failed: {e}")

    # Title Label
    label1 = ctk.CTkLabel(
        frame1, text="Software", text_color="white", fg_color="#A83232",
        font=("Arial", 20, 'bold'), anchor='center'
    )
    label1.grid(row=0, column=0, pady=5, padx=0, sticky="new")

    # --- Frame for content ---
    frame2 = ctk.CTkFrame(software_frame, fg_color="white", corner_radius=0)
    frame2.grid(row=1, column=0, pady=50, sticky="nsew")

    frame2.columnconfigure((0, 1), weight=1)
    frame2.rowconfigure(tuple(range(len(info_dict) + 2)), weight=1)

    # Labels for Software Info
    for i, (key, value) in enumerate(info_dict.items()):
        ctk.CTkLabel(
            frame2, text=f"{key}:", text_color="#A83232", anchor='w', font=("Arial", 18)
        ).grid(row=i, column=0, padx=100, pady=10, sticky="w")
        ctk.CTkLabel(
            frame2, text=value, text_color="#A83232", anchor='w', font=("Arial", 18)
        ).grid(row=i, column=1, padx=0, pady=10, sticky="w")

    # Buttons
    check_button = ctk.CTkButton(
        frame2, text="Check", text_color="#A83232", fg_color="#C4E3ED",
        font=("Arial", 18), corner_radius=0
    )
    check_button.grid(row=len(info_dict), column=0, pady=20, sticky="w", padx=100)

    reboot_button = ctk.CTkButton(
        frame2, text="Reboot", text_color="#A83232", fg_color="#C4E3ED",
        font=("Arial", 18), corner_radius=0
    )
    reboot_button.grid(row=len(info_dict), column=1, pady=20, sticky="w")

    return software_frame


def close_software_frame(software_frame, base):
    # Destroy the software window and re-display the base
    software_frame.destroy()
    base.pack(fill="both", expand=True)
