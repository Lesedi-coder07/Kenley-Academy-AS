import tkinter as tk
from tkinter import ttk 

def display_message(text):
    """Displays a message in a styled window."""
    root = tk.Tk()
    root.title("Message Display")

    # Configure a style for the label
    label_style = ttk.Style()  # Use ttk.Style()
    label_style.configure("Message.TLabel",
                          font=("Arial", 16),  # Slightly larger font
                          padding=20,         # More padding around the text
                          wraplength=400)       # Wrap text if it's too long

    # Use a themed label (ttk.Label) with the configured style
    label = ttk.Label(root, text=text, style="Message.TLabel")  # Use ttk.Label
    label.pack()

    # Configure a style for the button
    button_style = ttk.Style()  # Use ttk.Style()
    button_style.configure("OK.TButton",
                           font=("Arial", 12),
                           padding=10,
                           background="#4CAF50",  # Green background
                           foreground="white")   # White text

    # Use a themed button (ttk.Button) with the configured style
    ok_button = ttk.Button(root, text="OK", command=root.destroy, style="OK.TButton")  # Use ttk.Button
    ok_button.pack(pady=15)

    # Center the window on the screen
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

    root.mainloop()
    """Displays a message in a styled window."""
    root = tk.Tk()
    root.title("Message Display")

    # Configure a style for the label
    label_style = tk.Style()
    label_style.configure("Message.TLabel", 
                          font=("Arial", 16),  # Slightly larger font
                          padding=20,         # More padding around the text
                          wraplength=400)       # Wrap text if it's too long

    # Use a themed label (tk.Label) with the configured style
    label = tk.Label(root, text=text, style="Message.TLabel")
    label.pack()

    # Configure a style for the button
    button_style = tk.Style()
    button_style.configure("OK.TButton", 
                           font=("Arial", 12),
                           padding=10,
                           background="#4CAF50",  # Green background
                           foreground="white")   # White text

    # Use a themed button (tk.Button) with the configured style
    ok_button = tk.Button(root, text="OK", command=root.destroy, style="OK.TButton")
    ok_button.pack(pady=15)

    # Center the window on the screen
    root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

    root.mainloop()


# Example usage (students modify this part)


name = input("Enter your name: ")
responses = ["Hello there!", "Nice to meet you!", "Welcome!", "Hope you have a great day!"]

if name.lower() == "admin":
    display_message("Welcome, Admin!")
else:
    display_message(f"{name}, {responses[len(name) % len(responses)]}")

if name.lower() == "admin":
    display_message("Welcome, Admin!")
else:
    display_message(f"hi {name}")