import customtkinter as ctk 

def main_window():
    
    root = ctk.CTk()
    root.title("Warning")
    root.geometry("300x100")
    
def open_warning(message1, message2):
    warning=ctk.CTkToplevel()  
    warning.title("Warning")
    warning.geometry("440x150")  
    warning.resizable(False, False)  
    
    warning.transient()  
    warning.grab_set()       
    warning.focus_force() 
    
    frame=ctk.CTkFrame(warning,fg_color="white",width=450,height=150, corner_radius=0)
    frame.grid(row=0, column=0, sticky="news")
    
    label=ctk.CTkLabel(frame, text="Warning",text_color="white", fg_color="#A83232",width=450, anchor="w",font=("Arial", 18, 'bold'))
    label.grid(row=0, column=0, sticky="news")
    
    msg_label_1 = ctk.CTkLabel(frame, text=message1, text_color="black", fg_color="white",
                            anchor="w", font=("Arial", 16))
    msg_label_1.grid(row=1, column=0, padx=10, pady=(5, 0), sticky="w")

    msg_label_2 = ctk.CTkLabel(frame, text=message2, text_color="black", fg_color="white",
                            anchor="w", font=("Arial", 16))
    msg_label_2.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")
    
    button=ctk.CTkButton(frame, text="OK",text_color="black",anchor="center", fg_color="white",border_width=1,corner_radius=0,command=warning.destroy, font=("Arial", 16,))
    button.grid(row=3, column=0, padx=40, pady=20,sticky="w")
    
    button=ctk.CTkButton(frame, text="Back",text_color="black", anchor="center",fg_color="white",border_width=1,corner_radius=0,command=warning.destroy, font=("Arial", 16,))
    button.grid(row=3, column=0, padx=60, pady=20,sticky="e")
    