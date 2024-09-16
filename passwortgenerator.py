import tkinter as tk
from tkinter import ttk
import random
import string


# Funktion zur Passwortgenerierung
def generate_password():
    length = int(length_slider.get())  # Die Länge des Passworts vom int abrufen
    chars = ""  # Leerer Zeichensatz, den wir mit Optionen füllen

    # Check für Kleinbuchstaben
    if lowercase_var.get():
        chars += string.ascii_lowercase

    # Check für Großbuchstaben
    if uppercase_var.get():
        chars += string.ascii_uppercase

    # Check für Ziffern
    if digits_var.get():
        chars += string.digits

    # Check für Sonderzeichen
    if special_chars_var.get():
        chars += string.punctuation

    # Sicherstellen, dass mindestens eine Option ausgewählt ist
    if not chars:
        result_label.config(text="Bitte mindestens eine Option wählen!")
        return

    # Passwort generieren
    password = "".join(random.choice(chars) for _ in range(length))

    # Das Ergebnis im Label anzeigen
    result_label.config(text=password)


# Funktion zum Kopieren des Passworts in die Zwischenablage
def copy_to_clipboard():
    password = result_label.cget("text")  # Das generierte Passwort holen
    if password:
        root.clipboard_clear()  # Zwischenablage leeren
        root.clipboard_append(password)  # Passwort in die Zwischenablage kopieren
        root.update()  # Zwischenablage aktualisieren
        copy_button.config(text="Kopiert!")  # Button-Text ändern
    else:
        copy_button.config(text="Nichts zu kopieren")


# Funktion zum Synchronisieren des Sliders mit dem Eingabefeld
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


# Funktion zum Synchronisieren des Eingabefelds mit dem Slider
def update_entry_from_slider(value):
    length_entry.delete(0, tk.END)
    length_entry.insert(0, value)


# GUI Setup
root = tk.Tk()
root.title("Super Crypto Suite")

# Style Setup (für ttk-Widgets)
style = ttk.Style(root)
style.theme_use("clam")  # Wählt ein modernes Theme
style.configure("TButton", padding=6, relief="flat", background="#ccc")

# Notebook für Tabs
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Frame für Passwortgenerator
password_generator_tab = ttk.Frame(notebook)
notebook.add(password_generator_tab, text="Passwortgenerator")

# Frame für Passwortmanager (Platzhalter)
password_manager_tab = ttk.Frame(notebook)
notebook.add(password_manager_tab, text="Passwortmanager")

# Frame für File Encryptor (Platzhalter)
file_encryptor_tab = ttk.Frame(notebook)
notebook.add(file_encryptor_tab, text="File Encryptor")

### Passwortgenerator GUI ###

# Passwortlänge mit Slider einstellen
ttk.Label(password_generator_tab, text="Passwortlänge:").pack(pady=5)

# Eingabefeld für die Passwortlänge
length_entry = ttk.Entry(password_generator_tab, width=5)
length_entry.insert(0, "12")  # Standardwert
length_entry.pack(pady=5)

# Slider für die Passwortlänge
length_slider = ttk.Scale(
    password_generator_tab,
    from_=4,
    to_=64,
    orient=tk.HORIZONTAL,
    command=update_entry_from_slider,
)
length_slider.set(12)  # Standardwert für die Länge
length_slider.pack(pady=5)

# Aktualisieren des Sliders, wenn die Länge manuell im Eingabefeld geändert wird
length_entry.bind("<Return>", update_slider_from_entry)  # Aktualisierung bei "Enter"
length_entry.bind(
    "<FocusOut>", update_slider_from_entry
)  # Aktualisierung beim Verlassen des Feldes

# Checkbox für Kleinbuchstaben
lowercase_var = tk.BooleanVar(value=True)  # Standardmäßig aktiviert
lowercase_checkbox = ttk.Checkbutton(
    password_generator_tab, text="Kleinbuchstaben", variable=lowercase_var
)
lowercase_checkbox.pack(pady=5)

# Checkbox für Großbuchstaben
uppercase_var = tk.BooleanVar()
uppercase_checkbox = ttk.Checkbutton(
    password_generator_tab, text="Großbuchstaben", variable=uppercase_var
)
uppercase_checkbox.pack(pady=5)

# Checkbox für Ziffern
digits_var = tk.BooleanVar()
digits_checkbox = ttk.Checkbutton(
    password_generator_tab, text="Ziffern", variable=digits_var
)
digits_checkbox.pack(pady=5)

# Checkbox für Sonderzeichen
special_chars_var = tk.BooleanVar()
special_chars_checkbox = ttk.Checkbutton(
    password_generator_tab, text="Sonderzeichen", variable=special_chars_var
)
special_chars_checkbox.pack(pady=5)

# Button zum Generieren des Passworts
generate_button = ttk.Button(
    password_generator_tab, text="Passwort generieren", command=generate_password
)
generate_button.pack(pady=10)

# Label zum Anzeigen des generierten Passworts
result_label = ttk.Label(password_generator_tab, text="")
result_label.pack(pady=5)

# Button zum Kopieren des Passworts in die Zwischenablage
copy_button = ttk.Button(
    password_generator_tab, text="Passwort kopieren", command=copy_to_clipboard
)
copy_button.pack(pady=5)

### Passwortmanager Tab (Platzhalter) ###
ttk.Label(password_manager_tab, text="Passwortmanager (noch zu implementieren)").pack(
    pady=20
)

### File Encryptor Tab (Platzhalter) ###
ttk.Label(file_encryptor_tab, text="File Encryptor (noch zu implementieren)").pack(
    pady=20
)

# Hauptschleife für die GUI
root.mainloop()
