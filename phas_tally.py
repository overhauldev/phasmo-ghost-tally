import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import json
import os

# File to save tally counts
TALLY_FILE = 'tally_counts.json'

# List of ghost names
GHOST_NAMES = [
    "Banshee", "Demon", "Deogen", "Goryo", "Hantu", "Jinn", "Mare", "Moroi", "Myling", "Obake",
    "Oni", "Onryo", "Phantom", "Poltergeist", "Raiju", "Revenant", "Shade", "Spirit", "Thaye",
    "The Mimic", "The Twins", "Wraith", "Yokai", "Yurei"
]

# Load tally counts from file
def load_tally_counts():
    if os.path.exists(TALLY_FILE):
        with open(TALLY_FILE, 'r') as file:
            return json.load(file)
    return {name: 0 for name in GHOST_NAMES}

# Save tally counts to file
def save_tally_counts():
    with open(TALLY_FILE, 'w') as file:
        json.dump(tally_counts, file)

# Increment tally count for a specific entry
def increment_tally(entry):
    tally_counts[entry] += 1
    save_tally_counts()
    update_labels()

# Update labels in the UI
def update_labels():
    for entry, label in labels.items():
        label.config(text=f'{entry}: {tally_counts[entry]}')

# Update entry names in the UI
def update_entry_names():
    global tally_counts
    new_tally_counts = {}
    for entry, entry_var in entry_vars.items():
        new_entry_name = entry_var.get()
        new_tally_counts[new_entry_name] = tally_counts.pop(entry)
    tally_counts = new_tally_counts
    save_tally_counts()
    update_labels()

# Clear all tally counts
def clear_tallies():
    if messagebox.askyesno("Clear Tallies", "Are you sure you want to clear all tallies?"):
        global tally_counts
        tally_counts = {entry: 0 for entry in tally_counts}
        save_tally_counts()
        update_labels()

# Display bar chart
def display_bar_chart():
    entries = list(tally_counts.keys())
    counts = list(tally_counts.values())
    cmap = plt.colormaps.get_cmap('tab20')
    colors = [cmap(i / len(entries)) for i in range(len(entries))]

    plt.figure(figsize=(10, 6))
    plt.bar(entries, counts, color=colors)
    plt.xlabel('Entries')
    plt.ylabel('Counts')
    plt.title('Tally Counts Bar Chart')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Display pie chart
def display_pie_chart():
    entries = list(tally_counts.keys())
    counts = list(tally_counts.values())
    cmap = plt.colormaps.get_cmap('tab20')
    colors = [cmap(i / len(entries)) for i in range(len(entries))]

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=entries, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Tally Counts Pie Chart')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# Initialize tally counts
tally_counts = load_tally_counts()

# Create main window
root = tk.Tk()
root.title('Tally Counter')

# Create labels, entry fields, and buttons for each entry
labels = {}
entry_vars = {}
for entry in tally_counts:
    frame = tk.Frame(root)
    frame.pack(fill='x')
    entry_var = tk.StringVar(value=entry)
    entry_field = tk.Entry(frame, textvariable=entry_var, width=20)
    entry_field.pack(side='left')
    entry_vars[entry] = entry_var
    label = tk.Label(frame, text=f'{entry}: {tally_counts[entry]}', width=20)
    label.pack(side='left')
    button = tk.Button(frame, text='Increment', command=lambda e=entry: increment_tally(e))
    button.pack(side='right')
    labels[entry] = label

# Create button to update entry names
update_names_button = tk.Button(root, text='Update Entry Names', command=update_entry_names)
update_names_button.pack(fill='x')

# Create button to clear tallies
clear_tallies_button = tk.Button(root, text='Clear Entry Tallies', command=clear_tallies)
clear_tallies_button.pack(fill='x')

# Create buttons to display charts
bar_chart_button = tk.Button(root, text='Display Bar Chart', command=display_bar_chart)
bar_chart_button.pack(fill='x')

pie_chart_button = tk.Button(root, text='Display Pie Chart', command=display_pie_chart)
pie_chart_button.pack(fill='x')

# Start the main loop
root.mainloop()