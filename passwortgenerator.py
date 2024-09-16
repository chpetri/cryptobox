import tkinter as tk
import random
import string


# Funktion zur Passwortgenerierung
def generate_password():
    length = length_slider.get()  # Die Länge des Passworts vom Slider abrufen
    chars = ""  # Leerer Zeichensatz

    # Check für Kleinbuchstaben
    if lowercase_var.get():
        chars += string.ascii_lowercase

    # Check für Großbuchstaben
    if uppercase_var.get():
        chars += string.ascii_uppercase

    # Check für Sonderzeichen
    if special_chars_var.get():
        chars += string.punctuation

    # Sicherstellen, dass mindestens eine Option ausgewählt ist
    if not chars:
        result_label.config(text="Bitte mindestens eine Option wählen!")
        return

    # Passwort generieren
    password = "".join(random.choice(chars) for _ in range(length))

    # Ergebnis anzeigen
    result_label.config(text=password)


# Copy and Paste Passwort
def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Zwischenablage aktualisieren
        copy_button.config(text="Kopiert!")
    else:
        copy_button.config(text="Nichts zu kopieren")


# # Eingabefelds Synchron mit Slider
def update_slider_from_entry(event=None):
    try:
        new_length = int(length_entry.get())
        if 4 <= new_length <= 64:
            length_slider.set(new_length)
        else:
            length_entry.delete(0, tk.END)
            length_entry.insert(0, str(length_slider.get()))
    except ValueError:
        length_entry.delete(0, tk.END)
        length_entry.insert(0, str(length_slider.get()))


def update_entry_from_slider(value):
    length_entry.delete(0, tk.END)
    length_entry.insert(0, value)


# GUI Setup
root = tk.Tk()
root.title("Passwort Generator")

# Passwortlänge  Slider
tk.Label(root, text="Passwortlänge 4-64:").pack(pady=5)

# Eingabefeld für die Passwortlänge
length_entry = tk.Entry(root, width=5)
length_entry.insert(0, "12")  # Standardwert
length_entry.pack(pady=5)

# Slider für die Passwortlänge hier von 4-64
length_slider = tk.Scale(
    root, from_=4, to_=64, orient=tk.HORIZONTAL, command=update_entry_from_slider
)
length_slider.set(12)  # Standardwert für die Länge
length_slider.pack(pady=5)

# Slider ändert sich, wenn eingabe ins Feld
length_entry.bind("<Return>", update_slider_from_entry)
length_entry.bind("<FocusOut>", update_slider_from_entry)

# Checkbox für Kleinbuchstaben
lowercase_var = tk.BooleanVar(
    value=True
)  # Checkmark ist Standartmäßig gesetzt da value=True
lowercase_checkbox = tk.Checkbutton(
    root, text="Kleinbuchstaben", variable=lowercase_var
)
lowercase_checkbox.pack(pady=5)

# Checkbox für Großbuchstaben
uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Großbuchstaben", variable=uppercase_var)
uppercase_checkbox.pack(pady=5)

# Checkbox für Sonderzeichen
special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(
    root, text="Sonderzeichen", variable=special_chars_var
)
special_chars_checkbox.pack(pady=5)

# Generator Button
generate_button = tk.Button(root, text="Passwort generieren", command=generate_password)
generate_button.pack(pady=10)

# Anzeigen des PW
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Kopie buddne
copy_button = tk.Button(root, text="Passwort kopieren", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Hauptschleife
root.mainloop()
