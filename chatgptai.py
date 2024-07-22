from tkinter import *
import customtkinter
import openai
import os
import pickle

# Importing libraries
# tkinter: GUI library

# General Settings
root = customtkinter.CTk()  # Create the main window of the application
root.title("ChatGPT Bot")
root.geometry('600x600')
# icon page http://tkinter.com/images/ai_lt.ico 
# root.iconbitmap('ai_lt.ico')

# Coloring Options: dark/light
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Functions
def speak():
    if chat_entry.get():  # Get the user's input text
        filename = "api_key"  # File where the API key is stored
        try:
            if os.path.isfile(filename):  # Check if the file exists
                with open(filename, 'rb') as input_file:  # Open the file in read mode and load the API key
                    api_sifre = pickle.load(input_file)

                openai.api_key = api_sifre

                # Call the API and get a response
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # Enter the correct model name
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": chat_entry.get()},
                    ],
                    temperature=0.7,
                    max_tokens=4000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )

                my_text.insert(END, (response["choices"][0]["message"]["content"]).strip())
                my_text.insert(END, "\n\n")
            else:
                with open(filename, 'wb') as input_file:
                    input_file.close()
                my_text.insert(END, "\n\n You forgot to get the API Key, please obtain it from the page below\n")
        except Exception as e:
            my_text.insert(END, f"\n\n An error occurred: {e}")
    else:
        my_text.insert(END, "\n\n Hey buddy, you forgot to ask a question")

def clear():
    my_text.delete(1.0, END)
    chat_entry.delete(0, END)

def key():
    filename = "api_key"
    try:
        if os.path.isfile(filename):
            with open(filename, 'rb') as input_file:
                api_key = pickle.load(input_file)
                api_entry.insert(END, api_key)
        else:
            with open(filename, 'wb') as input_file:
                input_file.close()
    except Exception as e:
        my_text.insert(END, f"\n\n An error occurred: {e}")

    root.geometry('600x600')
    api_frame.pack(pady=10)

def save_key():
    filename = "api_key"
    try:
        with open(filename, 'wb') as output_file:
            pickle.dump(api_entry.get(), output_file)
        api_entry.delete(0, END)
        api_frame.pack_forget()
    except Exception as e:
        my_text.insert(END, f"\n\n An error occurred: {e}")
    root.geometry('600x500')

# Text Frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

my_text = Text(text_frame, bg="#343638", width=65, bd=1, relief="flat", wrap=WORD, selectbackground="#1f538d")
my_text.grid(row=0, column=0)

text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

my_text.configure(yscrollcommand=text_scroll.set)

# Entry (Input Box)
chat_entry = customtkinter.CTkEntry(root, placeholder_text="What would you like to ask Chat GPT?",
    width=535,
    height=50,
    border_width=1)
chat_entry.pack(pady=10)

# Button Frame
# Create a frame for the buttons
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)

# Submit button
submit_button = customtkinter.CTkButton(button_frame, text="Ask ChatGPT", command=speak)
submit_button.grid(row=0, column=1, padx=5)

# Clear button
clear_button = customtkinter.CTkButton(button_frame, text="Clear", command=clear)
clear_button.grid(row=0, column=2, padx=5)

# API button
api_button = customtkinter.CTkButton(button_frame, text="Update API key", command=key)
api_button.grid(row=0, column=3, padx=5)

# API Key Frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=10)

api_entry = customtkinter.CTkEntry(api_frame, placeholder_text="Enter new API Key", width=350, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

api_save_button = customtkinter.CTkButton(api_frame, text="Save Key", command=save_key)
api_save_button.grid(row=0, column=1, padx=10)


# Main Loop
root.mainloop()
# Start the Tkinter application and keep the GUI running.
