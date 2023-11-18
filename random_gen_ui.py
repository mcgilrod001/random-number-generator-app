import customtkinter as ct
import random
import randomf as rf

# customtkinter basic setup
ct.set_default_color_theme('dark-blue')
ct.set_appearance_mode('dark')
root = ct.CTk()
root.geometry("500x450")
root.title("Random Number Generator")

# customtkinter widgets
frame1 = ct.CTkFrame(root)
frame1.pack(pady=20  , padx=50, fill="both", expand=True)
title = ct.CTkLabel(frame1, text="Random Number Generator", font=("Arial", 20))
title.pack(pady=10)
# output_label = ct.CTkLabel(frame1, text="", font=("Arial", 15))
# output_label.pack(pady=12,padx=10)
# button commands
# single random number
def get_single_random():
    max_num = int(max_random.get())
    min_num = int(min_random.get())
    # currently throwing an error
    random_num = random.randint(min_num, max_num)

# entrys
max_random = ct.CTkEntry(frame1, placeholder_text="Max Number")
min_random = ct.CTkEntry(frame1, placeholder_text="Min Number")
max_random.pack(pady=10, padx=10)
min_random.pack(pady=10, padx=10)
# buttons
single_random_button = ct.CTkButton(frame1, text="Generate a Single Random Number", font=("Arial", 15), command=get_single_random)
single_random_button.pack(pady=10)
multi_random_button = ct.CTkButton(frame1, text="Generate Multiple Random Numbers", font=("Arial", 15))
multi_random_button.pack(pady=10)
list_random_button = ct.CTkButton(frame1, text="Generate a Random List", font=("Arial", 15))
list_random_button.pack(pady=10)

















root.mainloop()

