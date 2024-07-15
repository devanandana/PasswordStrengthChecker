import tkinter as tk
from tkinter import messagebox
import re
import random
import string
import math
from PIL import Image, ImageTk

def calculate_entropy(password):
    length = len(password)
    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'\d', password):
        pool_size += 10
    if re.search(r'[\W_]', password):
        pool_size += len(string.punctuation)
    entropy = length * math.log2(pool_size)
    return entropy

def check_password_strength(password):
    length = len(password) >= 8
    lower = re.search(r'[a-z]', password)
    upper = re.search(r'[A-Z]', password)
    digit = re.search(r'\d', password)
    special = re.search(r'[\W_]', password)
    
    feedback = []
    if not length:
        feedback.append("Password should be at least 8 characters long.")
    if not lower:
        feedback.append("Password should contain at least one lowercase letter.")
    if not upper:
        feedback.append("Password should contain at least one uppercase letter.")
    if not digit:
        feedback.append("Password should contain at least one digit.")
    if not special:
        feedback.append("Password should contain at least one special character.")
    
    strength = len(feedback) == 0
    entropy = calculate_entropy(password) if strength else None
    return strength, feedback, entropy

def evaluate_password(event=None):
    password = entry.get()
    strength, feedback, entropy = check_password_strength(password)
    if strength:
        strength_var.set(f"Strong (Entropy: {entropy:.2f} bits)")
        strength_label.config(fg="green")
    else:
        strength_var.set("Weak: " + "\n".join(feedback))
        strength_label.config(fg="red")

def generate_password():
    while True:
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        strength, feedback, entropy = check_password_strength(password)
        if strength:
            entry.delete(0, tk.END)
            entry.insert(0, password)
            strength_var.set("")
            strength_label.config(fg="black")
            break

def toggle_password_visibility():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_button.config(image=eye_open_image)
    else:
        entry.config(show='*')
        toggle_button.config(image=eye_closed_image)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")
root.resizable(False, False)

# Try to load and resize the images
try:
    eye_open_img = Image.open("eye_open.png").resize((30, 30))
    eye_closed_img = Image.open("eye_closed.png").resize((30, 30))
    eye_open_image = ImageTk.PhotoImage(eye_open_img)
    eye_closed_image = ImageTk.PhotoImage(eye_closed_img)
except Exception as e:
    print(f"Error loading images: {e}")
    eye_open_image = None
    eye_closed_image = None

tk.Label(root, text="Enter Password:", font=("Helvetica", 12)).pack(pady=10)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, show="*", font=("Helvetica", 12), width=30)
entry.pack(side=tk.LEFT, padx=5)
entry.bind("<KeyRelease>", evaluate_password)

if eye_open_image and eye_closed_image:
    toggle_button = tk.Button(entry_frame, command=toggle_password_visibility, image=eye_closed_image, width=30, height=30)
else:
    toggle_button = tk.Button(entry_frame, text="Show", command=toggle_password_visibility, font=("Helvetica", 10))

toggle_button.pack(side=tk.LEFT, padx=5)

strength_var = tk.StringVar()
strength_label = tk.Label(root, textvariable=strength_var, font=("Helvetica", 12))
strength_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Check Strength", command=evaluate_password, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Generate Strong Password", command=generate_password, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)

root.mainloop()

