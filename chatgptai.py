
from tkinter import *
import customtkinter
import openai
import os
import pickle

#Genel Ayarlar
root=customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x600')
#icon sayfası http://tkinter.com/images/ai_lt.ico http://tkinter.com/images/ai_lt.ico
root.iconbitmap('ai_lt.ico')

#Renklendirme Özlellikleri dark light
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root.mainloop()


"""
import os
import customtkinter as ctk

root = ctk.CTk()
root.title("ChatGPT Bot")

# Simge dosyasının tam yolunu belirleyin
current_directory = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_directory, 'ai_lt.ico')

# Simgeyi ayarlayın
try:
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Simge dosyası yüklenirken hata oluştu: {e}")

label = ctk.CTkLabel(master=root, text="Merhaba, CustomTkinter!")
label.pack(padx=20, pady=20)

root.mainloop()


text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

my_text=Text(text_frame)
my_text.grid(row=0,column=0)

"""